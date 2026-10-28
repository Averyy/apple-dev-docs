---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/multiplexloghandler/log(level:message:metadata:file:function:line:)"
framework: "swift-log/Logging"
---

# log(level:message:metadata:file:function:line:)

**Framework**: swift-log/Logging  
**Kind**: method  
**Role**: Instance Method

A default implementation for the SwiftLog 1.0 log message handler.

## Declaration

```swift
func log(level: Logging.Logger.Level, message: Logging.Logger.Message, metadata: Logging.Logger.Metadata?, file: String, function: String, line: UInt)
```

## Discussion

Forwards to [`log(event:)`](./log%28event%29.md) directly. Forwarding to the source-carrying deprecated method closed a cycle with its own default, so a handler implementing only [`log(event:)`](./log%28event%29.md) overflowed the stack when called through this entry point.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/multiplexloghandler/log(level:message:metadata:file:function:line:))*