# HKWorkoutZoneConfiguration.Source.app

**Framework**: HealthKit  
**Kind**: case

A case that indicates an app provided the zones for a specific workout.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
case app
```

#### Discussion

Apps create custom zone configurations by calling [`init(quantityType:zoneBoundaries:)`](hkworkoutzoneconfiguration/init(quantitytype:zoneboundaries:).md) and applying them to workouts with [`setCustomZoneConfiguration(_:for:)`](hkworkoutbuilder/setcustomzoneconfiguration(_:for:).md). Custom configurations apply only to the workout in which they’re set, and don’t modify the person’s preferred zones.

## See Also

- [HKWorkoutZoneConfiguration.Source.system](hkworkoutzoneconfiguration/source-swift.enum/system.md)
  A case that indicates the system generated the zones automatically.
- [HKWorkoutZoneConfiguration.Source.user](hkworkoutzoneconfiguration/source-swift.enum/user.md)
  A case that indicates the person configured the zones manually in Health Settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutzoneconfiguration/source-swift.enum/app)*