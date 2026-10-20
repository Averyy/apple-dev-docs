# predicateForWorkouts(with:totalEnergyBurned:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a predicate for matching workouts based on the total energy burned.

**Availability**:
- iOS 8.0+ - Deprecated in 18.0
- iPadOS 8.0+ - Deprecated in 18.0
- Mac Catalyst 13.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 2.0+ - Deprecated in 11.0

> **Deprecated**: Use predicateForWorkoutsWithOperatorType:quantityType:sumQuantity: passing the HKQuantityType for HKQuantityTypeIdentifierActiveEnergyBurned

## Declaration

```swift
class func predicateForWorkouts(with operatorType: NSComparisonPredicate.Operator, totalEnergyBurned: HKQuantity) -> NSPredicate
```

```objc
+ (NSPredicate *) predicateForWorkoutsWithOperatorType:(NSPredicateOperatorType) operatorType totalEnergyBurned:(HKQuantity *) totalEnergyBurned;
```

#### Return Value

A predicate for matching workouts based on the total energy burned. This predicate works only on workouts.

#### Discussion

Use this convenience method to create a predicate that matches against a workout’s total energy burned. The following sample uses both the convenience method and a predicate format string to create equivalent predicates.

**Swift**:

```swift
// Predicate matching workouts burning 500 calories or more
let energyBurned = HKQuantity(unit: HKUnit.kilocalorieUnit(), doubleValue: 500)
let workout = HKQuery.predicateForWorkoutsWithOperatorType(
    .GreaterThanOrEqualToPredicateOperatorType,
    totalEnergyBurned: energyBurned)
 
 
let explicitWorkout = NSPredicate(format: "%K >= %@",
                                  HKPredicateKeyPathWorkoutTotalEnergyBurned, energyBurned)
```

**Objective-C**:

```objc
// Predicate matching workouts burning 500 calories or more
HKQuantity *energyBurned =
[HKQuantity quantityWithUnit:[HKUnit kilocalorieUnit] doubleValue:500];
 
NSPredicate *workout =
    [HKQuery predicateForWorkoutsWithOperatorType:
     NSGreaterThanOrEqualToPredicateOperatorType
     totalEnergyBurned:energyBurned];
 
NSPredicate *explicitWorkout =
[NSPredicate predicateWithFormat:@"%K >= %@",
 HKPredicateKeyPathWorkoutTotalEnergyBurned,
 energyBurned];
```

## Parameters

- `operatorType`: The operator type to use when comparing the total energy burned.
- `totalEnergyBurned`: The target amount of energy burned.

## See Also

### Related Documentation
- [let HKPredicateKeyPathWorkoutTotalEnergyBurned: String](../hkpredicatekeypathworkouttotalenergyburned.md)
  The key path for accessing the workout’s total energy burned.
- [var totalEnergyBurned: HKQuantity?](../hkworkout/totalenergyburned.md)
  The total active energy burned during the workout.
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
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, totalFlightsClimbed: HKQuantity) -> NSPredicate](./predicateforworkouts%28with,totalflightsclimbed%29.md)
  Returns a predicate that matches workout samples based on the number of flights climbed.
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, totalSwimmingStrokeCount: HKQuantity) -> NSPredicate](./predicateforworkouts%28with,totalswimmingstrokecount%29.md)
  Returns a predicate that matches workout samples based on the number of strokes while swimming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforworkouts(with:totalenergyburned:))*