#!/usr/bin/env python3
"""
Apple Documentation MCP Client (Local)
=====================================

This runs the remote client but pointed at localhost.

SETUP:
1. Start the local server: cd mcp-server && make server
2. Add this to your Claude MCP config:

{
  "apple-docs": {
    "type": "stdio",
    "command": "python3",
    "args": ["/path/to/apple_docs_client.py"]
  }
}

3. Restart Claude

Repository: https://github.com/averyy/apple-developer-docs
"""

import os
import sys
import subprocess
from pathlib import Path

# Configuration
LOCAL_SERVER_URL = "http://localhost:8080/mcp/"

# Path to the remote client
CLIENT_DIR = Path(__file__).parent
REMOTE_CLIENT = CLIENT_DIR / "apple_docs_remote_client.py"

def main():
    """Run the remote client with localhost URL"""
    
    # Set environment variable to override the server URL
    env = os.environ.copy()
    env['MCP_SERVER_URL'] = LOCAL_SERVER_URL
    
    # Check if running interactively
    if sys.stdin.isatty():
        print("Apple Documentation MCP Client (Local)")
        print("=====================================")
        print(f"Server URL: {LOCAL_SERVER_URL}")
        print("")
        print("This should be run by Claude, not directly.")
        print("")
        print("To start the local server:")
        print("  cd mcp-server && make server")
        print("")
        print("To test the connection:")
        print("  python3 apple_docs_local_client.py --test")
        
        if len(sys.argv) > 1 and sys.argv[1] == '--test':
            # Test connection
            print("\nTesting connection to localhost...")
            print("(Make sure the server is running: cd mcp-server && make server)")
            result = subprocess.run(
                [sys.executable, str(REMOTE_CLIENT), '--test'],
                env=env,
                capture_output=True,
                text=True
            )
            print(result.stdout)
            if result.stderr:
                print(result.stderr, file=sys.stderr)
            return result.returncode
        
        return 1
    
    # Run the remote client with modified environment
    os.execve(sys.executable, [sys.executable, str(REMOTE_CLIENT)], env)

if __name__ == "__main__":
    sys.exit(main())