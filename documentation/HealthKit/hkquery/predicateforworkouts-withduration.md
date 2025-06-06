# predicateForWorkouts(with:duration:)

**Framework**: HealthKit  
**Kind**: method

Returns a predicate for matching workouts based on their duration.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, duration: TimeInterval) -> NSPredicate
```

#### Return Value

A predicate for matching workouts based on their duration. This predicate works only on workouts.

#### Discussion

Use this convenience method to create a predicate that matches against a workout’s duration. The following sample uses both the convenience method and a predicate format string to create equivalent predicates.

## Parameters

- `operatorType`: The operator type to use when comparing the duration.
- `duration`: The target duration.

## See Also

- [let HKPredicateKeyPathWorkoutDuration: String](hkpredicatekeypathworkoutduration.md)
  The key path for accessing the workout’s duration.
- [var duration: TimeInterval](hkworkout/duration.md)
  The workout’s duration.
- [class func predicateForObjects(from: HKWorkout) -> NSPredicate](hkquery/predicateforobjects(from:)-5irg9.md)
  Returns a predicate that matches any objects that have been associated with the provided workout.
- [class func predicateForWorkouts(with: HKWorkoutActivityType) -> NSPredicate](hkquery/predicateforworkouts(with:).md)
  Returns a predicate for matching workouts based on the type of activity.
- [class func predicateForWorkouts(activityPredicate: NSPredicate) -> NSPredicate](hkquery/predicateforworkouts(activitypredicate:).md)
  Returns a predicate for matching workouts based on the associated workout activities.
- [class func predicateForWorkouts(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, averageQuantity: HKQuantity) -> NSPredicate](hkquery/predicateforworkouts(operatortype:quantitytype:averagequantity:).md)
  Returns a predicate for matching workouts based the average value of an associated quantity type.
- [class func predicateForWorkouts(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, maximumQuantity: HKQuantity) -> NSPredicate](hkquery/predicateforworkouts(operatortype:quantitytype:maximumquantity:).md)
  Returns a predicate for matching workout activities based the maximum value of an associated quantity type.
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforworkouts(with:duration:))*