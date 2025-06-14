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

### 1. Ensure Vectorstore is Built with Metadata

If you haven't rebuilt the vectorstore with platform metadata:
```bash
cd mcp-server
python scripts/build_index.py --force
```

### 2. Running the Server

```bash
cd mcp-server
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

**Note**: Platform filtering is required to ensure relevant results. Use "all" to search across all platforms.

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
python tests/test_mcp_server.py
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
- Ensure platform parameter is set correctly (use "all" if unsure)

### Framework Mismatch
- Some frameworks may have no documents
- Sub-frameworks may be grouped under parent
- Check `/documentation/` folder for exact names

## Performance

- **Search Speed**: <500ms average with platform filtering
- **Memory Usage**: ~200MB server process
- **Vectorstore**: 3.2GB ChromaDB with platform metadata
- **Frameworks**: 341 indexed with platform availability
- **Documents**: 323,096 total with enhanced metadata

## Security

- API key required for all MCP endpoints
- Environment-based configuration
- Ready for HTTPS via reverse proxy
- No hardcoded credentials

## RAG Engine Details

The MCP server uses a sophisticated RAG (Retrieval-Augmented Generation) engine for fast, accurate search across Apple documentation.

### RAG Architecture

1. **Vector Store**: ChromaDB with OpenAI text-embedding-3-small embeddings
2. **Query Processing**: Optional query expansion for better results
3. **Search**: Similarity search with optional framework filtering
4. **Results**: Raw documentation returned for Claude to process

### RAG Performance

- **Total documents**: 323,096
- **Average search time**: ~350ms
- **Query cost**: $0.000002 per query (OpenAI embeddings only)
- **No GPT-4 needed**: Claude handles all reasoning

### Using the RAG Engine Directly

```python
# When using from within the MCP server
from rag import SimpleRAG

# Initialize
rag = SimpleRAG()

# Search across all documentation
results = await rag.search("SwiftUI Button", limit=5)

# Search within a specific framework
results = await rag.search("NavigationView", framework="SwiftUI", limit=3)

# Find exact API documentation
api_doc = await rag.get_api_doc("text", "SwiftUI")
if api_doc:
    print(api_doc['content'])

# Multi-query search with deduplication
results = await rag.multi_search([
    "SwiftUI List",
    "ForEach SwiftUI",
    "ScrollView"
], limit_per_query=3)
```

### Cost Analysis

- Query embedding: $0.000002 per query
- No LLM generation costs
- 10,000 queries/month = $0.02
- 7,500x cheaper than GPT-4 approach

## Future Enhancements

1. **Caching**: Redis for frequent queries
2. **Analytics**: Track popular searches
3. **ML Expansion**: Embedding-based related terms
4. **Monitoring**: Prometheus metrics