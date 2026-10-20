# HKPredicateKeyPathWorkoutTotalEnergyBurned

**Framework**: HealthKit  
**Kind**: var  
**Role**: Global Variable

The key path for accessing the workout’s total energy burned.

**Availability**:
- iOS 8.0+ - Deprecated in 18.0
- iPadOS 8.0+ - Deprecated in 18.0
- Mac Catalyst 13.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 2.0+ - Deprecated in 11.0

> **Deprecated**: Use predicateForWorkoutActivitiesWithOperatorType:quantityType:sumQuantity: passing the HKQuantityType for HKQuantityTypeIdentifierActiveEnergyBurned

## Declaration

```swift
let HKPredicateKeyPathWorkoutTotalEnergyBurned: String
```

```c
extern NSString * const HKPredicateKeyPathWorkoutTotalEnergyBurned;
```

## See Also

### Specifying predicate key paths
- [let HKPredicateKeyPathWorkoutType: String](./hkpredicatekeypathworkouttype.md)
  The key path for accessing the workout’s type.
- [let HKPredicateKeyPathWorkoutDuration: String](./hkpredicatekeypathworkoutduration.md)
  The key path for accessing the workout’s duration.
- [let HKPredicateKeyPathWorkoutTotalDistance: String](./hkpredicatekeypathworkouttotaldistance.md)
  The key path for accessing the workout’s total distance.
- [let HKPredicateKeyPathWorkoutAverageQuantity: String](./hkpredicatekeypathworkoutaveragequantity.md)
  The key path for accessing workouts with a matching average quantity.
- [let HKPredicateKeyPathWorkoutMaximumQuantity: String](./hkpredicatekeypathworkoutmaximumquantity.md)
  The key path for accessing workouts with a matching maximum quantity.
- [let HKPredicateKeyPathWorkoutMinimumQuantity: String](./hkpredicatekeypathworkoutminimumquantity.md)
  The key path for accessing workouts with a matching minimum quantity.
- [let HKPredicateKeyPathWorkoutSumQuantity: String](./hkpredicatekeypathworkoutsumquantity.md)
  The key path for accessing workouts with a matching sum.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkpredicatekeypathworkouttotalenergyburned)*