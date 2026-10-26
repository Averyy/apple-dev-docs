---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/debug(_:metadata:file:function:line:)"
framework: "swift-log/Logging"
---

# debug(_:metadata:file:function:line:)

**Framework**: swift-log/Logging  
**Kind**: method  
**Role**: Instance Method

Log a message at the ‘debug’ log level.

## Declaration

```swift
func debug(_ message: @autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata? = nil, file: String = #fileID, function: String = #function, line: UInt = #line)
```

#### Discussion

If [`Logger.Level.debug`](./level/debug.md) is at least as severe as this logger’s [`logLevel`](./loglevel.md) the system logs the message; otherwise nothing will happen.

## Parameters

- `message`: The message to be logged. The `message` parameter supports any string interpolation literal.
- `metadata`: One-off metadata to attach to this log message.
- `file`: The file this log message originates from. There’s usually no need to pass it explicitly, as it defaults to `#fileID`.
- `function`: The function this log message originates from. There’s usually no need to pass it explicitly, as it defaults to `#function`.
- `line`: The line this log message originates from. There’s usually no need to pass it explicitly, as it defaults to `#line`.

## See Also

### Sending debug log messages
- [func debug(@autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./debug%28_,metadata,source,file,function,line%29.md)
  Log a message at the ‘debug’ log level with the source that you provide.
- [func debug(@autoclosure () -> Logger.Message, error: @autoclosure () -> (any Error)?, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./debug%28_,error,metadata,source,file,function,line%29.md)
  Log a message at the ‘debug’ log level with the source that you provide.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/debug(_:metadata:file:function:line:))*