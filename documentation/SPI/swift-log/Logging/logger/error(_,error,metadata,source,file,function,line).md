---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/error(_:error:metadata:source:file:function:line:)"
framework: "swift-log/Logging"
---

# error(_:error:metadata:source:file:function:line:)

**Framework**: swift-log/Logging  
**Kind**: method  
**Role**: Instance Method

Log a message at the ‘error’ log level with the source that you provide.

## Declaration

```swift
func error(_ message: @autoclosure () -> Logger.Message, error: @autoclosure () -> (any Error)? = nil, metadata: @autoclosure () -> Logger.Metadata? = nil, source: @autoclosure () -> String? = nil, file: String = #fileID, function: String = #function, line: UInt = #line)
```

## Discussion

If [`Logger.Level.error`](./level/error.md) is at least as severe as this logger’s [`logLevel`](./loglevel.md) the system logs the message; otherwise nothing will happen.

## Parameters

- `message`: The message to be logged. The `message` parameter supports any string interpolation literal.
- `error`: An `Error` related to the event.
- `metadata`: One-off metadata to attach to this log message.
- `source`: The source this log message originates from. The value defaults to the module that emits the log message.
- `file`: The file this log message originates from. There’s usually no need to pass it explicitly, as it defaults to `#fileID`.
- `function`: The function this log message originates from. There’s usually no need to pass it explicitly, as it defaults to `#function`.
- `line`: The line this log message originates from. There’s usually no need to pass it explicitly, as it defaults to `#line`.

## See Also

### Sending error log messages
- [func error(@autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, file: String, function: String, line: UInt)](./error%28_,metadata,file,function,line%29.md)
  Log a message at the ‘error’ log level.
- [func error(@autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./error%28_,metadata,source,file,function,line%29.md)
  Log a message at the ‘error’ log level with the source that you provide.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/error(_:error:metadata:source:file:function:line:))*