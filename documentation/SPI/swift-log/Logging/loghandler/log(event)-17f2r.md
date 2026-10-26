---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loghandler/log(event:)-17f2r"
framework: "swift-log/Logging"
---

# log(event:)

**Framework**: swift-log/Logging  
**Kind**: method  
**Role**: Instance Method

Default implementation of [`log(event:)`](./log%28event%29-17f2r.md) for backward compatibility with handlers that implement the deprecated flat-parameter method.

> **Deprecated**: You should implement this method instead of using the default implementation

## Declaration

```swift
func log(event: LogEvent)
```

#### Discussion

Handlers that implement [`log(level:message:metadata:source:file:function:line:)`](./log%28level,message,metadata,source,file,function,line%29.md) continue to work without any source changes; this default forwards the event’s fields to that method.

New handlers should implement [`log(event:)`](./log%28event%29-17f2r.md) directly and rely on this default only as a fallback.

> ⚠️ **Warning**: Do not call this default directly. It exists only as a backward-compatibility bridge. Implement [`log(event:)`](./log%28event%29-17f2r.md) in your [`LogHandler`](../loghandler.md) instead.

## See Also

### Sending log messages
- [func log(event: LogEvent)](./log%28event%29.md)
  The library calls this method when a log handler must emit a log message.
- [func log(level: Logger.Level, message: Logger.Message, metadata: Logger.Metadata?, source: String, file: String, function: String, line: UInt)](./log%28level,message,metadata,source,file,function,line%29.md)
  Please do *not* implement this method when you create a `LogHandler` implementation. Implement [`log(event:)`](./log%28event%29.md) instead.
- [func log(level: Logger.Level, message: Logger.Message, metadata: Logger.Metadata?, source: String, file: String, function: String, line: UInt)](./log%28level,message,metadata,source,file,function,line%29-69pez.md)
  A default implementation for a log message handler that forwards to the SwiftLog 1.0 compatibility method.
- [func log(level: Logging.Logger.Level, message: Logging.Logger.Message, metadata: Logging.Logger.Metadata?, file: String, function: String, line: UInt)](./log%28level,message,metadata,file,function,line%29.md)
  SwiftLog 1.0 log compatibility method.
- [func log(level: Logging.Logger.Level, message: Logging.Logger.Message, metadata: Logging.Logger.Metadata?, file: String, function: String, line: UInt)](./log%28level,message,metadata,file,function,line%29-1xdau.md)
  A default implementation for the SwiftLog 1.0 log message handler.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loghandler/log(event:)-17f2r)*