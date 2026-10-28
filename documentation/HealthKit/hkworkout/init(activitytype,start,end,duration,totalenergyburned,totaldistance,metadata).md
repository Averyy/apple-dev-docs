# init(activityType:start:end:duration:totalEnergyBurned:totalDistance:metadata:)

**Framework**: HealthKit  
**Kind**: init  
**Role**: Initializer

Instantiates a new workout that includes the energy burned, distance, and metadata for the workout.

**Availability**:
- iOS 8.0+ - Deprecated in 17.0
- iPadOS 8.0+ - Deprecated in 17.0
- Mac Catalyst 13.0+ - Deprecated in 16.0
- macOS 13.0+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 10.0

> **Deprecated**: Use HKWorkoutBuilder

## Declaration

```swift
convenience init(activityType workoutActivityType: HKWorkoutActivityType, start startDate: Date, end endDate: Date, duration: TimeInterval, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, metadata: [String : Any]?)
```

```objc
+ (instancetype) workoutWithActivityType:(HKWorkoutActivityType) workoutActivityType startDate:(NSDate *) startDate endDate:(NSDate *) endDate duration:(NSTimeInterval) duration totalEnergyBurned:(HKQuantity *) totalEnergyBurned totalDistance:(HKQuantity *) totalDistance metadata:(NSDictionary<NSString *,id> *) metadata;
```

## Return Value

A workout object with the provided duration, total energy burned, total distance, and metadata properties. The [`workoutEvents`](./workoutevents.md) property and the device are set to `nil`.

## Discussion

This method returns a workout with the specified duration, total energy burned, total distance and metadata. The [`workoutEvents`](./workoutevents.md)property and the device are set to `nil`.

If the total energy burned or total distance are nonzero values, create a set of corresponding samples that add up to the calculated totals. Associate these samples with the workout by calling the health store’s [`add(_:to:completion:)`](../hkhealthstore/add%28_,to,completion%29.md) method.

**Swift**:

```swift
let distance = HKQuantity(unit: HKUnit.mileUnit(), doubleValue: 5.2)
let energyBurned = HKQuantity(unit: HKUnit.kilocalorieUnit(), doubleValue: 259.0)
let metadata = [HKMetadataKeyIndoorWorkout:false]
 
let hike = HKWorkout(activityType: HKWorkoutActivityType.Hiking,
                     startDate: start, endDate: end, duration: 9000,
                     totalEnergyBurned: energyBurned, totalDistance: distance, metadata: metadata)
 
 
healthStore.saveObject(hike) { (success, error) -> Void in
    guard success else {
        // Perform proper error handling here...
        fatalError("*** An error occurred while saving this " +
            "workout: \(error?.localizedDescription)")
    }
}
```

**Objective-C**:

```objc
HKQuantity *distance = [HKQuantity quantityWithUnit:[HKUnit mileUnit]
                                        doubleValue:5.2];
 
HKQuantity *energyBurned = [HKQuantity quantityWithUnit:[HKUnit kilocalorieUnit]
                                            doubleValue:259.0];
 
NSDictionary *metadata = @{HKMetadataKeyIndoorWorkout: @(NO)};
 
HKWorkout *hike = [HKWorkout workoutWithActivityType:HKWorkoutActivityTypeHiking
                                           startDate:start
                                             endDate:end
                                            duration:9000
                                   totalEnergyBurned:energyBurned
                                       totalDistance:distance
                                            metadata:metadata];
 
[self.healthStore
 saveObject:hike
 withCompletion:^(BOOL success, NSError *error) {
 
     if (!success) {
         // Perform proper error handling here...
         NSLog(@"*** An error occurred while saving this "
               @"workout: %@ ***", error.localizedDescription);
     }
 
 
 }];
```

## Parameters

