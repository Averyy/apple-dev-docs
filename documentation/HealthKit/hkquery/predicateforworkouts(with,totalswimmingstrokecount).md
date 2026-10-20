# predicateForWorkouts(with:totalSwimmingStrokeCount:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a predicate that matches workout samples based on the number of strokes while swimming.

**Availability**:
- iOS 10.0+ - Deprecated in 18.0
- iPadOS 10.0+ - Deprecated in 18.0
- Mac Catalyst 13.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 3.0+ - Deprecated in 11.0

> **Deprecated**: Use predicateForWorkoutsWithOperatorType:quantityType:sumQuantity: passing the HKQuantityType for HKQuantityTypeIdentifierSwimmingStrokeCount

## Declaration

```swift
class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalSwimmingStrokeCount: HKQuantity) -> NSPredicate
```

```objc
+ (NSPredicate *) predicateForWorkoutsWithOperatorType:(NSPredicateOperatorType) operatorType totalSwimmingStrokeCount:(HKQuantity *) totalSwimmingStrokeCount;
```

#### Return Value

A predicate that matches workouts based on the number of strokes while swimming.

#### Discussion

This convenience method creates a predicate that compares the number of swimming strokes during a workout with a target number. The following sample uses the convenience method and a predicate format string to create equivalent predicates.

```swift
// Creating a predicate using the convenience method.
let swimmingStrokeCount = HKQuantity(unit: HKUnit.count(), doubleValue: 500.0)
let longSwim = HKQuery.predicateForWorkouts(with: .greaterThanOrEqualTo, totalSwimmingStrokeCount: swimmingStrokeCount)

// Creating a predicate using a predicate format string.
let explicitLongSwim = NSPredicate(format: "%K >= %@",
                                   HKPredicateKeyPathWorkoutTotalSwimmingStrokeCount,
                                   swimmingStrokeCount)
```

## Parameters

- `operatorType`: The operator to use when comparing the sample to the target number of flights climbed.
- `totalSwimmingStrokeCount`: A quantity representing the target stroke count.

## See Also

### Related Documentation
- [let HKPredicateKeyPathWorkoutTotalSwimmingStrokeCount: String](../hkpredicatekeypathworkouttotalswimmingstrokecount.md)
  The key path for accessing the number of strokes during a swimming workout.
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
- [class func predicateForWorkouts(operatorType: NSComparisonPredicate.Operator, quantityType: HKQuantityType, sumQuantity: HKQuantity) -> NSPredicate](./predicateforworkouts%28operatortype,quantitytype,sumquantity%29.md)
  Returns a predicate for matching workout activities based the sum of an associated quantity type.
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, totalDistance: HKQuantity) -> NSPredicate](./predicateforworkouts%28with,totaldistance%29.md)
  Returns a predicate for matching workouts based on the total distance traveled.
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, totalEnergyBurned: HKQuantity) -> NSPredicate](./predicateforworkouts%28with,totalenergyburned%29.md)
  Returns a predicate for matching workouts based on the total energy burned.
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, totalFlightsClimbed: HKQuantity) -> NSPredicate](./predicateforworkouts%28with,totalflightsclimbed%29.md)
  Returns a predicate that matches workout samples based on the number of flights climbed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforworkouts(with:totalswimmingstrokecount:))*