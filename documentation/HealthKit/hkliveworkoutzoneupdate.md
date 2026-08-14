# HKLiveWorkoutZoneUpdate

**Framework**: HealthKit  
**Kind**: class

A structure that contains information about zone transitions during a live workout session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS ?+
- watchOS 27.0+ (Beta)

## Declaration

```swift
class HKLiveWorkoutZoneUpdate
```

## Mentions

- [Accessing workout zone data](accessing-workout-zone-data.md)

#### Overview

This structure provides details about zone changes as they occur during a workout. The system sends updates to the [`HKLiveWorkoutBuilderDelegate`](hkliveworkoutbuilderdelegate.md) when the person moves between zones.

## Topics

### Accessing update information
- [var lastSampleProcessedDate: Date?](hkliveworkoutzoneupdate/lastsampleprocesseddate.md)
  The timestamp of the most recent processed sample at the time of the update.
### Accessing zone data
- [var currentZoneDuration: HKWorkoutZoneDuration?](hkliveworkoutzoneupdate/currentzoneduration.md)
  A property that contains the zone duration just entered.
- [var previousZoneDuration: HKWorkoutZoneDuration?](hkliveworkoutzoneupdate/previouszoneduration.md)
  A property that contains the zone duration that just completed.
- [var zoneGroup: HKWorkoutZoneGroup?](hkliveworkoutzoneupdate/zonegroup.md)
  The zone group that contains the current duration data.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Tracking heart rate zones for workouts](tracking-heart-rate-zones-for-workouts.md)
  Start a workout on iOS or watchOS and track and display heart rate zones.
- [Accessing workout zone data](accessing-workout-zone-data.md)
  Provide training insights to people on your app using workout zone data.
- [struct HKWorkoutZone](hkworkoutzone.md)
  A structure that represents a single zone with defined thresholds for a quantity type.
- [struct HKWorkoutZoneConfiguration](hkworkoutzoneconfiguration.md)
  A structure that defines a complete set of zones for a quantity type.
- [struct HKWorkoutZoneDuration](hkworkoutzoneduration.md)
  A structure that represents the time spent in a specific zone during a workout or activity.
- [struct HKWorkoutZoneGroup](hkworkoutzonegroup.md)
  A structure that contains zone configuration and time-in-zone data for a quantity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutzoneupdate)*