#!/usr/bin/env python3
"""
Apple Documentation MCP Remote Client
=====================================

Stdio-to-HTTP proxy for connecting Claude Code to a remote MCP server.
Handles the streamable-http protocol with SSE (Server-Sent Events).

SETUP:
1. Change SERVER_URL below to point to your deployed server
2. Add this to your Claude MCP configuration:

{
  "apple-docs": {
    "type": "stdio",
    "command": "python3",
    "args": ["/path/to/apple_docs_remote_client.py"]
  }
}

3. Restart Claude

Repository: https://github.com/averyy/apple-developer-docs
"""

import asyncio
import json
import os
import sys
import logging
from typing import Dict, Any, Optional
from datetime import datetime, timedelta
import aiohttp

# ============================================================================
# CONFIGURATION - Change this to your deployed server
# ============================================================================
# Check environment variable first (for local client override)
SERVER_URL = os.getenv('MCP_SERVER_URL', "https://xdocs.dev/mcp")  # Public server URL

# Setup logging
logging.basicConfig(
    level=logging.WARNING,  # Set to DEBUG for troubleshooting
    format='[%(asctime)s] %(levelname)s: %(message)s',
    stream=sys.stderr
)
logger = logging.getLogger(__name__)

class MCPRemoteProxy:
    """Proxy between stdio (Claude) and HTTP streamable transport (server)"""

    def __init__(self, server_url: str, api_key: Optional[str] = None):
        self.server_url = server_url.rstrip('/')
        if not self.server_url.endswith('/'):
            self.server_url += '/'
        self.api_key = api_key
        self.session: Optional[aiohttp.ClientSession] = None
        self.session_id: Optional[str] = None
        self.session_created_at: Optional[datetime] = None
        self._reconnection_lock = asyncio.Lock()
        self._last_activity = datetime.now()
        
    async def start(self):
        """Initialize the HTTP session"""
        # Create session with connection management
        connector = aiohttp.TCPConnector(
            limit=10,
            limit_per_host=5,
            ttl_dns_cache=300,
            force_close=True
        )
        timeout = aiohttp.ClientTimeout(total=120, connect=10)
        self.session = aiohttp.ClientSession(
            connector=connector,
            timeout=timeout
        )
        logger.debug(f"Initialized session for {self.server_url}")
        
    async def stop(self):
        """Clean up resources"""
        if self.session:
            await self.session.close()
            self.session = None
            
    def _is_session_error(self, status: int, error_text: str) -> bool:
        """Check if the error is session-related"""
        # Common session error patterns
        if status == 400 and "No valid session ID" in error_text:
            return True
        if status == 401:  # Unauthorized
            return True
        if status == 403 and "session" in error_text.lower():
            return True
        if "session expired" in error_text.lower():
            return True
        # Some servers return 500 for session errors during initialization
        if status == 500 and self.session_id and self.session_id != "":
            # If we have a session ID and get 500, it might be invalid
            # Only treat as session error if we had a non-empty session
            return True
        return False
    
    def _should_refresh_session(self) -> bool:
        """Check if session should be proactively refreshed"""
        if not self.session_created_at:
            return False
        age = datetime.now() - self.session_created_at
        return age > timedelta(hours=23)
    
    async def _reconnect_and_retry(self, original_request: Dict[str, Any]) -> None:
        """Reconnect and retry the original request"""
        logger.info("Reconnecting session...")
        
        # Clear session state
        self.session_id = None
        self.session_created_at = None
        
        # Recreate HTTP session to avoid stale connections
        if self.session:
            await self.session.close()
            self.session = None
        await self.start()
        
        # Send initialize request
        logger.info("Sending automatic re-initialization")
        init_request = {
            "jsonrpc": "2.0",
            "id": f"auto-init-{original_request.get('id', 'unknown')}",
            "method": "initialize",
            "params": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "clientInfo": {
                    "name": "apple-docs-remote",
                    "version": "1.1.0"
                }
            }
        }
        
        await self.send_request(init_request)
        
        # Retry original request
        logger.info("Retrying original request after re-initialization")
        await self.send_request(original_request)
    
    async def send_request(self, request: Dict[str, Any]) -> None:
        """Send request to HTTP server and handle SSE response"""
        if not self.session:
            await self.start()
        
        # Check if session needs proactive refresh
        if self._should_refresh_session() and request.get("method") != "initialize":
            logger.info("Session is old, proactively refreshing")
            async with self._reconnection_lock:
                if self._should_refresh_session():
                    await self._reconnect_and_retry(request)
                    return
        
        self._last_activity = datetime.now()
            
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json, text/event-stream'
        }

        # Add API key if we have one
        if self.api_key:
            headers['Authorization'] = f'Bearer {self.api_key}'

        # Add session ID if we have one
        if self.session_id:
            headers['MCP-Session-Id'] = self.session_id
            
        try:
            logger.debug(f"Sending request: {request}")
            
            # Send the request
            async with self.session.post(
                self.server_url,
                json=request,
                headers=headers
            ) as response:
                # Store session ID
                if 'mcp-session-id' in response.headers:
                    self.session_id = response.headers['mcp-session-id']
                    self.session_created_at = datetime.now()
                    logger.debug(f"Got session ID: {self.session_id}")
                
                # Check content type
                content_type = response.headers.get('content-type', '')
                
                if response.status != 200:
                    error_text = await response.text()
                    
                    # Check if it's a session error
                    if self._is_session_error(response.status, error_text):
                        logger.info(f"Session error detected: {response.status} - {error_text[:100]}")
                        
                        # If this is an initialize request, don't retry
                        if request.get("method") == "initialize":
                            error_response = {
                                "jsonrpc": "2.0",
                                "id": request.get("id"),
                                "error": {
                                    "code": -32603,
                                    "message": f"HTTP {response.status}: {error_text}"
                                }
                            }
                            print(json.dumps(error_response, separators=(',', ':')))
                            sys.stdout.flush()
                            return
                        
                        # Handle reconnection with lock
                        async with self._reconnection_lock:
                            # Double-check we still need to reconnect
                            if self._is_session_error(response.status, error_text):
                                await self._reconnect_and_retry(request)
                                return
                    
                    error_response = {
                        "jsonrpc": "2.0",
                        "id": request.get("id"),
                        "error": {
                            "code": -32603,
                            "message": f"HTTP {response.status}: {error_text}"
                        }
                    }
                    print(json.dumps(error_response, separators=(',', ':')))
                    sys.stdout.flush()
                    return
                
                if 'text/event-stream' in content_type:
                    # Handle SSE response by reading lines
                    buffer = ""
                    event_data = None
                    
                    async for chunk in response.content:
                        text = chunk.decode('utf-8')
                        buffer += text
                        
                        # Process complete lines
                        while '\n' in buffer:
                            line, buffer = buffer.split('\n', 1)
                            line = line.strip()
                            
                            if line.startswith('data: '):
                                event_data = line[6:]  # Remove 'data: ' prefix
                            elif line == '' and event_data:
                                # Empty line signals end of event
                                try:
                                    response_data = json.loads(event_data)
                                    logger.debug(f"Got SSE response: {response_data}")
                                    print(json.dumps(response_data, separators=(',', ':')))
                                    sys.stdout.flush()
                                    
                                    # Return after first complete response
                                    return
                                except json.JSONDecodeError as e:
                                    logger.error(f"Failed to parse SSE data: {e}")
                                    logger.error(f"Raw data: {event_data}")
                                event_data = None
                else:
                    # Handle regular JSON response
                    response_data = await response.json()
                    logger.debug(f"Got JSON response: {response_data}")
                    print(json.dumps(response_data, separators=(',', ':')))
                    sys.stdout.flush()
                    
        except aiohttp.ClientError as e:
            logger.error(f"HTTP client error: {e}")
            error_response = {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "error": {
                    "code": -32603,
                    "message": f"Connection error: {str(e)}"
                }
            }
            print(json.dumps(error_response, separators=(',', ':')))
            sys.stdout.flush()
        except Exception as e:
            logger.error(f"Unexpected error: {e}", exc_info=True)
            error_response = {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "error": {
                    "code": -32603,
                    "message": f"Internal error: {str(e)}"
                }
            }
            print(json.dumps(error_response, separators=(',', ':')))
            sys.stdout.flush()
    
    async def run_stdio_loop(self):
        """Main loop reading from stdin and forwarding to HTTP"""
        logger.info(f"Starting stdio proxy for {self.server_url}")
        
        loop = asyncio.get_event_loop()
        reader = asyncio.StreamReader()
        protocol = asyncio.StreamReaderProtocol(reader)
        await loop.connect_read_pipe(lambda: protocol, sys.stdin)
        
        while True:
            try:
                # Read line from stdin
                line = await reader.readline()
                if not line:
                    logger.info("Stdin closed, exiting")
                    break
                    
                line = line.decode('utf-8').strip()
                if not line:
                    continue
                    
                logger.debug(f"Received from stdin: {line}")
                
                # Parse JSON-RPC request
                try:
                    request = json.loads(line)
                except json.JSONDecodeError as e:
                    logger.error(f"Invalid JSON from stdin: {e}")
                    error_response = {
                        "jsonrpc": "2.0",
                        "id": None,
                        "error": {
                            "code": -32700,
                            "message": f"Parse error: {str(e)}"
                        }
                    }
                    print(json.dumps(error_response, separators=(',', ':')))
                    sys.stdout.flush()
                    continue
                
                # Forward to HTTP server
                await self.send_request(request)
                
            except asyncio.CancelledError:
                logger.info("Loop cancelled")
                break
            except Exception as e:
                logger.error(f"Error in stdio loop: {e}", exc_info=True)
                error_response = {
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {
                        "code": -32603,
                        "message": f"Internal error: {str(e)}"
                    }
                }
                print(json.dumps(error_response, separators=(',', ':')))
                sys.stdout.flush()

