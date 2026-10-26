---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/002-structuredlogging"
framework: "swift-log/Logging"
---

# 002: Structured logging

**Framework**: swift-log/Logging  
**Role**: Article

Use metadata to create machine-readable, searchable log entries.

#### Overview

Structured logging uses metadata to separate human-readable messages from machine-readable data. This practice makes logs easier to search, filter, and analyze programmatically while maintaining readability.

##### Motivation

Traditional string-based logging embeds all information in the message text, making it more difficult for automated tools to parse and extract. Structured logging separates these concerns; messages provide human readable context while metadata provides structured data for tooling.

##### Example

###### Recommended: Structured logging

```swift
// ✅ Structured - message provides context, metadata provides data
logger.info(
    "Accepted connection",
    metadata: [
        "connection.id": "\(id)",
        "connection.peer": "\(peer)", 
        "connections.total": "\(count)"
    ]
)

logger.error(
    "Database query failed",
    metadata: [
        "query.retries": "\(retries)",
        "query.error": "\(error)",
        "query.duration": "\(duration)"
    ]
)
```

##### Advanced: Nested metadata for complex data

```swift
// ✅ Complex structured data
logger.trace(
    "HTTP request started",
    metadata: [
        "request.id": "\(requestId)",
        "request.method": "GET",
        "request.path": "/api/users",
        "request.headers": [
            "user-agent": "\(userAgent)"
        ],
        "client.ip": "\(clientIP)",
        "client.country": "\(country)"
    ]
)
```

###### Avoid: Unstructured logging

```swift
// ❌ Not structured - hard to parse programmatically
logger.info("Accepted connection \(id) from \(peer), total: \(count)")
logger.error("Database query failed after \(retries) retries: \(error)")
```

##### Metadata key conventions

Use hierarchical dot-notation for related fields:

```swift
// ✅ Good: Hierarchical keys
logger.debug(
    "Database operation completed",
    metadata: [
        "db.operation": "SELECT",
        "db.table": "users",
        "db.duration": "\(duration)",
        "db.rows": "\(rowCount)"
    ]
)

// ✅ Good: Consistent prefixing
logger.info(
    "HTTP response",
    metadata: [
        "http.method": "POST",
        "http.status": "201",
        "http.path": "/api/users",
        "http.duration": "\(duration)"
    ]
)
```

## See Also

- [001: Choosing log levels](./api-001-choosingloglevels.md)
  Select appropriate log levels in applications and libraries.
- [003: Logger propagation in libraries](./api-003-acceptingloggers.md)
  Propagate caller context by accepting a `Logger` parameter or reading the task-local [`current`](./logger/current.md) — never by constructing your own logger.
- [004: Testing code that logs](./api-004-testinglogging.md)
  Validate what you code logs by capturing entries in memory rather than bootstrapping a process-wide backend.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/002-structuredlogging)*