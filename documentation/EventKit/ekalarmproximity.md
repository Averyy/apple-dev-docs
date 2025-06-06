# EKAlarmProximity

**Framework**: EventKit  
**Kind**: enum

A value indicating whether an alarm is triggered by entering or exiting a region.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum EKAlarmProximity
```

## Topics

### Constants
- [EKAlarmProximity.none](ekalarmproximity/none.md)
  The alarm has no proximity trigger.
- [EKAlarmProximity.enter](ekalarmproximity/enter.md)
  The alarm is set to fire when entering a region.
- [EKAlarmProximity.leave](ekalarmproximity/leave.md)
  The alarm is set to fire when leaving a region.
### Initializers
- [init?(rawValue: Int)](ekalarmproximity/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var proximity: EKAlarmProximity](ekalarm/proximity.md)
  A value indicating how a location-based alarm is triggered.
- [var structuredLocation: EKStructuredLocation?](ekalarm/structuredlocation.md)
  The location to trigger an alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekalarmproximity)*