async def test_connection(api_key: Optional[str] = None):
    """Test connection to remote server"""
    print(f"Testing connection to: {SERVER_URL}", file=sys.stderr)

    # Test with proper initialize request
    test_request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {"tools": {}},
            "clientInfo": {
                "name": "test-client",
                "version": "1.0.0"
            }
        }
    }

    proxy = MCPRemoteProxy(SERVER_URL, api_key=api_key)
    try:
        await proxy.start()

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json, text/event-stream'
        }

        # Add API key if provided
        if api_key:
            headers['Authorization'] = f'Bearer {api_key}'

        print("Sending initialize request...", file=sys.stderr)
        async with proxy.session.post(
            proxy.server_url,
            json=test_request,
            headers=headers
        ) as response:
            print(f"Response status: {response.status}", file=sys.stderr)
            
            if response.status == 200:
                # Handle SSE response
                if 'text/event-stream' in response.headers.get('content-type', ''):
                    print("Reading SSE response...", file=sys.stderr)
                    buffer = ""
                    event_data = None
                    
                    async for chunk in response.content:
                        text = chunk.decode('utf-8')
                        buffer += text
                        
                        while '\n' in buffer:
                            line, buffer = buffer.split('\n', 1)
                            line = line.strip()
                            
                            if line.startswith('data: '):
                                event_data = line[6:]
                            elif line == '' and event_data:
                                try:
                                    data = json.loads(event_data)
                                    print(f"Response: {json.dumps(data, indent=2)}", file=sys.stderr)
                                    if "result" in data:
                                        print("✅ Connection successful!", file=sys.stderr)
                                        return True
                                    else:
                                        print(f"❌ Error in response", file=sys.stderr)
                                        return False
                                except Exception as e:
                                    print(f"❌ Parse error: {e}", file=sys.stderr)
                                    return False
                else:
                    data = await response.json()
                    print(f"Response: {json.dumps(data, indent=2)}", file=sys.stderr)
            else:
                error_text = await response.text()
                print(f"❌ HTTP {response.status}: {error_text}", file=sys.stderr)
                return False
                
    except Exception as e:
        print(f"❌ Connection failed: {e}", file=sys.stderr)
        return False
    finally:
        await proxy.stop()