- `workoutActivityType`: The type of activity performed during the workout. For a complete list of activity types, see [`HKWorkoutActivityType`](../hkworkoutactivitytype.md).
- `startDate`: The date and time when the activity started.
- `endDate`: The date and time when the activity ended. This date must be equal to or later than the start date.
- `duration`: A time interval representing the workout’s actual duration. Passing a nonzero value sets the workout’s [`duration`](./duration.md) property. If you pass 0, this method calculates the [`duration`](./duration.md) property based on the workout’s start and end dates.
- `totalEnergyBurned`: A quantity using energy units, or `nil`. This property sets the workout’s [`totalEnergyBurned`](./totalenergyburned.md) property. It represents the total active energy burned during the workout.
- `totalDistance`: A quantity using length units, or `nil`. This property sets the workout’s [`totalDistance`](./totaldistance.md) property.
- `metadata`: The metadata dictionary contains extra information describing this workout. The dictionary’s keys are all [`NSString`](../../Foundation/nsstring.md) objects . The values may be [`NSString`](../../Foundation/nsstring.md), [`NSNumber`](../../Foundation/nsnumber.md), or [`NSDate`](../../Foundation/nsdate.md) objects. For a complete list of predefined metadata keys, see Metadata Keys.

  Using predefined keys helps facilitate sharing data between apps; however, you are also encouraged to create your own, custom keys as needed to extend the workout’s capabilities.

## See Also

### Related Documentation
- [var workoutActivityType: HKWorkoutActivityType](./workoutactivitytype.md)
  The type of activity performed during the workout.
- [var totalDistance: HKQuantity?](./totaldistance.md)
  The total distance traveled during the workout.
- [var duration: TimeInterval](./duration.md)
  The workout’s duration.
- [var metadata: [String : Any]?](../hkobject/metadata.md)
  The metadata for this HealthKit object.
- [var totalEnergyBurned: HKQuantity?](./totalenergyburned.md)
  The total active energy burned during the workout.
- [var workoutEvents: [HKWorkoutEvent]?](./workoutevents.md)
  An array of workout event objects.
### Creating workouts
- [convenience init(activityType: HKWorkoutActivityType, start: Date, end: Date)](./init%28activitytype,start,end%29.md)
  Instantiates a new workout.
- [convenience init(activityType: HKWorkoutActivityType, start: Date, end: Date, workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, metadata: [String : Any]?)](./init%28activitytype,start,end,workoutevents,totalenergyburned,totaldistance,metadata%29.md)
  Instantiates a new workout whose duration is calculated based on the start and end dates and the provided workout events.
- [convenience init(activityType: HKWorkoutActivityType, start: Date, end: Date, duration: TimeInterval, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, device: HKDevice?, metadata: [String : Any]?)](./init%28activitytype,start,end,duration,totalenergyburned,totaldistance,device,metadata%29.md)
  Instantiates a new workout activity that includes the device that produced the sample data.
- [convenience init(activityType: HKWorkoutActivityType, start: Date, end: Date, workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, device: HKDevice?, metadata: [String : Any]?)](./init%28activitytype,start,end,workoutevents,totalenergyburned,totaldistance,device,metadata%29.md)
  Instantiates a workout that includes both workout events and the device that produced the sample data.
- [convenience init(activityType: HKWorkoutActivityType, start: Date, end: Date, workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, totalFlightsClimbed: HKQuantity?, device: HKDevice?, metadata: [String : Any]?)](./init%28activitytype,start,end,workoutevents,totalenergyburned,totaldistance,totalflightsclimbed,device,metadata%29.md)
  Instantiates a workout using a variety of data, including the number of flights of stairs climbed.
- [convenience init(activityType: HKWorkoutActivityType, start: Date, end: Date, workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, totalSwimmingStrokeCount: HKQuantity?, device: HKDevice?, metadata: [String : Any]?)](./init%28activitytype,start,end,workoutevents,totalenergyburned,totaldistance,totalswimmingstrokecount,device,metadata%29.md)
  Instantiates a workout using a variety of data, including the number of strokes while swimming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkout/init(activitytype:start:end:duration:totalenergyburned:totaldistance:metadata:))*