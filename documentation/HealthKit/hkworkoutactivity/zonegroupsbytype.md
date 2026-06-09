# zoneGroupsByType

**Framework**: HealthKit  
**Kind**: property

A property that contains a dictionary that maps quantity types to their zone groups for this activity.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var zoneGroupsByType: [HKQuantityType : HKWorkoutZoneGroup]? { get }
```

## Mentions

- [Accessing workout zone data](accessing-workout-zone-data.md)

#### Discussion

This property provides zone data specific to the activity’s time range within the workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutactivity/zonegroupsbytype)*