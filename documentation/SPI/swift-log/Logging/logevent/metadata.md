---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logevent/metadata"
framework: "swift-log/Logging"
---

# metadata

**Framework**: swift-log/Logging  
**Kind**: property  
**Role**: Instance Property

The metadata associated with this event, if any.

## Declaration

```swift
var metadata: Logger.Metadata?
```

#### Discussion

Metadata values may carry attributes accessible via [`attributes`](../logger/metadatavalue/attributes.md).

## See Also

### Inspecting a log event
- [var level: Logger.Level](./level.md)
  The log level of this event.
- [var message: Logger.Message](./message.md)
  The message of this event.
- [var error: (any Error)?](./error.md)
  The error associated with this event, if any.
- [var source: String](./source.md)
  The source where this log event originated, for example the logging module.
- [var file: String](./file.md)
  The file this log event originates from.
- [var function: String](./function.md)
  The function this log event originates from.
- [var line: UInt](./line.md)
  The line this log event originates from.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/logevent/metadata)*