# Apple Developer Documentation MCP Server

A comprehensive MCP (Model Context Protocol) server providing AI-powered search across Apple's complete developer documentation ecosystem - 341+ frameworks with 340,000+ pages.

## Features

- **Complete Coverage**: All 341 Apple frameworks automatically discovered and indexed
- **Vector Search**: OpenAI embeddings with ChromaDB for semantic documentation search
- **Platform Filtering**: Search by iOS, macOS, tvOS, watchOS, visionOS, or all platforms
- **MCP Integration**: Works with Claude Code, Claude Desktop, and other MCP clients
- **Dual Deployment**: Both local and remote server options
- **Sub-500ms Search**: Optimized for fast responses with metadata filtering

## Quick Start

### Client Setup (Choose One)

#### Option 1: Local Client (Runs server on your machine)
1. **Download**: `curl -O https://raw.githubusercontent.com/averyy/apple-developer-docs/main/apple_docs_client.py`
2. **Setup server**: Clone this repo and run `cd mcp-server && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
3. **Add to Claude config**:
   ```json
   {
     "mcpServers": {
       "apple-docs": {
         "type": "stdio",
         "command": "python3",
         "args": ["/path/to/apple_docs_client.py"]
       }
     }
   }
   ```

#### Option 2: Remote Client (Connects to deployed server)
1. **Download**: `curl -O https://raw.githubusercontent.com/averyy/apple-developer-docs/main/apple_docs_remote_client.py`
2. **Configure server URL**: Set `MCP_SERVER_URL` environment variable or edit the default
3. **Add to Claude config**:
   ```json
   {
     "mcpServers": {
       "apple-docs": {
         "type": "stdio", 
         "command": "python3",
         "args": ["/path/to/apple_docs_remote_client.py"]
       }
     }
   }
   ```

### Server Deployment

#### Docker Deployment (Recommended)
```bash
git clone https://github.com/averyy/apple-developer-docs.git
cd apple-developer-docs

# Configure environment
cp .env.example .env
# Edit .env with your OPENAI_API_KEY

# Deploy with Docker
cd mcp-server/deploy
./quick-start.sh
```

#### Local Development
```bash
# Clone and setup
git clone https://github.com/averyy/apple-developer-docs.git
cd apple-developer-docs/mcp-server

# Install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure environment
cp ../.env.example ../.env
# Edit .env to add your OPENAI_API_KEY

# Build vector index (one-time, ~4-6 hours)
python scripts/build_index.py --force

# Run server
python server/mcp_server.py
```

The server starts on port 8080 with:
- Platform-aware search across all Apple platforms
- 341+ frameworks with complete API documentation
- Vector similarity search with metadata filtering
- Health monitoring at `/health` endpoint

## Architecture

**Two Client Options:**
- **Local Client**: Downloads and runs the MCP server on your machine
- **Remote Client**: Connects to a deployed server via HTTP proxy

**Server Components:**
- **Scraping**: Uses Apple's internal JSON API (no HTML parsing)
- **Vector Search**: OpenAI text-embedding-3-small + ChromaDB
- **MCP Server**: FastMCP framework with streamable HTTP transport
- **Platform Filtering**: Metadata-based iOS/macOS/tvOS/watchOS/visionOS filtering

## Configuration Files

### Claude Desktop Config Locations:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux**: `~/.config/Claude/claude_desktop_config.json`

### Claude Code Config:
Usually stored in your project's `.claude/mcp_servers.json` or global config.

## Available Tools

When connected, the MCP server provides:

- **`search_apple_docs`**: Search documentation with platform and framework filtering
  - `query`: Search terms (e.g., "SwiftUI Button", "async await")
  - `framework`: Optional framework filter (e.g., "SwiftUI", "UIKit")
  - `platform`: Platform filter - ios, macos, tvos, watchos, visionos, catalyst, or "all"
  - `limit`: Number of results (1-20, default: 5)

- **`list_frameworks`**: List all available Apple frameworks
  - `platform`: Optional platform filter

## Project Structure

```
apple-developer-docs/
├── apple_docs_client.py          # Local client (all-in-one)
├── apple_docs_remote_client.py   # Remote client (HTTP proxy)
├── documentation/                # Scraped Apple docs (340K+ files)
├── mcp-server/                   # Server implementation
│   ├── server/mcp_server.py      # Main MCP HTTP server
│   ├── server/rag.py             # Vector search engine
│   ├── scripts/build_index.py    # Vector index builder
│   └── vectorstore/              # ChromaDB embeddings (~1.9GB)
├── scraper/                      # Apple JSON API scraper
└── docs/                         # Documentation
```

## Performance

- **Search Speed**: <500ms with platform filtering
- **Index Size**: ~1.9GB ChromaDB for 340K+ documents
- **Memory Usage**: ~2GB RAM for full index
- **Update Cost**: ~$4 initial indexing, <$0.10 for incremental updates

## Environment Variables

Create a `.env` file with:
```bash
# Required
OPENAI_API_KEY=sk-proj-xxxxx

# Optional
MCP_PORT=8080
VECTORSTORE_PATH=./vectorstore
MCP_SERVER_URL=http://192.168.2.5:8080/mcp/  # For remote server tests/clients
```

## Health Check

Test your deployment:
```bash
# Local server
curl http://localhost:8080/health

# Remote client test
python3 apple_docs_remote_client.py --test
```

## Troubleshooting

**Connection Issues**:
- Ensure server is running on correct port (8080)
- Check firewall settings for remote connections
- Verify Claude config file syntax

**Search Issues**:
- Platform parameter is required (use "all" if unsure)
- Check that vectorstore is properly built
- Ensure OpenAI API key is valid

**Performance Issues**:
- Allocate at least 2GB RAM for full index
- Use SSD storage for better search performance
- Consider platform filtering to reduce search scope

## Development

To modify or extend the server:

```bash
# Run tests
cd mcp-server
python tests/test_mcp_server.py

# Rebuild index
python scripts/build_index.py --force

# Check logs
tail -f server/server.log
```

## License

**Code**: MIT License
**Documentation Content**: © Apple Inc. - This tool provides offline access to publicly available documentation for development use.

---

For detailed technical information, see the [docs/](docs/) directory.