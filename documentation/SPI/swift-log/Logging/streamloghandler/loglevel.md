---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/streamloghandler/loglevel"
framework: "swift-log/Logging"
---

# logLevel

**Framework**: swift-log/Logging  
**Kind**: property  
**Role**: Instance Property

Get the log level configured for this `Logger`.

## Declaration

```swift
var logLevel: Logger.Level
```

#### Discussion

> **Note**: Changing the log level threshold for a logger only affects the instance of the `Logger` where you change it. It is acceptable for logging backends to have some form of global log level override that affects multiple or even all loggers. This means a change in `logLevel` to one `Logger` might in certain cases have no effect.

## See Also

### Inspecting a log handler
- [var metadata: Logger.Metadata](./metadata.md)
  Get or set the entire metadata storage as a dictionary.
- [var metadataProvider: Logger.MetadataProvider?](./metadataprovider.md)
  The metadata provider.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/streamloghandler/loglevel)*