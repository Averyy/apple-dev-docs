---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loghandler/log(level:message:metadata:source:file:function:line:)-69pez"
framework: "swift-log/Logging"
---

# log(level:message:metadata:source:file:function:line:)

**Framework**: swift-log/Logging  
**Kind**: method  
**Role**: Instance Method

A default implementation for a log message handler that forwards to the SwiftLog 1.0 compatibility method.

## Declaration

```swift
func log(level: Logger.Level, message: Logger.Message, metadata: Logger.Metadata?, source: String, file: String, function: String, line: UInt)
```

## See Also

### Sending log messages
- [func log(event: LogEvent)](./log%28event%29.md)
  The library calls this method when a log handler must emit a log message.
- [func log(event: LogEvent)](./log%28event%29-17f2r.md)
  Default implementation of [`log(event:)`](./log%28event%29-17f2r.md) for backward compatibility with handlers that implement the deprecated flat-parameter method.
- [func log(level: Logger.Level, message: Logger.Message, metadata: Logger.Metadata?, source: String, file: String, function: String, line: UInt)](./log%28level,message,metadata,source,file,function,line%29.md)
  Please do *not* implement this method when you create a `LogHandler` implementation. Implement [`log(event:)`](./log%28event%29.md) instead.
- [func log(level: Logging.Logger.Level, message: Logging.Logger.Message, metadata: Logging.Logger.Metadata?, file: String, function: String, line: UInt)](./log%28level,message,metadata,file,function,line%29.md)
  SwiftLog 1.0 log compatibility method.
- [func log(level: Logging.Logger.Level, message: Logging.Logger.Message, metadata: Logging.Logger.Metadata?, file: String, function: String, line: UInt)](./log%28level,message,metadata,file,function,line%29-1xdau.md)
  A default implementation for the SwiftLog 1.0 log message handler.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loghandler/log(level:message:metadata:source:file:function:line:)-69pez)*