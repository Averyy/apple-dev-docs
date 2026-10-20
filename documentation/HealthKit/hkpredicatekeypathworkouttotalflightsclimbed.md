# HKPredicateKeyPathWorkoutTotalFlightsClimbed

**Framework**: HealthKit  
**Kind**: var  
**Role**: Global Variable

The key path for accessing the total number of flights of stairs climbed during the workout.

**Availability**:
- iOS 11.0+ - Deprecated in 18.0
- iPadOS 11.0+ - Deprecated in 18.0
- Mac Catalyst 13.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 4.0+ - Deprecated in 11.0

> **Deprecated**: Use predicateForWorkoutActivitiesWithOperatorType:quantityType:sumQuantity: passing the HKQuantityType for HKQuantityTypeIdentifierFlightsClimbed

## Declaration

```swift
let HKPredicateKeyPathWorkoutTotalFlightsClimbed: String
```

```c
extern NSString * const HKPredicateKeyPathWorkoutTotalFlightsClimbed;
```

## See Also

### Workout keys
- [let HKPredicateKeyPathWorkout: String](./hkpredicatekeypathworkout.md)
  The key path for accessing the object’s workout inside a predicate format string.
- [let HKPredicateKeyPathWorkoutType: String](./hkpredicatekeypathworkouttype.md)
  The key path for accessing the workout’s type.
- [let HKPredicateKeyPathWorkoutDuration: String](./hkpredicatekeypathworkoutduration.md)
  The key path for accessing the workout’s duration.
- [let HKPredicateKeyPathWorkoutAverageQuantity: String](./hkpredicatekeypathworkoutaveragequantity.md)
  The key path for accessing workouts with a matching average quantity.
- [let HKPredicateKeyPathWorkoutMaximumQuantity: String](./hkpredicatekeypathworkoutmaximumquantity.md)
  The key path for accessing workouts with a matching maximum quantity.
- [let HKPredicateKeyPathWorkoutMinimumQuantity: String](./hkpredicatekeypathworkoutminimumquantity.md)
  The key path for accessing workouts with a matching minimum quantity.
- [let HKPredicateKeyPathWorkoutSumQuantity: String](./hkpredicatekeypathworkoutsumquantity.md)
  The key path for accessing workouts with a matching sum.
- [let HKPredicateKeyPathWorkoutTotalDistance: String](./hkpredicatekeypathworkouttotaldistance.md)
  The key path for accessing the workout’s total distance.
- [let HKPredicateKeyPathWorkoutTotalEnergyBurned: String](./hkpredicatekeypathworkouttotalenergyburned.md)
  The key path for accessing the workout’s total energy burned.
- [let HKPredicateKeyPathWorkoutTotalSwimmingStrokeCount: String](./hkpredicatekeypathworkouttotalswimmingstrokecount.md)
  The key path for accessing the number of strokes during a swimming workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkpredicatekeypathworkouttotalflightsclimbed)*