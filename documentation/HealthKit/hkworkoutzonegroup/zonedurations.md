# zoneDurations

**Framework**: HealthKit  
**Kind**: property

A property that contains the time spent in each zone, ordered from lowest to highest threshold.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
let zoneDurations: [HKWorkoutZoneDuration]
```

#### Discussion

Each element in this array corresponds to a zone in the group’s configuration and specifies the duration in seconds.

## See Also

- [let configuration: HKWorkoutZoneConfiguration](hkworkoutzonegroup/configuration.md)
  A property that specifies the zone configuration that defines the zones for this group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutzonegroup/zonedurations)*