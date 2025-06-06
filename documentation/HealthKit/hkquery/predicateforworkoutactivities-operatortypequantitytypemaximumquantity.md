# predicateForWorkoutActivities(operatorType:quantityType:maximumQuantity:)

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
class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, maximumQuantity: HKQuantity) -> NSPredicate
```

#### Discussion

Use this convenience method to create a predicate that matches workout activities with the specified maximum quantity. To use this predicate, call [`predicateForWorkouts(activityPredicate:)`](hkquery/predicateforworkouts(activitypredicate:).md) to wrap this predicate inside a workout predicate. You can then use the workout predicate in your query.

The following sample creates a predicate for workout activities with a maximum heart rate of 150 bmp or higher.

```swift
let quantityType = HKQuantityType(.heartRate)

let expectedQuantity =
HKQuantity(unit: .count().unitDivided(by: .minute()),
           doubleValue: 150.0)

let heartRatePredicate =
HKQuery.predicateForWorkoutActivities(
    operatorType: .greaterThanOrEqualTo,
    quantityType: quantityType,
    maximumQuantity:
        expectedQuantity
)

// Wrap the activity predicate inside a workout predicate.
let workoutPredicate = HKQuery.predicateForWorkouts(activityPredicate: heartRatePredicate)
```

For more information on how HealthKit calculates statistics for [`HKWorkoutActivity`](hkworkoutactivity.md) objects, see [`statistics(for:)`](hkworkoutactivity/statistics(for:).md).

## Parameters

- `operatorType`: The operator type to use when comparing the maximum quantity.
- `quantityType`: The type of   objects used to calculate the maximum quantity.
- `maximumQuantity`: The target value for the maximum quantity.

## See Also

- [class func predicateForWorkoutActivities(workoutActivityType: HKWorkoutActivityType) -> NSPredicate](hkquery/predicateforworkoutactivities(workoutactivitytype:).md)
  Returns a predicate for workout activities based on the type of activity performed.
- [class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, duration: TimeInterval) -> NSPredicate](hkquery/predicateforworkoutactivities(operatortype:duration:).md)
  Returns a predicate for matching workout activities based on their duration.
- [class func predicateForWorkoutActivities(start: Date?, end: Date?, options: HKQueryOptions) -> NSPredicate](hkquery/predicateforworkoutactivities(start:end:options:).md)
  Returns a predicate for workout activities that occur between the start and end date.
- [class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, averageQuantity: HKQuantity) -> NSPredicate](hkquery/predicateforworkoutactivities(operatortype:quantitytype:averagequantity:).md)
  Returns a predicate for matching workout activities based the average value of an associated quantity type.
- [class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, minimumQuantity: HKQuantity) -> NSPredicate](hkquery/predicateforworkoutactivities(operatortype:quantitytype:minimumquantity:).md)
  Returns a predicate for matching workout activities based the minimum value of an associated quantity type.
- [class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, sumQuantity: HKQuantity) -> NSPredicate](hkquery/predicateforworkoutactivities(operatortype:quantitytype:sumquantity:).md)
  Returns a predicate for matching workout activities based the sum of an associated quantity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforworkoutactivities(operatortype:quantitytype:maximumquantity:))*