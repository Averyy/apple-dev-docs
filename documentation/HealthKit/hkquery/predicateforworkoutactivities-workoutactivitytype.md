# predicateForWorkoutActivities(workoutActivityType:)

**Framework**: HealthKit  
**Kind**: method

Returns a predicate for workout activities based on the type of activity performed.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class func predicateForWorkoutActivities(workoutActivityType: HKWorkoutActivityType) -> NSPredicate
```

## Mentions

- [Dividing a HealthKit workout into activities](dividing-a-healthkit-workout-into-activities.md)

#### Discussion

To use this predicate, call [`predicateForWorkouts(activityPredicate:)`](hkquery/predicateforworkouts(activitypredicate:).md) to wrap this predicate inside a workout predicate. You can then use the workout predicate in your query.

The following example creates a predicate that matches workout activities with a [`HKWorkoutActivityType.running`](hkworkoutactivitytype/running.md) type.

```swift
let runningActivityPredicate =
HKQuery.predicateForWorkoutActivities(workoutActivityType: .running)

let workoutPredicate =
HKQuery.predicateForWorkouts(activityPredicate: runningActivityPredicate)
```

## Parameters

- `workoutActivityType`: The type of activity. For a list of valid workout activities, see  .

## See Also

- [class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, duration: TimeInterval) -> NSPredicate](hkquery/predicateforworkoutactivities(operatortype:duration:).md)
  Returns a predicate for matching workout activities based on their duration.
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforworkoutactivities(workoutactivitytype:))*