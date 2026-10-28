# predicateForObjects(from:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a predicate that matches any objects that have been associated with the provided workout.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
class func predicateForObjects(from workout: HKWorkout) -> NSPredicate
```

```objc
+ (NSPredicate *) predicateForObjectsFromWorkout:(HKWorkout *) workout;
```

## Mentions

- [Adding samples to a workout](../adding-samples-to-a-workout.md)

## Return Value

A predicate that matches any objects that have been added to the provided workout.

## Discussion

Use this convenience method to create a predicate that matches all the HealthKit objects for a given workout. The following sample uses both the convenience method and a predicate format string to create equivalent predicates.

**Swift**:

```swift
let workoutObjects = HKQuery.predicateForObjectsFromWorkout(workout)
 
let explicitWorkoutObjects =
    NSPredicate(format: "%K == %@", HKPredicateKeyPathWorkout, workout)
```

**Objective-C**:

```objc
NSPredicate *workoutObjects = [HKQuery predicateForObjectsFromWorkout:workout];
 
NSPredicate *explicitWorkoutObjects =
[NSPredicate predicateWithFormat:@"%K == %@",
 HKPredicateKeyPathWorkout,
 workout];
```

## Parameters

- `workout`: The workout you are searching for.

## See Also

### Related Documentation
- [func add([HKSample], to: HKWorkout, completion: (Bool, (any Error)?) -> Void)](../hkhealthstore/add%28_,to,completion%29.md)
  Associates the provided samples with the specified workout.
### Creating workout predicates
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
- [class func predicateForWorkouts(with: NSComparisonPredicate.Operator, totalSwimmingStrokeCount: HKQuantity) -> NSPredicate](./predicateforworkouts%28with,totalswimmingstrokecount%29.md)
  Returns a predicate that matches workout samples based on the number of strokes while swimming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforobjects(from:)-5irg9)*