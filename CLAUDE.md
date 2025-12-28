# Claude Guidelines

## Git Commit Rules

**NEVER commit without explicit written permission** - Only commit when the user explicitly asks with phrases like "commit this", "push these changes", or "git commit". Never assume permission to commit.

**NEVER add Claude attribution to commits** - Do not include "Co-Authored-By: Claude" or any other attribution. Keep commits simple with just the message.

## Deployment Testing

**Public server:** https://xdocs.dev/mcp

```bash
# Test health endpoint
curl https://xdocs.dev/health

# Test MCP endpoint
curl -X POST https://xdocs.dev/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"initialize","params":{},"id":1}'
```

**Server details:**
- URL: `https://xdocs.dev/mcp`
- Transport: Streamable HTTP (native MCP)
- Rate Limit: 30 req/min per IP (bypassed with API key)

## Project Overview

MCP server for Apple Developer Documentation with Meilisearch backend. 370+ frameworks, 334K+ documents, sub-3ms search.

## Critical Rules

- **NEVER create mock data** unless explicitly told to
- **NEVER replace existing code with simplified versions** - fix the actual problem
- **ALWAYS find root cause** - don't create workarounds
- **NEVER SUGGEST SPECIAL HANDLING FOR SPECIFIC PATTERNS** - 370+ frameworks means no special cases
- Update existing files, don't create new ones unless necessary
- Use relative paths in scripts
- Follow MCP spec from https://modelcontextprotocol.io/specification/

## Python Standards

- Python 3.11+ with type hints
- PEP 8 style
- asyncio for concurrent operations
- Proper logging (not print)
- Run mypy before considering complete

## Security

- API keys in environment variables only
- Never hardcode keys
- Use `.env` file (gitignored) for local dev

## Architecture

- **Scraper**: Uses Apple's JSON API (not HTML)
- **Search**: Meilisearch (<3ms latency)
- **MCP Server**: FastMCP with Streamable HTTP transport
- **Indexing**: ~4 minutes for 334K+ documents

## Core Commands

```bash
# Run scraper
python scrape.py --all --yes

# Index to Meilisearch
cd scripts && python index_to_meilisearch.py

# Run MCP server
cd mcp-server && python apple_docs_mcp.py

# Docker deployment
cd mcp-server && docker-compose up -d
```

## Project Structure

```
apple-dev-docs/
├── scrape.py                      # Documentation scraper
├── documentation/                 # Scraped markdown files
├── scripts/
│   └── index_to_meilisearch.py   # Indexer
├── mcp-server/
│   ├── apple_docs_mcp.py         # Native HTTP MCP server
│   ├── docker-compose.yml        # Docker deployment
│   └── Dockerfile
└── landing/
    └── index.html                # xdocs.dev landing page
```
