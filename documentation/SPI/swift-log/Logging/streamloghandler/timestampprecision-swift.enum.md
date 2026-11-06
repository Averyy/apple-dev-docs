---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/streamloghandler/timestampprecision-swift.enum"
framework: "swift-log/Logging"
---

# StreamLogHandler.TimestampPrecision

**Framework**: swift-log/Logging  
**Kind**: enum  
**Role**: Enumeration

The precision of the timestamp that a [`StreamLogHandler`](../streamloghandler.md) writes at the start of each log line.

## Declaration

```swift
@nonexhaustive enum TimestampPrecision
```

## Topics

### Enumeration Cases
- [StreamLogHandler.TimestampPrecision.milliseconds](./timestampprecision-swift.enum/milliseconds.md)
  Milliseconds, for example `2025-06-01T14:03:07.042+0000`.
- [StreamLogHandler.TimestampPrecision.seconds](./timestampprecision-swift.enum/seconds.md)
  Whole seconds, for example `2025-06-01T14:03:07+0000`.
### Default Implementations
- [Equatable Implementations](./timestampprecision-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Configuring the timestamp
- [var timestampPrecision: TimestampPrecision](./timestampprecision-swift.property.md)
  The precision of the timestamp written at the start of each log line.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/streamloghandler/timestampprecision-swift.enum)*