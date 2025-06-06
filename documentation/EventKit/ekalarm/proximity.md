# proximity

**Framework**: EventKit  
**Kind**: property

A value indicating how a location-based alarm is triggered.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var proximity: EKAlarmProximity { get set }
```

#### Discussion

Alarms can be set to trigger when entering or exiting a location specified by [`structuredLocation`](ekalarm/structuredlocation.md). By default, alarms are not affected by location.

## See Also

- [enum EKAlarmProximity](ekalarmproximity.md)
  A value indicating whether an alarm is triggered by entering or exiting a region.
- [var structuredLocation: EKStructuredLocation?](ekalarm/structuredlocation.md)
  The location to trigger an alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekalarm/proximity)*