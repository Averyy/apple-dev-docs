# totalSwimmingStrokeCount

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The total stroke count for the workout.

**Availability**:
- iOS 10.0+ - Deprecated in 18.0
- iPadOS 10.0+ - Deprecated in 18.0
- Mac Catalyst 13.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 3.0+ - Deprecated in 11.0

> **Deprecated**: Use [`allStatistics`](./allstatistics.md) or [`statistics(for:)`](./statistics%28for%29.md)  instead.

## Declaration

```swift
var totalSwimmingStrokeCount: HKQuantity? { get }
```

```objc
@property (strong, readonly, nullable) HKQuantity * totalSwimmingStrokeCount;
```

#### Discussion

This property contains a quantity using count units, or `nil`.

> **Note**:  Provide a total stroke count value whenever the stroke count is relevant to the workout type. In addition, add stroke count samples to a workout using the [`add(_:to:completion:)`](../hkhealthstore/add%28_,to,completion%29.md) method. These samples should sum up to the total stroke count, while providing detailed information about how the intensity changes over the duration of the workout.

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
- [var totalDistance: HKQuantity?](./totaldistance.md)
  The total distance traveled during the workout.
- [var totalEnergyBurned: HKQuantity?](./totalenergyburned.md)
  The total active energy burned during the workout.
- [var totalFlightsClimbed: HKQuantity?](./totalflightsclimbed.md)
  The total number of flights of stairs climbed during the workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkout/totalswimmingstrokecount)*