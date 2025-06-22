# Apple Docs MCP Server - Complete Guide

## Overview

The MCP (Model Context Protocol) server provides high-performance search across 341,207 Apple Developer Documentation pages via an HTTP API with sub-500ms response times, now with platform-aware filtering and framework discovery.

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

### 3. Client Configuration

#### For Claude (if using a version that supports SSE):
```bash
claude mcp add --transport sse apple-docs ${MCP_SERVER_URL:-http://localhost:8080}/mcp \
  -e AUTHORIZATION="Bearer YOUR_MCP_API_KEY"
```

This generates the following configuration:
```json
{
  "mcpServers": {
    "apple-docs": {
      "type": "sse",
      "url": "${MCP_SERVER_URL}/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_MCP_API_KEY"
      }
    }
  }
}
```

For remote access, set the MCP_SERVER_URL environment variable:
```bash
export MCP_SERVER_URL=http://192.168.2.5:8080
claude mcp add --transport sse apple-docs ${MCP_SERVER_URL}/mcp \
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
curl -X POST ${MCP_SERVER_URL:-http://localhost:8080}/mcp \
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
curl -X POST ${MCP_SERVER_URL:-http://localhost:8080}/mcp \
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
- Test with: `curl -N -H "Authorization: Bearer YOUR_KEY" ${MCP_SERVER_URL}/mcp`

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
- **Documents**: 341,207 total with enhanced metadata

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

---

# AI/LLM Developer Guide

## Self-Documenting Features

The MCP server provides built-in instructions through the protocol:

1. **Tools descriptions** - Each tool includes detailed descriptions and parameter documentation
2. **Prompts** - Pre-built templates including a `usage_guide` prompt
3. **Automatic discovery** - LLMs learn capabilities during the `initialize` handshake

### Getting Usage Instructions via MCP
```javascript
// Ask the server how to use it effectively
{
  "method": "prompts/get",
  "params": {
    "name": "usage_guide",
    "arguments": {
      "topic": "general"  // or: "search_tips", "platform_guide", "framework_discovery"
    }
  }
}
```

## Connection Details
- **Endpoint**: `${MCP_SERVER_URL}/mcp` (set MCP_SERVER_URL environment variable)
- **Protocol**: MCP Streamable HTTP (JSON-RPC 2.0)
- **Authentication**: Bearer token in Authorization header

## Core Capabilities

### 1. Search Documentation (`search_apple_docs`)
**Purpose**: Find relevant Apple documentation using natural language queries

**Parameters**:
- `query` (required): Natural language search query
- `platform` (required): Target platform - use "all" for cross-platform
  - Options: `ios`, `ipados`, `macos`, `tvos`, `watchos`, `visionos`, `catalyst`, `all`
- `framework` (optional): Filter by specific framework (e.g., "SwiftUI", "UIKit")
- `limit` (optional): Number of results (1-20, default: 5)
- `include_full_content` (optional): Return full documents vs summaries (default: false)

**Best Practices**:
- Use specific technical terms (e.g., "URLSession async await" not "how to make network calls")
- Include framework names when known (e.g., "SwiftUI List selection")
- Start with platform-specific searches, then broaden to "all" if needed

### 2. List Frameworks (`list_frameworks`)
**Purpose**: Discover available frameworks with descriptions

**Parameters**:
- `platform` (optional): Filter frameworks by platform
  - If omitted: Returns all 341 frameworks
  - If specified: Returns platform-specific frameworks with detailed descriptions

**When to Use**:
- User asks "what frameworks are available for [platform]?"
- Need to verify framework availability before searching
- Exploring capabilities of a specific platform

### 3. Browse Resources (`resources/list` and `resources/read`)
**Purpose**: Navigate documentation structure directly

**Usage**:
- `resources/list`: Get available documentation pages
- `resources/read`: Read specific documentation by URI
  - URI format: `docs://Framework/PageName`
  - Example: `docs://SwiftUI/Button`

### 4. Use Prompts (`prompts/list` and `prompts/get`)
**Purpose**: Pre-built templates for common documentation tasks

**Available Prompts**:
1. `explain_api` - Comprehensive API explanation
2. `compare_apis` - Compare similar APIs (e.g., UIButton vs SwiftUI Button)
3. `migration_guide` - Help migrate between frameworks
4. `platform_availability` - Check platform support
5. `code_example` - Find code examples

## Effective Search Strategies

### 1. Start Specific, Then Broaden
```javascript
// First attempt - specific platform
{
  "method": "tools/call",
  "params": {
    "name": "search_apple_docs",
    "arguments": {
      "query": "NavigationStack programmatic navigation",
      "platform": "ios",
      "framework": "SwiftUI"
    }
  }
}

// If no results, broaden search
{
  "arguments": {
    "query": "NavigationStack programmatic navigation",
    "platform": "all"  // Search across all platforms
  }
}
```

### 2. Use Framework Discovery First
When users mention a technology but you're unsure of the framework:
```javascript
// Step 1: Find the framework
{
  "method": "tools/call",
  "params": {
    "name": "list_frameworks",
    "arguments": {"platform": "ios"}
  }
}

// Step 2: Search within that framework
{
  "method": "tools/call",
  "params": {
    "name": "search_apple_docs",
    "arguments": {
      "query": "async image loading",
      "framework": "SwiftUI",  // Found from step 1
      "platform": "ios"
    }
  }
}
```

