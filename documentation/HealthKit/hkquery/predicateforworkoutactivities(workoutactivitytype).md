# predicateForWorkoutActivities(workoutActivityType:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NSPredicate *) predicateForWorkoutActivitiesWithWorkoutActivityType:(HKWorkoutActivityType) workoutActivityType;
```

## Mentions

- [Dividing a HealthKit workout into activities](../dividing-a-healthkit-workout-into-activities.md)

## Discussion

To use this predicate, call [`predicateForWorkouts(activityPredicate:)`](./predicateforworkouts%28activitypredicate%29.md) to wrap this predicate inside a workout predicate. You can then use the workout predicate in your query.

The following example creates a predicate that matches workout activities with a [`HKWorkoutActivityType.running`](../hkworkoutactivitytype/running.md) type.

```swift
let runningActivityPredicate =
HKQuery.predicateForWorkoutActivities(workoutActivityType: .running)

let workoutPredicate =
HKQuery.predicateForWorkouts(activityPredicate: runningActivityPredicate)
```

## Parameters

- `workoutActivityType`: The type of activity. For a list of valid workout activities, see [`HKWorkoutActivityType`](../hkworkoutactivitytype.md).

## See Also

### Creating workout activity predicates
- [class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, duration: TimeInterval) -> NSPredicate](./predicateforworkoutactivities%28operatortype,duration%29.md)
  Returns a predicate for matching workout activities based on their duration.
- [class func predicateForWorkoutActivities(start: Date?, end: Date?, options: HKQueryOptions) -> NSPredicate](./predicateforworkoutactivities%28start,end,options%29.md)
  Returns a predicate for workout activities that occur between the start and end date.
- [class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, averageQuantity: HKQuantity) -> NSPredicate](./predicateforworkoutactivities%28operatortype,quantitytype,averagequantity%29.md)
  Returns a predicate for matching workout activities based the average value of an associated quantity type.
- [class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, maximumQuantity: HKQuantity) -> NSPredicate](./predicateforworkoutactivities%28operatortype,quantitytype,maximumquantity%29.md)
  Returns a predicate for matching workout activities based the maximum value of an associated quantity type.
- [class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, minimumQuantity: HKQuantity) -> NSPredicate](./predicateforworkoutactivities%28operatortype,quantitytype,minimumquantity%29.md)
  Returns a predicate for matching workout activities based the minimum value of an associated quantity type.
- [class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, sumQuantity: HKQuantity) -> NSPredicate](./predicateforworkoutactivities%28operatortype,quantitytype,sumquantity%29.md)
  Returns a predicate for matching workout activities based the sum of an associated quantity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforworkoutactivities(workoutactivitytype:))*