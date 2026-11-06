---
url: "https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/streamloghandler/timestampprecision-swift.property"
framework: "swift-log/Logging"
---

# timestampPrecision

**Framework**: swift-log/Logging  
**Kind**: property  
**Role**: Instance Property

The precision of the timestamp written at the start of each log line.

## Declaration

```swift
var timestampPrecision: TimestampPrecision
```

## Discussion

Defaults to [`StreamLogHandler.TimestampPrecision.seconds`](./timestampprecision-swift.enum/seconds.md), which keeps the output format that `StreamLogHandler` has always used, for example `2025-06-01T14:03:07+0000`. Some tools parse this output, so the extra precision is opt-in rather than the default.

Set it to [`StreamLogHandler.TimestampPrecision.milliseconds`](./timestampprecision-swift.enum/milliseconds.md) to include milliseconds, for example `2025-06-01T14:03:07.042+0000`.

> **Note**: On WASI the wall clock is only read with second precision, so [`StreamLogHandler.TimestampPrecision.milliseconds`](./timestampprecision-swift.enum/milliseconds.md) always prints `.000` there.

## See Also

### Configuring the timestamp
- [StreamLogHandler.TimestampPrecision](./timestampprecision-swift.enum.md)
  The precision of the timestamp that a [`StreamLogHandler`](../streamloghandler.md) writes at the start of each log line.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-log/main/documentation/logging/streamloghandler/timestampprecision-swift.property)*