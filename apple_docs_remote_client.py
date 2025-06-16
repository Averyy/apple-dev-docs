#!/usr/bin/env python3
"""
Apple Documentation MCP Remote Client
=====================================

Connects to a remote Apple Documentation MCP server.

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

This file is self-contained - no other dependencies needed locally!

Repository: https://github.com/averyy/apple-developer-docs
"""

import asyncio
import json
import sys
from typing import Dict, Any

# ============================================================================
# CONFIGURATION - Change this to your deployed server
# ============================================================================
SERVER_URL = "http://192.168.2.5:8080/mcp/"  # Remote server IP

# ============================================================================
# HTTP Client (using only stdlib)
# ============================================================================

import urllib.request
import urllib.parse
import urllib.error

class MCPRemoteClient:
    def __init__(self, server_url: str):
        self.server_url = server_url.rstrip('/')
        
    def forward_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Forward MCP request to remote HTTP server"""
        try:
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'User-Agent': 'Apple-Docs-MCP-Remote-Client/1.0'
            }
            
            data = json.dumps(request).encode('utf-8')
            
            # Ensure URL ends with trailing slash
            url = self.server_url
            if not url.endswith('/'):
                url += '/'
            
            req = urllib.request.Request(url, data=data, headers=headers, method='POST')
            
            # Handle redirects manually
            try:
                with urllib.request.urlopen(req, timeout=30) as response:
                    response_data = response.read().decode('utf-8')
                    return json.loads(response_data)
            except urllib.error.HTTPError as e:
                if e.code in [301, 302, 307, 308]:
                    # Follow redirect
                    new_url = e.headers.get('Location')
                    if new_url:
                        req = urllib.request.Request(new_url, data=data, headers=headers, method='POST')
                        with urllib.request.urlopen(req, timeout=30) as response:
                            response_data = response.read().decode('utf-8')
                            return json.loads(response_data)
                raise e
                
        except urllib.error.HTTPError as e:
            error_msg = f"HTTP {e.code}: {e.reason}"
            if e.code == 404:
                error_msg += " - Check that SERVER_URL is correct and server is running"
            elif e.code == 406:
                error_msg += " - Server protocol mismatch"
            elif e.code >= 500:
                error_msg += " - Server error"
        except urllib.error.URLError as e:
            error_msg = f"Connection failed: {e.reason}"
        except Exception as e:
            error_msg = f"Unexpected error: {e}"
            
        return {
            "jsonrpc": "2.0",
            "id": request.get("id"),
            "error": {
                "code": -32603,
                "message": f"Remote server error: {error_msg}"
            }
        }
    
    async def run(self):
        """Main proxy loop - stdio to HTTP"""
        while True:
            try:
                # Read from stdin
                line = await asyncio.get_event_loop().run_in_executor(
                    None, sys.stdin.readline
                )
                
                if not line:
                    break
                    
                line = line.strip()
                if not line:
                    continue
                
                # Parse JSON-RPC request
                request = json.loads(line)
                
                # Forward to remote server
                response = self.forward_request(request)
                
                # Send response to stdout
                print(json.dumps(response, separators=(',', ':')))
                sys.stdout.flush()
                
            except json.JSONDecodeError as e:
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
                
            except Exception as e:
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

def test_connection():
    """Test connection to remote server"""
    print(f"Testing connection to: {SERVER_URL}")
    
    client = MCPRemoteClient(SERVER_URL)
    
    test_request = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {"tools": {}}
        }
    }
    
    print("Sending test request...")
    response = client.forward_request(test_request)
    
    if "error" in response:
        print(f"❌ Connection failed: {response['error']['message']}")
        return False
    else:
        print("✅ Connection successful!")
        return True

async def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == '--test':
            test_connection()
            return
        elif sys.argv[1] == '--help':
            print(__doc__)
            return
    
    if sys.stdin.isatty():
        print("Apple Documentation MCP Remote Client")
        print(f"Current server: {SERVER_URL}")
        print("Run with --test to test connection")
        print("Run with --help for setup instructions")
        return
    
    # Run the remote client
    client = MCPRemoteClient(SERVER_URL)
    await client.run()

if __name__ == "__main__":
    asyncio.run(main())