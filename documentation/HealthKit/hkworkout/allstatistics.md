# allStatistics

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

A dictionary that contains all the statistics for the workout.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var allStatistics: [HKQuantityType : HKStatistics] { get }
```

```objc
@property (copy, readonly) NSDictionary<HKQuantityType *,HKStatistics *> * allStatistics;
```

## Discussion

HealthKit calculates an [`HKStatistics`](../hkstatistics.md) object for each [`HKQuantityType`](../hkquantitytype.md), based on the [`HKQuantitySample`](../hkquantitysample.md) objects associated with the containing workout.

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
- [var totalDistance: HKQuantity?](./totaldistance.md)
  The total distance traveled during the workout.
- [var totalEnergyBurned: HKQuantity?](./totalenergyburned.md)
  The total active energy burned during the workout.
- [var totalFlightsClimbed: HKQuantity?](./totalflightsclimbed.md)
  The total number of flights of stairs climbed during the workout.
- [var totalSwimmingStrokeCount: HKQuantity?](./totalswimmingstrokecount.md)
  The total stroke count for the workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkout/allstatistics)*