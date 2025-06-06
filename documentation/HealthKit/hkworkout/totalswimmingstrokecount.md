# totalSwimmingStrokeCount

**Framework**: HealthKit  
**Kind**: property

The total stroke count for the workout.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var totalSwimmingStrokeCount: HKQuantity? { get }
```

#### Discussion

This property contains a quantity using count units, or `nil`.

> **Note**:  Provide a total stroke count value whenever the stroke count is relevant to the workout type. In addition, add stroke count samples to a workout using the [`add(_:to:completion:)`](hkhealthstore/add(_:to:completion:).md) method. These samples should sum up to the total stroke count, while providing detailed information about how the intensity changes over the duration of the workout.

 Provide a total stroke count value whenever the stroke count is relevant to the workout type. In addition, add stroke count samples to a workout using the [`add(_:to:completion:)`](hkhealthstore/add(_:to:completion:).md) method. These samples should sum up to the total stroke count, while providing detailed information about how the intensity changes over the duration of the workout.

## See Also

- [var duration: TimeInterval](hkworkout/duration.md)
  The workout’s duration.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkout/totalswimmingstrokecount)*