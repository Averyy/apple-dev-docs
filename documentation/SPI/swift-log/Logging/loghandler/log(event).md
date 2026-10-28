---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loghandler/log(event:)"
framework: "swift-log/Logging"
---

# log(event:)

**Framework**: swift-log/Logging  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

The library calls this method when a log handler must emit a log message.

## Declaration

```swift
func log(event: LogEvent)
```

## Mentions

- [Implementing a log handler](../implementingaloghandler.md)

## Discussion

There is no need for the `LogHandler` to check if the level is above or below the configured `logLevel` as `Logger` already performed this check and determined that a message should be logged.

## Parameters

- `event`: The log event containing the level, message, metadata, and source location.

## Default Implementations

### LogHandler Implementations
- [func log(event: LogEvent)](./log%28event%29-17f2r.md)
  Default implementation of [`log(event:)`](./log%28event%29-17f2r.md) for backward compatibility with handlers that implement the deprecated flat-parameter method.

## See Also

### Sending log messages
- [func log(event: LogEvent)](./log%28event%29-17f2r.md)
  Default implementation of [`log(event:)`](./log%28event%29-17f2r.md) for backward compatibility with handlers that implement the deprecated flat-parameter method.
- [func log(level: Logger.Level, message: Logger.Message, metadata: Logger.Metadata?, source: String, file: String, function: String, line: UInt)](./log%28level,message,metadata,source,file,function,line%29.md)
  Please do *not* implement this method when you create a `LogHandler` implementation. Implement [`log(event:)`](./log%28event%29.md) instead.
- [func log(level: Logger.Level, message: Logger.Message, metadata: Logger.Metadata?, source: String, file: String, function: String, line: UInt)](./log%28level,message,metadata,source,file,function,line%29-69pez.md)
  A default implementation for a log message handler that forwards to the SwiftLog 1.0 compatibility method.
- [func log(level: Logging.Logger.Level, message: Logging.Logger.Message, metadata: Logging.Logger.Metadata?, file: String, function: String, line: UInt)](./log%28level,message,metadata,file,function,line%29.md)
  SwiftLog 1.0 log compatibility method.
- [func log(level: Logging.Logger.Level, message: Logging.Logger.Message, metadata: Logging.Logger.Metadata?, file: String, function: String, line: UInt)](./log%28level,message,metadata,file,function,line%29-1xdau.md)
  A default implementation for the SwiftLog 1.0 log message handler.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/loghandler/log(event:))*