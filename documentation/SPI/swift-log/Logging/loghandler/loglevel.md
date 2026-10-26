---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loghandler/loglevel"
framework: "swift-log/Logging"
---

# logLevel

**Framework**: swift-log/Logging  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Get or set the configured log level.

## Declaration

```swift
var logLevel: Logger.Level { get set }
```

#### Discussion

> **Note**: `LogHandler`s must treat the log level as a value type. This means that the change in metadata must only affect this very `LogHandler`. It is acceptable to provide some form of global log level override that means a change in log level on a particular `LogHandler` might not be reflected in any `LogHandler`.

## See Also

### Inspecting a log handler
- [var metadata: Logger.Metadata](./metadata.md)
  Get or set the entire metadata storage as a dictionary.
- [var metadataProvider: Logger.MetadataProvider?](./metadataprovider.md)
  The metadata provider this log handler uses when a log statement is about to be emitted.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loghandler/loglevel)*