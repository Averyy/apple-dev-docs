---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/init(label:metadataprovider:)"
framework: "swift-log/Logging"
---

# init(label:metadataProvider:)

**Framework**: swift-log/Logging  
**Kind**: init  
**Role**: Initializer

Creates a logger using the label that identifies the creator of the logger or a non-standard log handler.

## Declaration

```swift
init(label: String, metadataProvider: MetadataProvider)
```

## Discussion

The `label` should identify the creator of the `Logger`. The label can represent an application, a sub-system, or even a datatype.

## Parameters

- `label`: An identifier for the creator of a `Logger`.
- `metadataProvider`: The custom metadata provider this logger should invoke, instead of the system wide bootstrapped one, when a log statement is about to be emitted.

## See Also

### Creating Loggers
- [init(label: String)](./init%28label%29.md)
  Construct a logger with the label you provide to identify the creator of the logger.
- [init(label: String, factory: (String) -> any LogHandler)](./init%28label,factory%29-9uiy2.md)
  Creates a logger using the label that identifies the creator of the logger or a non-standard log handler.
- [init(label: String, factory: (String, Logger.MetadataProvider?) -> any LogHandler)](./init%28label,factory%29-6iktu.md)
  Creates a logger using the label that identifies the creator of the logger or a non-standard log handler.
- [Logger.MetadataProvider](./metadataprovider-swift.struct.md)
  A MetadataProvider automatically injects runtime-generated metadata to all logs emitted by a logger.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/init(label:metadataprovider:))*