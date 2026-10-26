---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/streamloghandler/init(label:stream:)"
framework: "swift-log/Logging"
---

# init(label:stream:)

**Framework**: swift-log/Logging  
**Kind**: init  
**Role**: Initializer

Creates a [`StreamLogHandler`](../streamloghandler.md) that directs its output to the stream you provide, using the global metadata provider from [`LoggingSystem`](../loggingsystem.md).

## Declaration

```swift
init(label: String, stream: any TextOutputStream & Sendable)
```

## Parameters

- `label`: The label for this log handler.
- `stream`: The stream to write log output to.

## See Also

### Creating a stream log handler
- [static func standardOutput(label: String) -> StreamLogHandler](./standardoutput%28label%29.md)
  Creates a stream log handler that directs its output to STDOUT.
- [static func standardOutput(label: String, metadataProvider: Logger.MetadataProvider?) -> StreamLogHandler](./standardoutput%28label,metadataprovider%29.md)
  Creates a stream log handler that directs its output to STDOUT using the metadata provider you provide.
- [static func standardError(label: String) -> StreamLogHandler](./standarderror%28label%29.md)
  Creates a stream log handler that directs its output to STDERR.
- [static func standardError(label: String, metadataProvider: Logger.MetadataProvider?) -> StreamLogHandler](./standarderror%28label,metadataprovider%29.md)
  Creates a stream log handler that directs its output to STDERR using the metadata provider you provide.
- [init(label: String, stream: any TextOutputStream & Sendable, metadataProvider: Logger.MetadataProvider?)](./init%28label,stream,metadataprovider%29.md)
  Creates a [`StreamLogHandler`](../streamloghandler.md) that directs its output to the stream you provide, using the metadata provider you provide.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/streamloghandler/init(label:stream:))*