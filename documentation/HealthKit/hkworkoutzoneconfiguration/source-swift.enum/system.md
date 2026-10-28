# HKWorkoutZoneConfiguration.Source.system

**Framework**: HealthKit  
**Kind**: case  
**Role**: Case

A case that indicates the system generated the zones automatically.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
case system
```

## Discussion

The system calculates zones based on the person’s health metrics, including age, resting heart rate, height, and weight. The system recalculates these zones periodically as the person’s metrics change.

## See Also

### Identifying the source
- [HKWorkoutZoneConfiguration.Source.user](./user.md)
  A case that indicates the person configured the zones manually in Health Settings.
- [HKWorkoutZoneConfiguration.Source.app](./app.md)
  A case that indicates an app provided the zones for a specific workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutzoneconfiguration/source-swift.enum/system)*