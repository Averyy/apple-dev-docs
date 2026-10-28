---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadataprovider-swift.struct"
framework: "swift-log/Logging"
---

# Logger.MetadataProvider

**Framework**: swift-log/Logging  
**Kind**: struct  
**Role**: Structure

A MetadataProvider automatically injects runtime-generated metadata to all logs emitted by a logger.

## Declaration

```swift
struct MetadataProvider
```

### Example

A metadata provider may be used to automatically inject metadata such as trace IDs:

```swift
import Tracing // https://github.com/apple/swift-distributed-tracing

let metadataProvider = MetadataProvider {
    guard let traceID = Baggage.current?.traceID else { return nil }
    return ["traceID": "\(traceID)"]
}
let logger = Logger(label: "example", metadataProvider: metadataProvider)
var baggage = Baggage.topLevel
baggage.traceID = 42
Baggage.withValue(baggage) {
    logger.info("hello") // automatically includes ["traceID": "42"] metadata
}
```

### Metadata with Attributes

Metadata providers can return values that carry attributes via string interpolation:

```swift
let provider = Logger.MetadataProvider {
    [
        "trace-id": "\(Baggage.current?.traceID, sensitivity: .public)",
        "user-id": "\(RequestContext.current.userId, sensitivity: .sensitive)"
    ]
}
```

We recommend referring to [swift-distributed-tracing](https://github.com/apple/swift-distributed-tracing) for metadata providers which make use of its tracing and metadata propagation infrastructure. It is however possible to make use of metadata providers independently of tracing and instruments provided by that library, if necessary.

## Topics

### Creating a metadata provider
- [init(@Sendable () -> Metadata)](./metadataprovider-swift.struct/init%28_%29.md)
  Creates a new metadata provider.
### Invoking the provider
- [func get() -> Metadata](./metadataprovider-swift.struct/get%28%29.md)
  Invokes the metadata provider and returns the generated contextual metadata.
### Merging metadata
- [static func multiplex([Logger.MetadataProvider]) -> Logger.MetadataProvider?](./metadataprovider-swift.struct/multiplex%28_%29.md)
  A pseudo metadata provider that merges metadata from multiple other metadata providers.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Creating Loggers
- [init(label: String)](./init%28label%29.md)
  Construct a logger with the label you provide to identify the creator of the logger.
- [init(label: String, metadataProvider: MetadataProvider)](./init%28label,metadataprovider%29.md)
  Creates a logger using the label that identifies the creator of the logger or a non-standard log handler.
- [init(label: String, factory: (String) -> any LogHandler)](./init%28label,factory%29-9uiy2.md)
  Creates a logger using the label that identifies the creator of the logger or a non-standard log handler.
- [init(label: String, factory: (String, Logger.MetadataProvider?) -> any LogHandler)](./init%28label,factory%29-6iktu.md)
  Creates a logger using the label that identifies the creator of the logger or a non-standard log handler.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadataprovider-swift.struct)*