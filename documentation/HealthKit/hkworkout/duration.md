# duration

**Framework**: HealthKit  
**Kind**: property

The workout’s duration.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var duration: TimeInterval { get }
```

## Mentions

- [Adding samples to a workout](adding-samples-to-a-workout.md)

#### Discussion

A workout’s duration can be specified in one of three ways. The [`init(activityType:start:end:)`](hkworkout/init(activitytype:start:end:).md) method uses the time interval between the provided start and end dates. The [`init(activityType:start:end:duration:totalEnergyBurned:totalDistance:metadata:)`](hkworkout/init(activitytype:start:end:duration:totalenergyburned:totaldistance:metadata:).md) method sets the duration to the provided value. And the [`init(activityType:start:end:workoutEvents:totalEnergyBurned:totalDistance:metadata:)`](hkworkout/init(activitytype:start:end:workoutevents:totalenergyburned:totaldistance:metadata:).md) method calculates the total active duration based on the start and end dates and the workout events.

## See Also

- [var workoutActivityType: HKWorkoutActivityType](hkworkout/workoutactivitytype.md)
  The type of activity performed during the workout.
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkout/duration)*