def parse_args():
    """Parse command line arguments"""
    import argparse
    parser = argparse.ArgumentParser(
        description="Apple Documentation MCP Remote Client - STDIO-to-HTTP proxy",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument(
        "--server-url",
        default=os.getenv('MCP_SERVER_URL', SERVER_URL),
        help="URL of the remote MCP server (default: from env or config)"
    )
    parser.add_argument(
        "--api-key",
        default=os.getenv('MCP_API_KEY'),
        help="API key for authentication (required, can also use MCP_API_KEY env var)"
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Test connection to the server and exit"
    )
    return parser.parse_args()


async def main():
    """Main entry point"""
    args = parse_args()

    # Override global SERVER_URL with args
    server_url = args.server_url
    api_key = args.api_key

    # API key is required
    if not api_key:
        print("", file=sys.stderr)
        print("Error: MCP_API_KEY is required", file=sys.stderr)
        print("", file=sys.stderr)
        print("Get your API key at: https://xdocs.dev", file=sys.stderr)
        print("", file=sys.stderr)
        print("Set via environment variable:", file=sys.stderr)
        print("  export MCP_API_KEY=your-api-key", file=sys.stderr)
        print("", file=sys.stderr)
        print("Or pass via command line:", file=sys.stderr)
        print("  python3 apple_docs_remote_client.py --api-key your-api-key", file=sys.stderr)
        print("", file=sys.stderr)
        sys.exit(1)

    if args.test:
        # Override global for test
        global SERVER_URL
        SERVER_URL = server_url
        success = await test_connection(api_key=api_key)
        sys.exit(0 if success else 1)

    # Check if running interactively
    if sys.stdin.isatty():
        print("Apple Documentation MCP Remote Client", file=sys.stderr)
        print(f"Server: {server_url}", file=sys.stderr)
        print("", file=sys.stderr)
        print("This should be run by Claude, not directly.", file=sys.stderr)
        print("Run with --test to test connection", file=sys.stderr)
        print("Run with --help for setup instructions", file=sys.stderr)
        sys.exit(1)

    # Run the proxy
    proxy = MCPRemoteProxy(server_url, api_key=api_key)
    try:
        await proxy.run_stdio_loop()
    finally:
        await proxy.stop()

if __name__ == "__main__":
    # Check for required dependencies
    try:
        import aiohttp
    except ImportError:
        print("Error: Missing required dependency", file=sys.stderr)
        print("Please install: pip install aiohttp", file=sys.stderr)
        sys.exit(1)
    
    # Run async main
    asyncio.run(main())