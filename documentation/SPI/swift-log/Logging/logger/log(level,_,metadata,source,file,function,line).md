---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/log(level:_:metadata:source:file:function:line:)"
framework: "swift-log/Logging"
---

# log(level:_:metadata:source:file:function:line:)

**Framework**: swift-log/Logging  
**Kind**: method  
**Role**: Instance Method

Log a message using the log level and source that you provide.

## Declaration

```swift
func log(level: Logger.Level, _ message: @autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata? = nil, source: @autoclosure () -> String? = nil, file: String = #fileID, function: String = #function, line: UInt = #line)
```

## Discussion

If the `logLevel` passed to this method is more severe than the `Logger`’s [`logLevel`](./loglevel.md), the library logs the message, otherwise nothing will happen.

NOTE: This method adds a constant overhead over calling level-specific methods.

## Parameters

- `level`: The severity level of the `message`.
- `message`: The message to be logged. The `message` parameter supports any string interpolation literal.
- `metadata`: One-off metadata to attach to this log message.
- `source`: The source this log message originates from. The value defaults to the module that emits the log message.
- `file`: The file this log message originates from. There’s usually no need to pass it explicitly, as it defaults to `#fileID`.
- `function`: The function this log message originates from. There’s usually no need to pass it explicitly, as it defaults to `#function`.
- `line`: The line this log message originates from. There’s usually no need to pass it explicitly, as it defaults to `#line`.

## See Also

### Sending general log messages
- [func log(level: Logger.Level, @autoclosure () -> Logger.Message, metadata: @autoclosure () -> Logger.Metadata?, file: String, function: String, line: UInt)](./log%28level,_,metadata,file,function,line%29.md)
  Log a message using the log level you provide.
- [func log(level: Logger.Level, @autoclosure () -> Logger.Message, error: @autoclosure () -> (any Error)?, metadata: @autoclosure () -> Logger.Metadata?, source: @autoclosure () -> String?, file: String, function: String, line: UInt)](./log%28level,_,error,metadata,source,file,function,line%29.md)
  Log a message using the log level and source that you provide.
- [Logger.Level](./level.md)
  The log level.
- [Logger.Message](./message.md)
  The content of log message.
- [typealias Metadata](./metadata.md)
  The type of the metadata storage.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logger/log(level:_:metadata:source:file:function:line:))*