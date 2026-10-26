---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logevent/source"
framework: "swift-log/Logging"
---

# source

**Framework**: swift-log/Logging  
**Kind**: property  
**Role**: Instance Property

The source where this log event originated, for example the logging module.

## Declaration

```swift
var source: String { get set }
```

#### Discussion

When no explicit source was provided at the call site, this is derived lazily from [`file`](./file.md) every time this property is accessed. Handlers that never read this property pay no allocation cost for source computation.

## See Also

### Inspecting a log event
- [var level: Logger.Level](./level.md)
  The log level of this event.
- [var message: Logger.Message](./message.md)
  The message of this event.
- [var error: (any Error)?](./error.md)
  The error associated with this event, if any.
- [var metadata: Logger.Metadata?](./metadata.md)
  The metadata associated with this event, if any.
- [var file: String](./file.md)
  The file this log event originates from.
- [var function: String](./function.md)
  The function this log event originates from.
- [var line: UInt](./line.md)
  The line this log event originates from.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logevent/source)*