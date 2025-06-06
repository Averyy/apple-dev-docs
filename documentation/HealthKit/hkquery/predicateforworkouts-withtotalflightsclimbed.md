# predicateForWorkouts(with:totalFlightsClimbed:)

**Framework**: HealthKit  
**Kind**: method

Returns a predicate that matches workout samples based on the number of flights climbed.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalFlightsClimbed: HKQuantity) -> NSPredicate
```

#### Return Value

A predicate that matches workouts based on the number of flights climbed.

#### Discussion

This convenience method creates a predicate that compares the total flights climbed during a workout with a target number of flights climbed. The following sample uses the convenience method and a predicate format string to create equivalent predicates.

```swift
let flightsClimbed = HKQuantity(unit: HKUnit.count(), doubleValue: 10.0)
let tenFlightsClimbed = HKQuery.predicateForWorkouts(with: .greaterThanOrEqualTo, totalFlightsClimbed: flightsClimbed)

// Creating a predicate using a predicate format string.
let explicitTenFlightsClimbed = NSPredicate(format: "%K >= %@",
                                            HKPredicateKeyPathWorkoutTotalFlightsClimbed,
                                            flightsClimbed)
```

## Parameters

- `operatorType`: The operator to use when comparing the sample to the target number of flights climbed.
- `totalFlightsClimbed`: A quantity representing the target number of flights climbed.

## See Also

- [let HKPredicateKeyPathWorkoutTotalFlightsClimbed: String](hkpredicatekeypathworkouttotalflightsclimbed.md)
  The key path for accessing the total number of flights of stairs climbed during the workout.
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
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, totalSwimmingStrokeCount: HKQuantity) -> NSPredicate](hkquery/predicateforworkouts(with:totalswimmingstrokecount:).md)
  Returns a predicate that matches workout samples based on the number of strokes while swimming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforworkouts(with:totalflightsclimbed:))*