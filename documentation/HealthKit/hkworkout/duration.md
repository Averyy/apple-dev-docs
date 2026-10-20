# duration

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (assign, readonly) NSTimeInterval duration;
```

## Mentions

- [Adding samples to a workout](../adding-samples-to-a-workout.md)

#### Discussion

A workout’s duration can be specified in one of three ways. The [`init(activityType:start:end:)`](./init%28activitytype,start,end%29.md) method uses the time interval between the provided start and end dates. The [`init(activityType:start:end:duration:totalEnergyBurned:totalDistance:metadata:)`](./init%28activitytype,start,end,duration,totalenergyburned,totaldistance,metadata%29.md) method sets the duration to the provided value. And the [`init(activityType:start:end:workoutEvents:totalEnergyBurned:totalDistance:metadata:)`](./init%28activitytype,start,end,workoutevents,totalenergyburned,totaldistance,metadata%29.md) method calculates the total active duration based on the start and end dates and the workout events.

## See Also

### Accessing workout data
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
- [var totalSwimmingStrokeCount: HKQuantity?](./totalswimmingstrokecount.md)
  The total stroke count for the workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkout/duration)*