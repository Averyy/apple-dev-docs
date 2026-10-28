# totalDistance

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The total distance traveled during the workout.

**Availability**:
- iOS 8.0+ - Deprecated in 27.2
- iPadOS 8.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [`allStatistics`](./allstatistics.md) or [`statistics(for:)`](./statistics%28for%29.md)  instead.

## Declaration

```swift
var totalDistance: HKQuantity? { get }
```

```objc
@property (strong, readonly, nullable) HKQuantity * totalDistance;
```

## Mentions

- [Adding samples to a workout](../adding-samples-to-a-workout.md)

## Discussion

This property contains a quantity using length units, or `nil`.

> **Note**:  Provide a total distance value whenever the distance traveled is relevant to the workout type. In addition, add distance samples to a workout using the [`add(_:to:completion:)`](../hkhealthstore/add%28_,to,completion%29.md) method. These samples should sum up to the total distance, while providing detailed information about how the intensity changes over the duration of the workout.

## See Also

### Accessing workout data
- [var duration: TimeInterval](./duration.md)
  The workout’s duration.
- [var workoutActivityType: HKWorkoutActivityType](./workoutactivitytype.md)
  The type of activity performed during the workout.
- [var workoutActivities: [HKWorkoutActivity]](./workoutactivities.md)
- [var workoutEvents: [HKWorkoutEvent]?](./workoutevents.md)
  An array of workout event objects.
- [func statistics(for: HKQuantityType) -> HKStatistics?](./statistics%28for%29.md)
  Returns the workout’s statistics for the provided quantity type.
- [var allStatistics: [HKQuantityType : HKStatistics]](./allstatistics.md)
  A dictionary that contains all the statistics for the workout.
- [var totalEnergyBurned: HKQuantity?](./totalenergyburned.md)
  The total active energy burned during the workout.
- [var totalFlightsClimbed: HKQuantity?](./totalflightsclimbed.md)
  The total number of flights of stairs climbed during the workout.
- [var totalSwimmingStrokeCount: HKQuantity?](./totalswimmingstrokecount.md)
  The total stroke count for the workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkout/totaldistance)*