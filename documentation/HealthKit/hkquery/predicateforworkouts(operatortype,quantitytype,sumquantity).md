# predicateForWorkouts(operatorType:quantityType:sumQuantity:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a predicate for matching workout activities based the sum of an associated quantity type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class func predicateForWorkouts(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, sumQuantity: HKQuantity) -> NSPredicate
```

```objc
+ (NSPredicate *) predicateForWorkoutsWithOperatorType:(NSPredicateOperatorType) operatorType quantityType:(HKQuantityType *) quantityType sumQuantity:(HKQuantity *) sumQuantity;
```

#### Discussion

Use this convenience method to create a predicate that matches workouts with the specified total value. For more information on how HealthKit calculates statistics for [`HKWorkoutActivity`](../hkworkoutactivity.md) objects, see [`statistics(for:)`](../hkworkoutactivity/statistics%28for%29.md).

The following sample creates a predicate for workout activities with a total step count of 1000 or higher.

```swift
let quantityType = HKQuantityType(.stepCount)

let expectedQuantity = HKQuantity(unit: .count(),
                                  doubleValue: 1000.0)

let stepCountPredicate = HKQuery.predicateForWorkouts(
    operatorType: .greaterThanOrEqualTo,
    quantityType: quantityType,
    sumQuantity: expectedQuantity)
```

## Parameters

- `operatorType`: The operator type to use when comparing the sum.
- `quantityType`: The type of [`HKQuantitySample`](../hkquantitysample.md) objects used to calculate the sum.
- `sumQuantity`: The target value for the sum.

## See Also

### Creating workout predicates
- [class func predicateForObjects(from: HKWorkout) -> NSPredicate](./predicateforobjects%28from%29-5irg9.md)
  Returns a predicate that matches any objects that have been associated with the provided workout.
- [class func predicateForWorkouts(with: HKWorkoutActivityType) -> NSPredicate](./predicateforworkouts%28with%29.md)
  Returns a predicate for matching workouts based on the type of activity.
- [class func predicateForWorkouts(activityPredicate: NSPredicate) -> NSPredicate](./predicateforworkouts%28activitypredicate%29.md)
  Returns a predicate for matching workouts based on the associated workout activities.
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, duration: TimeInterval) -> NSPredicate](./predicateforworkouts%28with,duration%29.md)
  Returns a predicate for matching workouts based on their duration.
- [class func predicateForWorkouts(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, averageQuantity: HKQuantity) -> NSPredicate](./predicateforworkouts%28operatortype,quantitytype,averagequantity%29.md)
  Returns a predicate for matching workouts based the average value of an associated quantity type.
- [class func predicateForWorkouts(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, maximumQuantity: HKQuantity) -> NSPredicate](./predicateforworkouts%28operatortype,quantitytype,maximumquantity%29.md)
  Returns a predicate for matching workout activities based the maximum value of an associated quantity type.
- [class func predicateForWorkouts(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, minimumQuantity: HKQuantity) -> NSPredicate](./predicateforworkouts%28operatortype,quantitytype,minimumquantity%29.md)
  Returns a predicate for matching workout activities based the minimum value of an associated quantity type.
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, totalDistance: HKQuantity) -> NSPredicate](./predicateforworkouts%28with,totaldistance%29.md)
  Returns a predicate for matching workouts based on the total distance traveled.
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, totalEnergyBurned: HKQuantity) -> NSPredicate](./predicateforworkouts%28with,totalenergyburned%29.md)
  Returns a predicate for matching workouts based on the total energy burned.
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, totalFlightsClimbed: HKQuantity) -> NSPredicate](./predicateforworkouts%28with,totalflightsclimbed%29.md)
  Returns a predicate that matches workout samples based on the number of flights climbed.
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, totalSwimmingStrokeCount: HKQuantity) -> NSPredicate](./predicateforworkouts%28with,totalswimmingstrokecount%29.md)
  Returns a predicate that matches workout samples based on the number of strokes while swimming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforworkouts(operatortype:quantitytype:sumquantity:))*