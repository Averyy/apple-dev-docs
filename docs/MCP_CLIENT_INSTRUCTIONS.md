# Apple Docs MCP Server - AI/LLM Developer Guide

## Overview
This MCP server provides semantic search over 341,207 Apple Developer Documentation pages across 360 frameworks. It's optimized for AI assistants helping developers build Apple apps.

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
- **Endpoint**: `http://192.168.2.5:8080/mcp` (or your server IP)
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
  - If omitted: Returns all 360 frameworks
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