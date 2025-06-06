# relativeStartTime

**Framework**: SensorKit  
**Kind**: property

The time the user starts the app relative to the start time of the first app in a report interval.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
var relativeStartTime: TimeInterval { get }
```

#### Discussion

Use this property to order and determine the time between app instances in the same report. The first instance of this property in the report interval is `0`.

## See Also

- [var usageTime: TimeInterval](srdeviceusagereport/applicationusage/usagetime.md)
  The amount of time the user uses the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srdeviceusagereport/applicationusage/relativestarttime)*