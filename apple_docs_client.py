#!/usr/bin/env python3
"""
Apple Documentation MCP Client
=====================================

Simple wrapper that runs the local stdio server.

SETUP:
1. Download this file to your computer
2. Set the path to the server directory below
3. Add to Claude MCP config:

{
  "apple-docs": {
    "type": "stdio",
    "command": "python3",
    "args": ["/path/to/apple_docs_client_simple.py"]
  }
}

4. Make sure you have the vectorstore data in the expected location

Repository: https://github.com/averyy/apple-developer-docs
"""

import os
import sys
import subprocess
from pathlib import Path

# ============================================================================
# CONFIGURATION
# ============================================================================

# Auto-detect server location relative to this file
CLIENT_DIR = Path(__file__).parent
SERVER_SCRIPT = CLIENT_DIR / "mcp-server" / "server" / "mcp_server_stdio.py"
VENV_PYTHON = CLIENT_DIR / "mcp-server" / "venv" / "bin" / "python3"

# Fallback paths if auto-detection fails
FALLBACK_PATHS = [
    "/Users/avery/Code/apple-developer-docs/mcp-server/server/mcp_server_stdio.py",
    "~/Code/apple-developer-docs/mcp-server/server/mcp_server_stdio.py",
    "./mcp-server/server/mcp_server_stdio.py"
]

def find_server_script():
    """Find the server script"""
    # Try auto-detected path first
    if SERVER_SCRIPT.exists():
        return str(SERVER_SCRIPT)
    
    # Try fallback paths
    for path_str in FALLBACK_PATHS:
        path = Path(path_str).expanduser()
        if path.exists():
            return str(path)
    
    return None

def find_python():
    """Find the right Python executable"""
    # Try venv python first
    if VENV_PYTHON.exists():
        return str(VENV_PYTHON)
    
    # Try system python
    return sys.executable

def print_help():
    """Print setup help"""
    server_path = find_server_script()
    python_path = find_python()
    
    print(f"""
Apple Documentation MCP Client
==============================

Auto-detected configuration:
  Server script: {server_path or "NOT FOUND"}
  Python path: {python_path}

SETUP STEPS:
1. Download the full repository:
   git clone https://github.com/averyy/apple-developer-docs.git

2. Set up the server (one-time):
   cd apple-developer-docs/mcp-server
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

3. Add to Claude MCP config:
   {{
     "apple-docs": {{
       "type": "stdio",
       "command": "python3",
       "args": ["{Path(__file__).absolute()}"]
     }}
   }}

4. Restart Claude

TESTING:
  python3 {Path(__file__).name} --test

ERROR TROUBLESHOOTING:
If auto-detection fails, edit this file and set the correct paths manually.
""", file=sys.stderr)

def test_setup():
    """Test if everything is set up correctly"""
    print("Testing Apple Docs MCP setup...", file=sys.stderr)
    
    server_path = find_server_script()
    if not server_path:
        print("❌ Server script not found", file=sys.stderr)
        print("Please download the full repository or edit paths in this file", file=sys.stderr)
        return False
    
    python_path = find_python()
    print(f"✅ Found server: {server_path}", file=sys.stderr)
    print(f"✅ Found Python: {python_path}", file=sys.stderr)
    
    # Test that we can import required modules
    try:
        result = subprocess.run([
            python_path, "-c", 
            "import os; "
            "from mcp.server.fastmcp import FastMCP; "
            "print('Dependencies OK')"
        ], capture_output=True, text=True, cwd=Path(server_path).parent)
        
        if result.returncode == 0:
            print("✅ Dependencies installed", file=sys.stderr)
        else:
            print(f"❌ Dependency error: {result.stderr}", file=sys.stderr)
            return False
    except Exception as e:
        print(f"❌ Failed to test dependencies: {e}", file=sys.stderr)
        return False
    
    print("✅ Setup looks good!", file=sys.stderr)
    return True

def main():
    """Main entry point"""
    if len(sys.argv) > 1:
        if sys.argv[1] in ['--help', '-h']:
            print_help()
            return
        elif sys.argv[1] == '--test':
            test_setup()
            return
    
    # Check if running interactively
    if sys.stdin.isatty():
        print_help()
        return
    
    # Find server script
    server_path = find_server_script()
    if not server_path:
        print(json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {
                "code": -32603,
                "message": "Server script not found. Run with --help for setup instructions."
            }
        }))
        return
    
    # Find python
    python_path = find_python()
    
    # Execute the server script directly
    try:
        os.execv(python_path, [python_path, server_path])
    except Exception as e:
        print(json.dumps({
            "jsonrpc": "2.0", 
            "id": None,
            "error": {
                "code": -32603,
                "message": f"Failed to start server: {e}"
            }
        }))

if __name__ == "__main__":
    main()