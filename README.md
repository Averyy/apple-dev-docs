# Apple Developer Documentation Scraper & MCP Server

A comprehensive Python tool that scrapes Apple's entire developer documentation ecosystem (341 frameworks, 278K+ pages) and provides an MCP server for AI-powered documentation search with platform-aware filtering.

## Features

- **Complete Coverage**: All 341 Apple frameworks automatically discovered and scraped
- **Fast Scraping**: Uses Apple's internal JSON API (no HTML parsing needed)
- **Vector Search**: OpenAI embeddings with ChromaDB for semantic search
- **Platform Filtering**: Search by iOS, macOS, tvOS, watchOS, visionOS, or all platforms
- **MCP Integration**: Model Context Protocol server for AI assistants like Claude
- **Incremental Updates**: ETag-based efficient updates for changed content only
- **Cost Optimized**: ~$4 initial setup, <$0.10 for typical updates

## Quick Start

### Option 1: Docker Deployment (Recommended)

```bash
# Clone and setup
git clone <repo-url>
cd apple-developer-docs

# Configure environment
cp .env.example .env
# Edit .env with:
# - OPENAI_API_KEY=sk-proj-xxxxx
# - MCP_API_KEY=$(openssl rand -hex 32)

# Deploy with Docker
cd mcp-server/deploy
./quick-start.sh
```

Docker automatically handles:
- Building vectorstore on first run (~4-6 hours)
- Weekly updates (Sundays 1 AM)
- Health monitoring and auto-restart
- Process management with supervisor

#### Docker Commands

```bash
# Check status
docker logs -f apple-docs-mcp
docker exec apple-docs-mcp supervisorctl status

# Manual update
docker exec apple-docs-mcp python /app/scraper/auto_scrape_and_embed.py --embed --yes

# Test search
curl -H "Authorization: Bearer $MCP_API_KEY" http://localhost:8080/health
```

### Option 2: Local Development

```bash
# Clone and setup
git clone <repo-url>
cd apple-developer-docs

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env to add your keys

# Build Vector Index (one-time)
cd mcp-server
python scripts/build_index.py --force

# Run MCP Server
make server
```

The server starts on port 8080 with:
- Platform-aware search (iOS, macOS, tvOS, watchOS, visionOS)
- Framework discovery (341 frameworks)
- Sub-500ms response times
- Bearer token authentication

### 4. Configure AI Assistant

For Claude Desktop, edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "apple-docs": {
      "type": "sse", 
      "url": "http://localhost:8080/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_MCP_API_KEY"
      }
    }
  }
}
```

Replace `YOUR_MCP_API_KEY` with the value from your `.env` file.

## Architecture

**Scraping**: Uses Apple's internal JSON API endpoints (no HTML parsing needed)
```
https://developer.apple.com/tutorials/data/documentation/{framework}/{page}.json
```

**Vector Search**: OpenAI text-embedding-3-small (1536 dimensions) + ChromaDB  
**Platform Filtering**: Metadata extraction enables iOS/macOS/etc. specific search  
**Incremental Updates**: ETag-based change detection for efficient updates
**Docker Deployment**: Multi-process container with supervisor for reliability

## Key Commands

```bash
# Docker deployment
cd mcp-server/deploy && ./quick-start.sh

# Health check
curl -H "Authorization: Bearer $MCP_API_KEY" http://localhost:8080/health

# Update index (local)
cd mcp-server && python scripts/build_index.py

# Run tests
cd mcp-server && python tests/test_mcp_server.py

# View logs (Docker)
docker logs -f apple-docs-mcp
```

## Project Structure

```
apple-developer-docs/
├── documentation/           # Scraped Apple docs (278K+ files, 1.17GB)
├── mcp-server/             # MCP server and vector indexing
│   ├── scripts/build_index.py  # Main indexing script
│   ├── server/mcp_server.py    # MCP HTTP server
│   └── vectorstore/            # ChromaDB embeddings (~1.9GB)
├── scraper/                # Scraping engine for Apple's JSON API
└── docs/                   # Detailed documentation
```

## Documentation

### Core Guides
- **[Docker Deployment Guide](docs/DOCKER_DEPLOYMENT.md)** - Complete deployment instructions
- **[MCP Server Guide](docs/MCP_SERVER_GUIDE.md)** - MCP server setup and API reference
- **[Indexing Guide](docs/INDEXING_GUIDE.md)** - Vector index building and maintenance
- **[Project Status](docs/PROJECT_STATUS.md)** - Current system status and metrics
- **[Deployment Checklist](docs/DEPLOYMENT_CHECKLIST.md)** - Pre-deployment verification

### API Tools Available in MCP
- `search_apple_docs` - Search with platform filtering (required parameter)
- `list_frameworks` - Discover all 341 Apple frameworks

## Performance

- **Search Speed**: <500ms with platform filtering
- **Index Size**: ~1.9GB ChromaDB for 323K+ documents  
- **Update Cost**: ~$4 initial, <$0.10 for incremental updates
- **Platform Coverage**: iOS, macOS, tvOS, watchOS, visionOS, Catalyst

## Troubleshooting

**Environment Issues**: Ensure `OPENAI_API_KEY` is set in `.env`  
**Build Errors**: Try `cd mcp-server && python scripts/build_index.py --force`  
**Server Issues**: Check `curl http://localhost:8080/health`  
**Search Problems**: Ensure platform parameter is set (use "all" if unsure)

## License & Legal

**Code**: MIT License  
**Documentation Content**: © Apple Inc. - This tool provides offline access to publicly available documentation for personal development use.

---

For detailed technical information, see the [docs/](docs/) directory.