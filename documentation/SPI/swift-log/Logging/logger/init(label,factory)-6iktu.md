---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/init(label:factory:)-6iktu"
framework: "swift-log/Logging"
---

# init(label:factory:)

**Framework**: swift-log/Logging  
**Kind**: init  
**Role**: Initializer

Creates a logger using the label that identifies the creator of the logger or a non-standard log handler.

## Declaration

```swift
init(label: String, factory: (String, Logger.MetadataProvider?) -> any LogHandler)
```

## Discussion

The `label` should identify the creator of the `Logger`. The label can represent an application, a sub-system, or even a datatype.

This initializer provides an escape hatch in case the global default logging backend implementation (set up using `LoggingSystem.bootstrap`) is not appropriate for this particular logger.

## Parameters

- `label`: An identifier for the creator of a `Logger`.
- `factory`: A closure that creates a non-standard `LogHandler`.

## See Also

### Creating Loggers
- [init(label: String)](./init%28label%29.md)
  Construct a logger with the label you provide to identify the creator of the logger.
- [init(label: String, metadataProvider: MetadataProvider)](./init%28label,metadataprovider%29.md)
  Creates a logger using the label that identifies the creator of the logger or a non-standard log handler.
- [init(label: String, factory: (String) -> any LogHandler)](./init%28label,factory%29-9uiy2.md)
  Creates a logger using the label that identifies the creator of the logger or a non-standard log handler.
- [Logger.MetadataProvider](./metadataprovider-swift.struct.md)
  A MetadataProvider automatically injects runtime-generated metadata to all logs emitted by a logger.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/init(label:factory:)-6iktu)*