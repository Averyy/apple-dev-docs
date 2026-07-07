# HKWorkoutZoneConfiguration

**Framework**: HealthKit  
**Kind**: struct

A structure that defines a complete set of zones for a quantity type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct HKWorkoutZoneConfiguration
```

#### Overview

This structure contains an ordered array of zones and identifies the [`source`](hkworkoutzoneconfiguration/source-swift.property.md) of the configuration. The system generates zones automatically based on people’s health metrics. People can configure zones manually in Health Settings, or apps can provide custom zones for specific workouts.

## Topics

### Creating zone configurations
- [init(quantityType: HKQuantityType, zoneBoundaries: [HKQuantity]) throws](hkworkoutzoneconfiguration/init(quantitytype:zoneboundaries:).md)
  Initializes a zone configuration from zone boundaries for the specified quantity type.
### Accessing configuration properties
- [var quantityType: HKQuantityType](hkworkoutzoneconfiguration/quantitytype.md)
  A property that specifies the quantity type to which the zones apply.
- [let zones: [HKWorkoutZone]](hkworkoutzoneconfiguration/zones.md)
  A property that contains the workout zones, ordered from lowest to highest threshold.
### Identifying the configuration source
- [let source: HKWorkoutZoneConfiguration.Source](hkworkoutzoneconfiguration/source-swift.property.md)
  A property that identifies the origin of this zone configuration.
- [HKWorkoutZoneConfiguration.Source](hkworkoutzoneconfiguration/source-swift.enum.md)
  An enumeration that identifies the origin of the zone configuration.
### Comparing configurations
- [static func == (HKWorkoutZoneConfiguration, HKWorkoutZoneConfiguration) -> Bool](hkworkoutzoneconfiguration/==(_:_:).md)

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
- [struct HKWorkoutZoneDuration](hkworkoutzoneduration.md)
  A structure that represents the time spent in a specific zone during a workout or activity.
- [struct HKWorkoutZoneGroup](hkworkoutzonegroup.md)
  A structure that contains zone configuration and time-in-zone data for a quantity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutzoneconfiguration)*