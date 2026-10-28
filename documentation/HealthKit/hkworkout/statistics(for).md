# statistics(for:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Returns the workout’s statistics for the provided quantity type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func statistics(for quantityType: HKQuantityType) -> HKStatistics?
```

```objc
- (HKStatistics *) statisticsForType:(HKQuantityType *) quantityType;
```

## Discussion

HealthKit calculates an [`HKStatistics`](../hkstatistics.md) object based on the [`HKQuantitySample`](../hkquantitysample.md) objects associated with the workout that also match the specified [`HKQuantityType`](../hkquantitytype.md).

If there are no matching quantity values, this method returns `nil`.

## Parameters

- `quantityType`: The type of [`HKQuantitySample`](../hkquantitysample.md) objects used to calculate the statistics.

## See Also

### Accessing workout data
- [var duration: TimeInterval](./duration.md)
  The workout’s duration.
- [var workoutActivityType: HKWorkoutActivityType](./workoutactivitytype.md)
  The type of activity performed during the workout.
- [var workoutActivities: [HKWorkoutActivity]](./workoutactivities.md)
- [var workoutEvents: [HKWorkoutEvent]?](./workoutevents.md)
  An array of workout event objects.
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkout/statistics(for:))*