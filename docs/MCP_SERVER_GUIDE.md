# Apple Docs MCP Server - Complete Guide

## Overview

The MCP (Model Context Protocol) server provides high-performance search across 323,096 Apple Developer Documentation pages via an HTTP API with sub-500ms response times, now with platform-aware filtering and framework discovery.

## Architecture

- **Server**: FastAPI-based HTTP server (`/mcp-server/server/mcp_server.py`)
- **Search Engine**: ChromaDB vector store with OpenAI embeddings
- **Authentication**: Bearer token via `MCP_API_KEY` environment variable
- **Documents**: 323,096 pages across 341 Apple frameworks
- **Enhanced Features**:
  - Platform filtering (iOS, macOS, tvOS, watchOS, visionOS)
  - Framework discovery with summaries
  - Metadata extraction for intelligent search

## Quick Start

### 1. Running the Server

```bash
cd mcp-server
source venv/bin/activate
make server

# Or directly:
python server/mcp_server.py
```

### 2. Client Configuration

For Claude Desktop on macOS, edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

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

For remote access, change `localhost` to your server's IP address.

## API Reference

### Endpoints

- `GET /health` - Health check (no auth required)
- `GET /mcp/tools/list` - List available tools
- `POST /mcp/tools/call` - Execute tool calls

### Tool: search_apple_docs

**Parameters:**
- `query` (required): Search terms
- `framework` (optional): Filter by framework (e.g., "SwiftUI", "UIKit")
- `platform` (required, default: "all"): Platform filter ("ios", "macos", "tvos", "watchos", "visionos", "catalyst", "all")
- `limit` (optional): Results count (1-20, default: 5)
- `include_full_content` (optional): Return full documents (default: false)

**Example Request:**
```bash
curl -X POST http://localhost:8080/mcp/tools/call \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "search_apple_docs",
    "arguments": {
      "query": "SwiftUI Button",
      "platform": "ios",
      "limit": 5
    }
  }'
```

### Tool: list_frameworks

**Parameters:** None

**Returns:** List of all available frameworks with:
- Total framework count
- Frameworks grouped by platform
- Popular frameworks with summaries
- Alphabetical grouping

**Example Request:**
```bash
curl -X POST http://localhost:8080/mcp/tools/call \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "list_frameworks",
    "arguments": {}
  }'
```

## Enhanced Search Features

### Query Preprocessing
The server automatically handles LLM-style queries by removing common prefixes:
- "how to", "what is", "show me" → cleaned query
- Question marks and filler words → removed

### Query Expansion
Queries are expanded with semantic variations:
- "button" → "Button ButtonStyle onTapGesture action tap click press"
- "async" → "async await Task concurrency AsyncSequence asynchronous"
- Common typos → corrected terms

### Dynamic Framework Discovery
- Automatically loads 341 framework names from vectorstore
- Extracts platform availability for each framework
- Provides framework summaries from overview sections
- Groups frameworks by platform for easy filtering

## Testing

Run the comprehensive test suite:

```bash
cd mcp-server
./venv/bin/python tests/test_mcp_server.py
```

Tests include:
- Health check validation
- Authentication testing
- Search functionality (basic, filtered, full content)
- Error handling and edge cases

## Troubleshooting

### Connection Refused
- Ensure server is running: `make server`
- Check port 8080 is available
- Verify firewall settings

### Authentication Failed
- Check API key matches `.env` file
- Include "Bearer " prefix in header

### No/Poor Results
- Try broader search terms
- Use framework filter for specific docs
- Check server logs for errors

### Framework Mismatch
- Some frameworks may have no documents
- Sub-frameworks may be grouped under parent
- Check `/documentation/` folder for exact names

## Performance

- **Search Speed**: <500ms average
- **Memory Usage**: ~200MB server process
- **Vectorstore**: 3.2GB ChromaDB
- **Frameworks**: ~361 indexed
- **Documents**: 323,096 total

## Security

- API key required for all MCP endpoints
- Environment-based configuration
- Ready for HTTPS via reverse proxy
- No hardcoded credentials

## Future Enhancements

1. **Caching**: Redis for frequent queries
2. **Analytics**: Track popular searches
3. **ML Expansion**: Embedding-based related terms
4. **Monitoring**: Prometheus metrics