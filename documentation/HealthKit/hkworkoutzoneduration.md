# HKWorkoutZoneDuration

**Framework**: HealthKit  
**Kind**: struct

A structure that represents the time spent in a specific zone during a workout or activity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct HKWorkoutZoneDuration
```

#### Overview

This structure pairs a zone with the duration of time the person spent in that zone. The system calculates durations based on quantity samples collected during the workout.

## Topics

### Accessing duration properties
- [let zone: HKWorkoutZone](hkworkoutzoneduration/zone.md)
  A property that identifies the workout zone.
- [let duration: TimeInterval](hkworkoutzoneduration/duration.md)
  A property that specifies the time spent in this zone, measured in seconds.

## Relationships

### Conforms To
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
- [struct HKWorkoutZoneGroup](hkworkoutzonegroup.md)
  A structure that contains zone configuration and time-in-zone data for a quantity type.
- [class HKLiveWorkoutZoneUpdate](hkliveworkoutzoneupdate.md)
  A structure that contains information about zone transitions during a live workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutzoneduration)*