# HKWorkoutZoneGroup

**Framework**: HealthKit  
**Kind**: struct

A structure that contains zone configuration and time-in-zone data for a quantity type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct HKWorkoutZoneGroup
```

## Mentions

- [Accessing workout zone data](accessing-workout-zone-data.md)

#### Overview

This structure combines an [`HKWorkoutZoneConfiguration`](hkworkoutzoneconfiguration.md) with an array of [`HKWorkoutZoneDuration`](hkworkoutzoneduration.md) instances. Access zone groups from [`HKWorkout`](hkworkout.md) and [`HKWorkoutActivity`](hkworkoutactivity.md) instances to retrieve zone data for completed workouts, or from [`HKWorkoutBuilder`](hkworkoutbuilder.md) for real-time zone information during active workouts.

## Topics

### Accessing group properties
- [let configuration: HKWorkoutZoneConfiguration](hkworkoutzonegroup/configuration.md)
  A property that specifies the zone configuration that defines the zones for this group.
- [let zoneDurations: [HKWorkoutZoneDuration]](hkworkoutzonegroup/zonedurations.md)
  A property that contains the time spent in each zone, ordered from lowest to highest threshold.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutzonegroup)*