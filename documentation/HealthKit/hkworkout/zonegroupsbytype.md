# zoneGroupsByType

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

A property that contains a dictionary that maps quantity types to their zone groups for this workout.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var zoneGroupsByType: [HKQuantityType : HKWorkoutZoneGroup]? { get }
```

## Mentions

- [Accessing workout zone data](../accessing-workout-zone-data.md)

#### Discussion

This property provides zone data for the workout’s primary activity, covering the full workout duration. Access zone groups for individual activities using [`zoneGroupsByType`](../hkworkoutactivity/zonegroupsbytype.md).

## See Also

### Accessing zone data
- [func zoneGroup(for: HKQuantityType) -> HKWorkoutZoneGroup?](./zonegroup%28for%29.md)
  Returns the current zone group for the specified quantity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkout/zonegroupsbytype)*