### 3. Leverage Prompts for Complex Queries
For migration or comparison questions:
```javascript
{
  "method": "prompts/get",
  "params": {
    "name": "migration_guide",
    "arguments": {
      "from_framework": "UIKit",
      "to_framework": "SwiftUI",
      "component": "TableView"
    }
  }
}
```

## Query Optimization Tips

### Do's ✅
- Use Apple's exact terminology (e.g., "URLSession" not "URL Session")
- Include method/property names when known (e.g., "navigationDestination modifier")
- Specify version-specific features (e.g., "iOS 17 Observable macro")
- Combine related terms (e.g., "CoreData CloudKit sync")

### Don'ts ❌
- Avoid conversational queries (e.g., "how do I..." - just use the technical terms)
- Don't include code syntax in queries (search for concepts, not code)
- Avoid generic terms without context (e.g., just "button" - specify framework)

## Common Use Cases

### 1. Building a New Feature
```
User: "I need to add a share sheet to my SwiftUI app"
→ Search: "ShareLink SwiftUI" with platform="ios"
```

### 2. Debugging an Issue
```
User: "My NavigationStack isn't updating when I change the path"
→ Search: "NavigationStack path binding update" with framework="SwiftUI"
```

### 3. Understanding Best Practices
```
User: "What's the proper way to handle background tasks in iOS?"
→ Search: "BGTaskScheduler background processing" with platform="ios"
```

### 4. Platform Compatibility
```
User: "Does Vision Pro support ARKit?"
→ Search: "ARKit" with platform="visionos"
```

## Response Handling

### Search Results Include:
- **API Name**: The specific API or component
- **Framework**: Which framework it belongs to
- **Platforms**: Supported platforms (iOS, macOS, etc.)
- **File Path**: Documentation location
- **Relevance Score**: How well it matches the query
- **Content Preview**: Summary or full content based on request

### Interpreting Results:
1. **High Relevance (>80%)**: Direct match to query
2. **Medium Relevance (50-80%)**: Related concepts
3. **Low Relevance (<50%)**: Peripheral matches

## Advanced Features

### 1. Batch Searches
For comprehensive answers, search multiple related concepts:
```javascript
// Search for related concepts in one batch
[
  {
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "search_apple_docs",
      "arguments": {"query": "SwiftUI List", "platform": "ios"}
    }
  },
  {
    "id": 2,
    "method": "tools/call",
    "params": {
      "name": "search_apple_docs",
      "arguments": {"query": "ForEach SwiftUI", "platform": "ios"}
    }
  }
]
```

### 2. Cross-Framework Searches
When building features that span frameworks:
```javascript
// Search without framework filter to find cross-framework solutions
{
  "arguments": {
    "query": "share extension",
    "platform": "ios"
    // No framework specified - searches all frameworks
  }
}
```

## Error Handling

Common issues and solutions:
1. **No results found**: Broaden search terms or try platform="all"
2. **Too many results**: Add framework filter or more specific terms
3. **Timeout errors**: Reduce limit parameter or split into multiple searches

## Performance Tips

1. **Cache frequent searches**: Results are stable for common queries
2. **Use appropriate limits**: Start with limit=5, increase if needed
3. **Prefer summaries**: Only use include_full_content=true when necessary
4. **Batch related searches**: Send multiple queries in one request

## Example Integration Flow

```javascript
// 1. Initialize connection
{
  "jsonrpc": "2.0",
  "id": "init",
  "method": "initialize",
  "params": {
    "protocolVersion": "1.0.0",
    "clientInfo": {
      "name": "ai-assistant",
      "version": "1.0.0"
    }
  }
}

// 2. User asks: "How do I create a custom SwiftUI button style?"

// 3. Search for documentation
{
  "jsonrpc": "2.0",
  "id": "search-1",
  "method": "tools/call",
  "params": {
    "name": "search_apple_docs",
    "arguments": {
      "query": "ButtonStyle SwiftUI custom",
      "platform": "ios",
      "framework": "SwiftUI",
      "limit": 5
    }
  }
}

// 4. If user needs more detail, read specific resource
{
  "jsonrpc": "2.0",
  "id": "read-1",
  "method": "resources/read",
  "params": {
    "uri": "docs://SwiftUI/ButtonStyle"
  }
}
```

## Best Practices Summary

1. **Always specify platform** - Even if using "all"
2. **Start narrow, expand as needed** - Specific queries yield better results
3. **Use framework filter when known** - Improves relevance significantly
4. **Leverage prompts for common tasks** - They provide structured responses
5. **Batch related searches** - More efficient than sequential requests
6. **Cache results when appropriate** - Documentation is relatively stable

## Need Help?

- Server health: GET `/health` (no auth required)
- Test connection: Try `list_frameworks` with no parameters
- Verify search: Use a known API like "SwiftUI Button" as a test query

Remember: This server contains Apple's official documentation as of the last scrape. For the very latest updates, cross-reference with developer.apple.com.

## Future Enhancements

1. **Binary Results**: Support for image/diagram extraction
2. **OAuth Support**: Dynamic client registration for enterprise
3. **Caching**: Redis for frequent queries
4. **Analytics**: Track popular searches
5. **Monitoring**: Prometheus metrics
6. **Streaming**: Real-time documentation updates