# workoutEvents

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly, nullable) NSArray<HKWorkoutEvent *> * workoutEvents;
```

#### Discussion

This array specifies when the user has paused and resumed the workout activity. This method calculates the workout’s duration based on the amount of active time between the provided start and end dates. For more information on workout events, see [`HKWorkoutEvent`](../hkworkoutevent.md).

## See Also

### Accessing workout data
- [var duration: TimeInterval](./duration.md)
  The workout’s duration.
- [var workoutActivityType: HKWorkoutActivityType](./workoutactivitytype.md)
  The type of activity performed during the workout.
- [var workoutActivities: [HKWorkoutActivity]](./workoutactivities.md)
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
- [var totalSwimmingStrokeCount: HKQuantity?](./totalswimmingstrokecount.md)
  The total stroke count for the workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkout/workoutevents)*