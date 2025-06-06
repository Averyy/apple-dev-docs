# workoutEvents

**Framework**: HealthKit  
**Kind**: property

An array of workout event objects.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var workoutEvents: [HKWorkoutEvent]? { get }
```

#### Discussion

This array specifies when the user has paused and resumed the workout activity. This method calculates the workout’s duration based on the amount of active time between the provided start and end dates. For more information on workout events, see [`HKWorkoutEvent`](hkworkoutevent.md).

## See Also

- [var duration: TimeInterval](hkworkout/duration.md)
  The workout’s duration.
- [var workoutActivityType: HKWorkoutActivityType](hkworkout/workoutactivitytype.md)
  The type of activity performed during the workout.
- [var workoutActivities: [HKWorkoutActivity]](hkworkout/workoutactivities.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkout/workoutevents)*