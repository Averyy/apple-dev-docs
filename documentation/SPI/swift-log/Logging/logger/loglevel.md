---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/loglevel"
framework: "swift-log/Logging"
---

# logLevel

**Framework**: swift-log/Logging  
**Kind**: property  
**Role**: Instance Property

Get or set the log level configured for this `Logger`.

## Declaration

```swift
var logLevel: Logger.Level { get set }
```

## Mentions

- [Disable log levels during compilation](../disableloglevelsduringcompilation.md)

#### Discussion

> **Note**: Changing the log level threshold for a logger only affects the instance of the `Logger` where you change it. It is acceptable for logging backends to have some form of global log level override that affects multiple or even all loggers. This means a change in `logLevel` to one `Logger` might in certain cases have no effect.

## See Also

### Inspecting a logger
- [var label: String](./label.md)
- [var handler: any LogHandler](./handler.md)
  The log handler.
- [var metadataProvider: Logger.MetadataProvider?](./metadataprovider-swift.property.md)
  The metadata provider this logger was created with.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/loglevel)*