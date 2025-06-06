# predicateForWorkouts(operatorType:quantityType:maximumQuantity:)

**Framework**: HealthKit  
**Kind**: method

Returns a predicate for matching workout activities based the maximum value of an associated quantity type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class func predicateForWorkouts(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, maximumQuantity: HKQuantity) -> NSPredicate
```

#### Discussion

Use this convenience method to create a predicate that matches workouts with the specified maximum quantity. For more information on how HealthKit calculates statistics for [`HKWorkoutActivity`](hkworkoutactivity.md) objects, see [`statistics(for:)`](hkworkoutactivity/statistics(for:).md).

The following sample creates a predicate for workout activities with a maximum heart rate of 150 bmp or higher.

```swift
let quantityType = HKQuantityType(.heartRate)

let expectedQuantity =
HKQuantity(unit: .count().unitDivided(by: .minute()),
           doubleValue: 150.0)

let heartRatePredicate = HKQuery.predicateForWorkouts(
    operatorType: .greaterThanOrEqualTo,
    quantityType: quantityType,
    maximumQuantity: expectedQuantity)
}
```

## Parameters

- `operatorType`: The operator type to use when comparing the maximum quantity.
- `quantityType`: The type of   objects used to calculate the maximum quantity.
- `maximumQuantity`: The target value for the maximum quantity.

## See Also

- [class func predicateForObjects(from: HKWorkout) -> NSPredicate](hkquery/predicateforobjects(from:)-5irg9.md)
  Returns a predicate that matches any objects that have been associated with the provided workout.
- [class func predicateForWorkouts(with: HKWorkoutActivityType) -> NSPredicate](hkquery/predicateforworkouts(with:).md)
  Returns a predicate for matching workouts based on the type of activity.
- [class func predicateForWorkouts(activityPredicate: NSPredicate) -> NSPredicate](hkquery/predicateforworkouts(activitypredicate:).md)
  Returns a predicate for matching workouts based on the associated workout activities.
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, duration: TimeInterval) -> NSPredicate](hkquery/predicateforworkouts(with:duration:).md)
  Returns a predicate for matching workouts based on their duration.
- [class func predicateForWorkouts(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, averageQuantity: HKQuantity) -> NSPredicate](hkquery/predicateforworkouts(operatortype:quantitytype:averagequantity:).md)
  Returns a predicate for matching workouts based the average value of an associated quantity type.
- [class func predicateForWorkouts(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, minimumQuantity: HKQuantity) -> NSPredicate](hkquery/predicateforworkouts(operatortype:quantitytype:minimumquantity:).md)
  Returns a predicate for matching workout activities based the minimum value of an associated quantity type.
- [class func predicateForWorkouts(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, sumQuantity: HKQuantity) -> NSPredicate](hkquery/predicateforworkouts(operatortype:quantitytype:sumquantity:).md)
  Returns a predicate for matching workout activities based the sum of an associated quantity type.
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, totalDistance: HKQuantity) -> NSPredicate](hkquery/predicateforworkouts(with:totaldistance:).md)
  Returns a predicate for matching workouts based on the total distance traveled.
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, totalEnergyBurned: HKQuantity) -> NSPredicate](hkquery/predicateforworkouts(with:totalenergyburned:).md)
  Returns a predicate for matching workouts based on the total energy burned.
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, totalFlightsClimbed: HKQuantity) -> NSPredicate](hkquery/predicateforworkouts(with:totalflightsclimbed:).md)
  Returns a predicate that matches workout samples based on the number of flights climbed.
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, totalSwimmingStrokeCount: HKQuantity) -> NSPredicate](hkquery/predicateforworkouts(with:totalswimmingstrokecount:).md)
  Returns a predicate that matches workout samples based on the number of strokes while swimming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforworkouts(operatortype:quantitytype:maximumquantity:))*