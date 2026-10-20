# predicateForWorkouts(with:totalDistance:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a predicate for matching workouts based on the total distance traveled.

**Availability**:
- iOS 8.0+ - Deprecated in 27.2
- iPadOS 8.0+ - Deprecated in 27.2
- Mac Catalyst 13.0+ - Deprecated in 27.2
- macOS 13.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use predicateForWorkoutsWithOperatorType:quantityType:sumQuantity: passing the HKQuantityType for the desired distance type

## Declaration

```swift
class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalDistance: HKQuantity) -> NSPredicate
```

```objc
+ (NSPredicate *) predicateForWorkoutsWithOperatorType:(NSPredicateOperatorType) operatorType totalDistance:(HKQuantity *) totalDistance;
```

#### Return Value

A predicate for matching workouts based on the total distance traveled. This predicate works only on workouts.

#### Discussion

Use this convenience method to create a predicate that matches against a workout’s total distance. The following sample uses both the convenience method and a predicate format string to create equivalent predicates.

**Swift**:

```swift
// Predicate matching workouts covering 6.5 miles or more.
let distance = HKQuantity(unit: HKUnit.mileUnit(), doubleValue: 6.5)
let workout = HKQuery.predicateForWorkoutsWithOperatorType(
    .GreaterThanOrEqualToPredicateOperatorType,
    totalDistance: distance)
 
 
let explicitWorkout = NSPredicate(format: "%K >= %@",
                                  HKPredicateKeyPathWorkoutTotalDistance, distance)
```

**Objective-C**:

```objc
// Predicate matching workouts covering 6.5 miles or more.
HKQuantity *distance =
    [HKQuantity quantityWithUnit:[HKUnit mileUnit] doubleValue:6.5];
 
NSPredicate *workout =
    [HKQuery predicateForWorkoutsWithOperatorType:
     NSGreaterThanOrEqualToPredicateOperatorType
     totalDistance:distance];
 
NSPredicate *explicitWorkout =
[NSPredicate predicateWithFormat:@"%K >= %@",
 HKPredicateKeyPathWorkoutTotalDistance,
 distance];
```

## Parameters

- `operatorType`: The operator type to use when comparing the total distance.
- `totalDistance`: The target distance.

## See Also

### Related Documentation
- [var totalDistance: HKQuantity?](../hkworkout/totaldistance.md)
  The total distance traveled during the workout.
- [let HKPredicateKeyPathWorkoutTotalDistance: String](../hkpredicatekeypathworkouttotaldistance.md)
  The key path for accessing the workout’s total distance.
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
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, totalEnergyBurned: HKQuantity) -> NSPredicate](./predicateforworkouts%28with,totalenergyburned%29.md)
  Returns a predicate for matching workouts based on the total energy burned.
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, totalFlightsClimbed: HKQuantity) -> NSPredicate](./predicateforworkouts%28with,totalflightsclimbed%29.md)
  Returns a predicate that matches workout samples based on the number of flights climbed.
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, totalSwimmingStrokeCount: HKQuantity) -> NSPredicate](./predicateforworkouts%28with,totalswimmingstrokecount%29.md)
  Returns a predicate that matches workout samples based on the number of strokes while swimming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforworkouts(with:totaldistance:))*