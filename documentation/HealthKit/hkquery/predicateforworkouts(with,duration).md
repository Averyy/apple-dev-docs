# predicateForWorkouts(with:duration:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a predicate for matching workouts based on their duration.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, duration: TimeInterval) -> NSPredicate
```

```objc
+ (NSPredicate *) predicateForWorkoutsWithOperatorType:(NSPredicateOperatorType) operatorType duration:(NSTimeInterval) duration;
```

#### Return Value

A predicate for matching workouts based on their duration. This predicate works only on workouts.

#### Discussion

Use this convenience method to create a predicate that matches against a workout’s duration. The following sample uses both the convenience method and a predicate format string to create equivalent predicates.

**Swift**:

```swift
// Predicate matching workouts equal to or longer than 30 minutes
let workout = HKQuery.predicateForWorkoutsWithOperatorType(
    .GreaterThanOrEqualToPredicateOperatorType,
    duration: 60.0 * 30.0)
 
 
let explicitWorkout = NSPredicate(format: "%K >= %d",
                                  HKPredicateKeyPathWorkoutDuration, 60 * 30)
```

**Objective-C**:

```objc
// Predicate matching workouts equal to or longer than 30 minutes
NSPredicate *workout =
    [HKQuery predicateForWorkoutsWithOperatorType:
 
     NSGreaterThanOrEqualToPredicateOperatorType
      duration:60.0 * 30.0];
 
NSPredicate *explicitWorkout =
[NSPredicate predicateWithFormat:@"%K >= %d",
 HKPredicateKeyPathWorkoutDuration,
 60 * 30];
```

## Parameters

- `operatorType`: The operator type to use when comparing the duration.
- `duration`: The target duration.

## See Also

### Related Documentation
- [let HKPredicateKeyPathWorkoutDuration: String](../hkpredicatekeypathworkoutduration.md)
  The key path for accessing the workout’s duration.
- [var duration: TimeInterval](../hkworkout/duration.md)
  The workout’s duration.
### Creating workout predicates
- [class func predicateForObjects(from: HKWorkout) -> NSPredicate](./predicateforobjects%28from%29-5irg9.md)
  Returns a predicate that matches any objects that have been associated with the provided workout.
- [class func predicateForWorkouts(with: HKWorkoutActivityType) -> NSPredicate](./predicateforworkouts%28with%29.md)
  Returns a predicate for matching workouts based on the type of activity.
- [class func predicateForWorkouts(activityPredicate: NSPredicate) -> NSPredicate](./predicateforworkouts%28activitypredicate%29.md)
  Returns a predicate for matching workouts based on the associated workout activities.
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
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, totalSwimmingStrokeCount: HKQuantity) -> NSPredicate](./predicateforworkouts%28with,totalswimmingstrokecount%29.md)
  Returns a predicate that matches workout samples based on the number of strokes while swimming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforworkouts(with:duration:))*