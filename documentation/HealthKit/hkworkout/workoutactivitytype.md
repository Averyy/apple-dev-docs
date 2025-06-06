# workoutActivityType

**Framework**: HealthKit  
**Kind**: property

The type of activity performed during the workout.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var workoutActivityType: HKWorkoutActivityType { get }
```

#### Discussion

For the complete list of activity types, see [`HKWorkoutActivityType`](hkworkoutactivitytype.md).

## See Also

- [var duration: TimeInterval](hkworkout/duration.md)
  The workout’s duration.
- [var workoutActivities: [HKWorkoutActivity]](hkworkout/workoutactivities.md)
- [var workoutEvents: [HKWorkoutEvent]?](hkworkout/workoutevents.md)
  An array of workout event objects.
- [func statistics(for: HKQuantityType) -> HKStatistics?](hkworkout/statistics(for:).md)
  Returns the workout’s statistics for the provided quantity type.
- [var allStatistics: [HKQuantityType : HKStatistics]](hkworkout/allstatistics.md)
  A dictionary that contains all the statistics for the workout.
- [var totalDistance: HKQuantity?](hkworkout/totaldistance.md)
  The total distance traveled during the workout.
- [var totalEnergyBurned: HKQuantity?](hkworkout/totalenergyburned.md)
  The total active energy burned during the workout.
- [var totalFlightsClimbed: HKQuantity?](hkworkout/totalflightsclimbed.md)
  The total number of flights of stairs climbed during the workout.
- [var totalSwimmingStrokeCount: HKQuantity?](hkworkout/totalswimmingstrokecount.md)
  The total stroke count for the workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkout/workoutactivitytype)*