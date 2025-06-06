# predicateForWorkoutActivities(operatorType:duration:)

**Framework**: HealthKit  
**Kind**: method

Returns a predicate for matching workout activities based on their duration.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, duration: TimeInterval) -> NSPredicate
```

#### Return Value

A predicate for matching workout activities based on their duration. This predicate works only on workout activities.

#### Discussion

Use this convenience method to create a predicate that matches against an activity’s duration. To use this predicate, call [`predicateForWorkouts(activityPredicate:)`](hkquery/predicateforworkouts(activitypredicate:).md) to wrap this predicate inside a workout predicate. You can then use the workout predicate in your query.

The following sample creates a predicate for matching workout activities with a duration of 30 minutes or longer.

```swift
let longWorkoutActivityPredicate = HKQuery.predicateForWorkoutActivities(operatorType: .greaterThanOrEqualTo, duration: 60.0 * 30.0)


// Wrap the activity predicate inside a workout predicate.
let workoutPredicate = HKQuery.predicateForWorkouts(activityPredicate: longWorkoutActivityPredicate)
```

## Parameters

- `operatorType`: The operator type to use when comparing the duration.
- `duration`: The target duration.

## See Also

- [let HKPredicateKeyPathWorkoutDuration: String](hkpredicatekeypathworkoutduration.md)
  The key path for accessing the workout’s duration.
- [var duration: TimeInterval](hkworkout/duration.md)
  The workout’s duration.
- [class func predicateForWorkoutActivities(workoutActivityType: HKWorkoutActivityType) -> NSPredicate](hkquery/predicateforworkoutactivities(workoutactivitytype:).md)
  Returns a predicate for workout activities based on the type of activity performed.
- [class func predicateForWorkoutActivities(start: Date?, end: Date?, options: HKQueryOptions) -> NSPredicate](hkquery/predicateforworkoutactivities(start:end:options:).md)
  Returns a predicate for workout activities that occur between the start and end date.
- [class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, averageQuantity: HKQuantity) -> NSPredicate](hkquery/predicateforworkoutactivities(operatortype:quantitytype:averagequantity:).md)
  Returns a predicate for matching workout activities based the average value of an associated quantity type.
- [class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, maximumQuantity: HKQuantity) -> NSPredicate](hkquery/predicateforworkoutactivities(operatortype:quantitytype:maximumquantity:).md)
  Returns a predicate for matching workout activities based the maximum value of an associated quantity type.
- [class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, minimumQuantity: HKQuantity) -> NSPredicate](hkquery/predicateforworkoutactivities(operatortype:quantitytype:minimumquantity:).md)
  Returns a predicate for matching workout activities based the minimum value of an associated quantity type.
- [class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, sumQuantity: HKQuantity) -> NSPredicate](hkquery/predicateforworkoutactivities(operatortype:quantitytype:sumquantity:).md)
  Returns a predicate for matching workout activities based the sum of an associated quantity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforworkoutactivities(operatortype:duration:))*