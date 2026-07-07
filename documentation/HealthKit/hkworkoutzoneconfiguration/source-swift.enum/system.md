# HKWorkoutZoneConfiguration.Source.system

**Framework**: HealthKit  
**Kind**: case

A case that indicates the system generated the zones automatically.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
case system
```

#### Discussion

The system calculates zones based on the person’s health metrics, including age, resting heart rate, height, and weight. The system recalculates these zones periodically as the person’s metrics change.

## See Also

- [HKWorkoutZoneConfiguration.Source.user](hkworkoutzoneconfiguration/source-swift.enum/user.md)
  A case that indicates the person configured the zones manually in Health Settings.
- [HKWorkoutZoneConfiguration.Source.app](hkworkoutzoneconfiguration/source-swift.enum/app.md)
  A case that indicates an app provided the zones for a specific workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutzoneconfiguration/source-swift.enum/system)*