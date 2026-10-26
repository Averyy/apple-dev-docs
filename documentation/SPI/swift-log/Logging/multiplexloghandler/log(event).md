---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/multiplexloghandler/log(event:)"
framework: "swift-log/Logging"
---

# log(event:)

**Framework**: swift-log/Logging  
**Kind**: method  
**Role**: Instance Method

Log a message using the log level and source that you provide.

## Declaration

```swift
func log(event: LogEvent)
```

#### Discussion

Metadata from this handler’s metadata provider overrides metadata from the underlying handlers and their providers. Explicit metadata in the log event takes precedence over this handler’s provider.

## Parameters

- `event`: The log event containing the level, message, metadata, and source location.

## See Also

### Sending log messages
- [func log(level: Logger.Level, message: Logger.Message, metadata: Logger.Metadata?, source: String, file: String, function: String, line: UInt)](./log%28level,message,metadata,source,file,function,line%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/multiplexloghandler/log(event:))*