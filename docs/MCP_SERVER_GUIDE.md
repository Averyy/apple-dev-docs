# Apple Docs MCP Server - Complete Guide

## Overview

The MCP (Model Context Protocol) server provides high-performance search across 323,096 Apple Developer Documentation pages via an HTTP API with sub-500ms response times, now with platform-aware filtering and framework discovery.

## Architecture

- **Server**: FastAPI-based HTTP server with Streamable HTTP transport
- **Protocol**: MCP Streamable HTTP (2025-03-26 spec) with JSON-RPC 2.0
- **Search Engine**: ChromaDB vector store with OpenAI embeddings
- **Authentication**: Bearer token via `MCP_API_KEY` environment variable
- **Documents**: 341,207 pages across 341 Apple frameworks
- **Enhanced Features**:
  - Platform filtering (iOS, macOS, tvOS, watchOS, visionOS)
  - Framework discovery with summaries
  - Metadata extraction for intelligent search
  - MCP Streamable HTTP implementation (latest spec)
  - Resources and Prompts support
  - Session management

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

#### For Claude (if using a version that supports SSE):
```bash
claude mcp add --transport sse apple-docs http://localhost:8080/mcp \
  -e AUTHORIZATION="Bearer YOUR_MCP_API_KEY"
```

This generates the following configuration:
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

For remote access, use your server's IP:
```bash
claude mcp add --transport sse apple-docs http://192.168.2.5:8080/mcp \
  -e AUTHORIZATION="Bearer YOUR_MCP_API_KEY"
```

## API Reference

### Endpoints

#### Streamable HTTP Endpoints
- `POST /mcp` - Main MCP endpoint (JSON-RPC 2.0)
  - Handles all MCP methods: initialize, tools/*, resources/*, prompts/*
  - Returns JSON or SSE based on Accept header
  - Session management via x-session-id header
  - Requires Bearer token authentication

- `GET /mcp` - Optional SSE stream for server-initiated messages
  - Provides persistent connection for notifications
  - Session-aware via x-session-id header
  - Requires Bearer token authentication
  
#### Health Check
- `GET /health` - Server and vectorstore status (no auth required)

#### MCP Methods Available
- `initialize` - Establish connection and capabilities
- `tools/list` - List search_apple_docs and list_frameworks tools
- `tools/call` - Execute documentation searches
- `resources/list` - Browse documentation structure
- `resources/read` - Read specific documentation pages
- `prompts/list` - Get available prompt templates
- `prompts/get` - Get filled prompt for specific use case

### Tool: search_apple_docs

**Parameters:**
- `query` (required): Search terms
- `framework` (optional): Filter by framework (e.g., "SwiftUI", "UIKit")
- `platform` (optional, default: "all"): Platform filter ("ios", "macos", "tvos", "watchos", "visionos", "catalyst", "all")
- `limit` (optional): Results count (1-20, default: 5)
- `include_full_content` (optional): Return full documents (default: false)

**JSON-RPC Example:**
```bash
curl -X POST http://localhost:8080/mcp \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": "search-1",
    "method": "tools/call",
    "params": {
      "name": "search_apple_docs",
      "arguments": {
        "query": "SwiftUI Button",
        "platform": "ios",
        "limit": 5
      }
    }
  }'
```

### Tool: list_frameworks

**Parameters:**
- `platform` (optional): Filter by platform ("ios", "macos", "tvos", "watchos", "visionos", "catalyst", "all")

**Returns:** 
- Without platform filter: All 341 frameworks with platform availability
- With platform filter: Platform-specific frameworks with full descriptions

**JSON-RPC Example:**
```bash
curl -X POST http://localhost:8080/mcp \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": "list-1",
    "method": "tools/call",
    "params": {
      "name": "list_frameworks",
      "arguments": {
        "platform": "ios"
      }
    }
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

### Run the comprehensive test suite:

```bash
cd mcp-server
python tests/test_mcp_server.py
```

Tests include:
- Health check validation
- Authentication testing
- Search functionality (basic, filtered, full content)
- Error handling and edge cases

### MCP SSE Protocol Testing

For Claude Code compatibility testing:

```bash
cd mcp-server
python tests/test_mcp_sse_protocol.py
```

This validates:
- ✅ SSE connection and initial event format
- ✅ JSON-RPC 2.0 compliance
- ✅ Heartbeat events (30-second interval)
- ✅ Tool discovery and execution
- ✅ Authentication requirements
- ✅ Error handling standards

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

### Claude Code Specific Issues

#### "Dynamic client registration failed: HTTP 404"
- This means the SSE endpoint is not available
- Ensure you've deployed the latest server code with SSE support
- Test with: `curl -N -H "Authorization: Bearer YOUR_KEY" http://server:8080/mcp`

#### Connection timeouts
- Check that heartbeat events are being sent every 30 seconds
- Verify no proxy/firewall is blocking SSE connections
- Ensure server has sufficient resources

#### No tools available
- Verify the initial connection event includes capabilities
- Check that tools/list method returns properly formatted tools
- Review server logs for initialization errors

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

- **Total documents**: 341,207
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

## Resources Support

The server provides browsable documentation through MCP resources:

### resources/list
Returns available documentation pages with URI templates:
- `docs://{framework}/{page}` - Browse specific framework docs
- Lists up to 100 resources at a time
- Includes resource templates for pattern-based access

### resources/read
Read specific documentation pages:
```bash
# Example: Read SwiftUI Button documentation
{
  "method": "resources/read",
  "params": {
    "uri": "docs://SwiftUI/Button"
  }
}
```

## Prompts Support

Pre-built prompt templates for common documentation tasks:

### Available Prompts
1. **explain_api** - Comprehensive API explanation
2. **compare_apis** - Compare two similar APIs
3. **migration_guide** - Framework migration assistance
4. **platform_availability** - Check platform support
5. **code_example** - Find code examples

### Example Usage
```bash
{
  "method": "prompts/get",
  "params": {
    "name": "migration_guide",
    "arguments": {
      "from_framework": "UIKit",
      "to_framework": "SwiftUI",
      "component": "Button"
    }
  }
}
```

## Protocol Compliance

The server implements MCP Streamable HTTP transport (2025-03-26 spec):

### Streamable HTTP Transport
- Single `/mcp` endpoint for all operations
- JSON or SSE responses based on Accept header
- Session management via x-session-id headers
- Initialize/initialized handshake flow

### JSON-RPC 2.0
- All messages use JSON-RPC 2.0 format
- Batch request support
- Request ID correlation maintained
- Standard error codes (-32601, -32603, etc.)

### Authentication
- Bearer token authentication required
- Token validated on all endpoints
- 401 responses for invalid/missing auth

### Full MCP Feature Support
- **Tools**: search_apple_docs, list_frameworks
- **Resources**: Browse and read documentation structure
- **Prompts**: Pre-built templates for common tasks
- **Sessions**: Stateful connection management

## Future Enhancements

1. **Binary Results**: Support for image/diagram extraction
2. **OAuth Support**: Dynamic client registration for enterprise
3. **Caching**: Redis for frequent queries
4. **Analytics**: Track popular searches
5. **Monitoring**: Prometheus metrics
6. **Streaming**: Real-time documentation updates