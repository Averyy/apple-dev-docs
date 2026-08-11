# zoneGroupsByType

**Framework**: HealthKit  
**Kind**: property

A property that contains a dictionary that maps quantity types to their zone groups for this workout.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
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

This property provides zone data for the workout’s primary activity, covering the full workout duration. Access zone groups for individual activities using [`zoneGroupsByType`](hkworkoutactivity/zonegroupsbytype.md).

## See Also

- [func zoneGroup(for: HKQuantityType) -> HKWorkoutZoneGroup?](hkworkout/zonegroup(for:).md)
  Returns the current zone group for the specified quantity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkout/zonegroupsbytype)*