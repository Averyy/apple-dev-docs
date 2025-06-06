# structuredLocation

**Framework**: EventKit  
**Kind**: property

The location to trigger an alarm.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var structuredLocation: EKStructuredLocation? { get set }
```

#### Discussion

This property is used in conjunction with [`proximity`](ekalarm/proximity.md) to perform geofence-based triggering of reminders.

## See Also

- [enum EKAlarmProximity](ekalarmproximity.md)
  A value indicating whether an alarm is triggered by entering or exiting a region.
- [var proximity: EKAlarmProximity](ekalarm/proximity.md)
  A value indicating how a location-based alarm is triggered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekalarm/structuredlocation)*