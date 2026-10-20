# proximity

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) EKAlarmProximity proximity;
```

#### Discussion

Alarms can be set to trigger when entering or exiting a location specified by [`structuredLocation`](./structuredlocation.md). By default, alarms are not affected by location.

## See Also

### Setting GeoFence-based Alarms
- [enum EKAlarmProximity](../ekalarmproximity.md)
  A value indicating whether an alarm is triggered by entering or exiting a region.
- [var structuredLocation: EKStructuredLocation?](./structuredlocation.md)
  The location to trigger an alarm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekalarm/proximity)*