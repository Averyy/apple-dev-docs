---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loghandler/metadataprovider"
framework: "swift-log/Logging"
---

# metadataProvider

**Framework**: swift-log/Logging  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The metadata provider this log handler uses when a log statement is about to be emitted.

## Declaration

```swift
var metadataProvider: Logger.MetadataProvider? { get set }
```

## Discussion

A [`Logger.MetadataProvider`](../logger/metadataprovider-swift.struct.md) may add a constant set of metadata, or use task-local values to pick up contextual metadata and add it to emitted logs.

## Default Implementations

### LogHandler Implementations
- [var metadataProvider: Logger.MetadataProvider?](./metadataprovider-7hq13.md)
  Default implementation for a metadata provider that defaults to nil.

## See Also

### Inspecting a log handler
- [var logLevel: Logger.Level](./loglevel.md)
  Get or set the configured log level.
- [var metadata: Logger.Metadata](./metadata.md)
  Get or set the entire metadata storage as a dictionary.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loghandler/metadataprovider)*