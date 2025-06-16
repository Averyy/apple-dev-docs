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
import sys
import logging
from typing import Dict, Any, Optional
import aiohttp

# ============================================================================
# CONFIGURATION - Change this to your deployed server
# ============================================================================
SERVER_URL = "http://192.168.2.5:8080/mcp/"  # Remote server URL

# Setup logging
logging.basicConfig(
    level=logging.WARNING,  # Set to DEBUG for troubleshooting
    format='[%(asctime)s] %(levelname)s: %(message)s',
    stream=sys.stderr
)
logger = logging.getLogger(__name__)

class MCPRemoteProxy:
    """Proxy between stdio (Claude) and HTTP streamable transport (server)"""
    
    def __init__(self, server_url: str):
        self.server_url = server_url.rstrip('/')
        if not self.server_url.endswith('/'):
            self.server_url += '/'
        self.session: Optional[aiohttp.ClientSession] = None
        self.session_id: Optional[str] = None
        
    async def start(self):
        """Initialize the HTTP session"""
        self.session = aiohttp.ClientSession()
        logger.debug(f"Initialized session for {self.server_url}")
        
    async def stop(self):
        """Clean up resources"""
        if self.session:
            await self.session.close()
            
    async def send_request(self, request: Dict[str, Any]) -> None:
        """Send request to HTTP server and handle SSE response"""
        if not self.session:
            await self.start()
            
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json, text/event-stream'
        }
        
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
                    logger.debug(f"Got session ID: {self.session_id}")
                
                # Check content type
                content_type = response.headers.get('content-type', '')
                
                if response.status != 200:
                    error_text = await response.text()
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

async def test_connection():
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
    
    proxy = MCPRemoteProxy(SERVER_URL)
    try:
        await proxy.start()
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json, text/event-stream'
        }
        
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

async def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        if sys.argv[1] == '--test':
            success = await test_connection()
            sys.exit(0 if success else 1)
        elif sys.argv[1] == '--help':
            print(__doc__, file=sys.stderr)
            sys.exit(0)
    
    # Check if running interactively
    if sys.stdin.isatty():
        print("Apple Documentation MCP Remote Client", file=sys.stderr)
        print(f"Server: {SERVER_URL}", file=sys.stderr)
        print("", file=sys.stderr)
        print("This should be run by Claude, not directly.", file=sys.stderr)
        print("Run with --test to test connection", file=sys.stderr)
        print("Run with --help for setup instructions", file=sys.stderr)
        sys.exit(1)
    
    # Run the proxy
    proxy = MCPRemoteProxy(SERVER_URL)
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