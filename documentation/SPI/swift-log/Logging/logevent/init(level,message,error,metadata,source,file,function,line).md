---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logevent/init(level:message:error:metadata:source:file:function:line:)"
framework: "swift-log/Logging"
---

# init(level:message:error:metadata:source:file:function:line:)

**Framework**: swift-log/Logging  
**Kind**: init  
**Role**: Initializer

Creates a new log event.

## Declaration

```swift
init(level: Logger.Level, message: Logger.Message, error: (any Error)?, metadata: Logger.Metadata?, source: String?, file: String, function: String, line: UInt)
```

## Parameters

- `level`: The log level of this event.
- `message`: The message of this event.
- `error`: The error associated with this event, if any.
- `metadata`: The metadata associated with this event, if any.
- `source`: The source where this log event originated. When `nil`, [`source`](./source.md) is derived lazily from [`file`](./file.md) on first access so handlers that never read it pay no allocation cost.
- `file`: The file this log event originates from.
- `function`: The function this log event originates from.
- `line`: The line this log event originates from.

## See Also

### Creating a log event
- [init(level: Logger.Level, message: Logger.Message, metadata: Logger.Metadata?, source: String?, file: String, function: String, line: UInt)](./init%28level,message,metadata,source,file,function,line%29.md)
  Creates a new log event.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logevent/init(level:message:error:metadata:source:file:function:line:))*