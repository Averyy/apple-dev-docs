---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loghandler/metadata"
framework: "swift-log/Logging"
---

# metadata

**Framework**: swift-log/Logging  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Get or set the entire metadata storage as a dictionary.

## Declaration

```swift
var metadata: Logger.Metadata { get set }
```

#### Discussion

> **Note**: `LogHandler`s must treat logging metadata as a value type. This means that the change in metadata must only affect this very `LogHandler`.

## See Also

### Inspecting a log handler
- [var logLevel: Logger.Level](./loglevel.md)
  Get or set the configured log level.
- [var metadataProvider: Logger.MetadataProvider?](./metadataprovider.md)
  The metadata provider this log handler uses when a log statement is about to be emitted.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loghandler/metadata)*