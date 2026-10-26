---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/init(label:)"
framework: "swift-log/Logging"
---

# init(label:)

**Framework**: swift-log/Logging  
**Kind**: init  
**Role**: Initializer

Construct a logger with the label you provide to identify the creator of the logger.

## Declaration

```swift
init(label: String)
```

## Mentions

- [003: Logger propagation in libraries](../api-003-acceptingloggers.md)

#### Discussion

The `label` should identify the creator of the `Logger`. This can be an application, a sub-system, or a datatype.

## Parameters

- `label`: An identifier for the creator of a `Logger`.

## See Also

### Creating Loggers
- [init(label: String, metadataProvider: MetadataProvider)](./init%28label,metadataprovider%29.md)
  Creates a logger using the label that identifies the creator of the logger or a non-standard log handler.
- [init(label: String, factory: (String) -> any LogHandler)](./init%28label,factory%29-9uiy2.md)
  Creates a logger using the label that identifies the creator of the logger or a non-standard log handler.
- [init(label: String, factory: (String, Logger.MetadataProvider?) -> any LogHandler)](./init%28label,factory%29-6iktu.md)
  Creates a logger using the label that identifies the creator of the logger or a non-standard log handler.
- [Logger.MetadataProvider](./metadataprovider-swift.struct.md)
  A MetadataProvider automatically injects runtime-generated metadata to all logs emitted by a logger.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/init(label:))*