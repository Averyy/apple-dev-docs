# configuration

**Framework**: HealthKit  
**Kind**: property

A property that specifies the zone configuration that defines the zones for this group.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
let configuration: HKWorkoutZoneConfiguration
```

#### Discussion

This configuration identifies the source of the zones and contains the zone definitions that the system uses to calculate durations.

## See Also

- [let zoneDurations: [HKWorkoutZoneDuration]](hkworkoutzonegroup/zonedurations.md)
  A property that contains the time spent in each zone, ordered from lowest to highest threshold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutzonegroup/configuration)*