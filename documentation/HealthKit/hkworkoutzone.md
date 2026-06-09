# HKWorkoutZone

**Framework**: HealthKit  
**Kind**: struct

A structure that represents a single zone with defined thresholds for a quantity type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct HKWorkoutZone
```

#### Overview

The system creates workout zones as part of an [`HKWorkoutZoneConfiguration`](hkworkoutzoneconfiguration.md). This structure defines the minimum and maximum values that determine when a quantity type measurement falls within the zone. For example, a heart rate zone might have a minimum of 136.8 beats per minute and a maximum of 147.6 beats per minute.

## Topics

### Accessing zone properties
- [let index: Int](hkworkoutzone/index.md)
  The zero-based index of the zone within the containing zone configuration, ordered from lowest to highest threshold.
- [var minimum: HKQuantity?](hkworkoutzone/minimum.md)
  The minimum threshold for the zone.
- [var maximum: HKQuantity?](hkworkoutzone/maximum.md)
  The maximum threshold for the zone.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Tracking heart rate zones for workouts](tracking-heart-rate-zones-for-workouts.md)
  Start a workout on iOS or watchOS and track and display heart rate zones.
- [Accessing workout zone data](accessing-workout-zone-data.md)
  Provide training insights to people on your app using workout zone data.
- [struct HKWorkoutZoneConfiguration](hkworkoutzoneconfiguration.md)
  A structure that defines a complete set of zones for a quantity type.
- [struct HKWorkoutZoneDuration](hkworkoutzoneduration.md)
  A structure that represents the time spent in a specific zone during a workout or activity.
- [struct HKWorkoutZoneGroup](hkworkoutzonegroup.md)
  A structure that contains zone configuration and time-in-zone data for a quantity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutzone)*