# predicateForWorkouts(with:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a predicate for matching workouts based on the type of activity.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
class func predicateForWorkouts(with workoutActivityType: HKWorkoutActivityType) -> NSPredicate
```

```objc
+ (NSPredicate *) predicateForWorkoutsWithWorkoutActivityType:(HKWorkoutActivityType) workoutActivityType;
```

#### Return Value

A predicate for matching workouts based on the type of activity.

#### Discussion

Use this convenience method to create a predicate that matches workouts based on their activity. The following sample uses both the convenience method and a predicate format string to create equivalent predicates.

**Swift**:

```swift
let workout = HKQuery.predicateForWorkouts(with: .curling)
 
 
let explicitWorkout = NSPredicate(format: "%K == %d",
                                  HKPredicateKeyPathWorkoutType,
                                  HKWorkoutActivityType.curling.rawValue)
```

**Objective-C**:

```objc
NSPredicate *workout =
    [HKQuery predicateForWorkoutsWithWorkoutActivityType:
     HKWorkoutActivityTypeCurling];
 
NSPredicate *explicitWorkout =
[NSPredicate predicateWithFormat:@"%K == %d",
 HKPredicateKeyPathWorkoutType,
 HKWorkoutActivityTypeCurling];
```

## Parameters

- `workoutActivityType`: The type of activity. For a list of valid workout activities, see [`HKWorkoutActivityType`](../hkworkoutactivitytype.md).

## See Also

### Related Documentation
- [var workoutActivityType: HKWorkoutActivityType](../hkworkout/workoutactivitytype.md)
  The type of activity performed during the workout.
- [let HKPredicateKeyPathWorkoutType: String](../hkpredicatekeypathworkouttype.md)
  The key path for accessing the workout’s type.
### Creating workout predicates
- [class func predicateForObjects(from: HKWorkout) -> NSPredicate](./predicateforobjects%28from%29-5irg9.md)
  Returns a predicate that matches any objects that have been associated with the provided workout.
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
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, totalSwimmingStrokeCount: HKQuantity) -> NSPredicate](./predicateforworkouts%28with,totalswimmingstrokecount%29.md)
  Returns a predicate that matches workout samples based on the number of strokes while swimming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforworkouts(with:))*