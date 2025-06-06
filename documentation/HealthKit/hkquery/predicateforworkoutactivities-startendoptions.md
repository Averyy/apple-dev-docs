# predicateForWorkoutActivities(start:end:options:)

**Framework**: HealthKit  
**Kind**: method

Returns a predicate for workout activities that occur between the start and end date.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class func predicateForWorkoutActivities(start startDate: Date?, end endDate: Date?, options: HKQueryOptions = []) -> NSPredicate
```

#### Discussion

Use this convenience method to create a predicate that matches workout activities that occur between the specified start and end dates. To use this predicate, call [`predicateForWorkouts(activityPredicate:)`](hkquery/predicateforworkouts(activitypredicate:).md) to wrap this predicate inside a workout predicate. You can then use the workout predicate in your query.

The following sample creates a predicate for workout activities within the last 30 minutes.

```swift
let end = Date()
let start = end.advanced(by: -30.0 * 60.0)

let recentActivityPredicate =
HKQuery.predicateForWorkoutActivities(start: start, end: end)

let workoutPredicate =
HKQuery.predicateForWorkouts(activityPredicate: recentActivityPredicate)
```

## Parameters

- `startDate`: The start date for the target time interval.
- `endDate`: The end date for the target time interval.
- `options`: A constant that specifies how HealthKit compares the sample’s start and end date with the target time interval. For a list of possible values, see  .

## See Also

- [class func predicateForWorkoutActivities(workoutActivityType: HKWorkoutActivityType) -> NSPredicate](hkquery/predicateforworkoutactivities(workoutactivitytype:).md)
  Returns a predicate for workout activities based on the type of activity performed.
- [class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, duration: TimeInterval) -> NSPredicate](hkquery/predicateforworkoutactivities(operatortype:duration:).md)
  Returns a predicate for matching workout activities based on their duration.
- [class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, averageQuantity: HKQuantity) -> NSPredicate](hkquery/predicateforworkoutactivities(operatortype:quantitytype:averagequantity:).md)
  Returns a predicate for matching workout activities based the average value of an associated quantity type.
- [class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, maximumQuantity: HKQuantity) -> NSPredicate](hkquery/predicateforworkoutactivities(operatortype:quantitytype:maximumquantity:).md)
  Returns a predicate for matching workout activities based the maximum value of an associated quantity type.
- [class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, minimumQuantity: HKQuantity) -> NSPredicate](hkquery/predicateforworkoutactivities(operatortype:quantitytype:minimumquantity:).md)
  Returns a predicate for matching workout activities based the minimum value of an associated quantity type.
- [class func predicateForWorkoutActivities(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, sumQuantity: HKQuantity) -> NSPredicate](hkquery/predicateforworkoutactivities(operatortype:quantitytype:sumquantity:).md)
  Returns a predicate for matching workout activities based the sum of an associated quantity type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforworkoutactivities(start:end:options:))*