---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadata"
framework: "swift-log/Logging"
---

# Logger.Metadata

**Framework**: swift-log/Logging  
**Kind**: typealias  
**Role**: Type Alias

The type of the metadata storage.

## Declaration

```swift
typealias Metadata = [String : MetadataValue]
```

#### Discussion

`Metadata` is a typealias for `[String: Logger.MetadataValue]` the type of the metadata storage.

## See Also

### Sending general log messages
- [func log(level: Logger.Level, @autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, file: String, function: String, line: UInt)](./log%28level,_,metadata,file,function,line%29.md)
  Log a message using the log level you provide.
- [func log(level: Logger.Level, @autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./log%28level,_,metadata,source,file,function,line%29.md)
  Log a message using the log level and source that you provide.
- [func log(level: Logger.Level, @autoclosure () -> Logger.Message, error: @autoclosure () -> (any Error)?, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./log%28level,_,error,metadata,source,file,function,line%29.md)
  Log a message using the log level and source that you provide.
- [Logger.Level](./level.md)
  The log level.
- [Logger.Message](./message.md)
  The content of log message.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/metadata)*