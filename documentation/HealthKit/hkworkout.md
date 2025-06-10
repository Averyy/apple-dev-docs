# HKWorkout

**Framework**: HealthKit  
**Kind**: class

A workout sample that stores information about a single physical activity.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKWorkout
```

## Mentions

- [Dividing a HealthKit workout into activities](dividing-a-healthkit-workout-into-activities.md)
- [About the HealthKit framework](about-the-healthkit-framework.md)
- [Creating a workout route](creating-a-workout-route.md)

#### Overview

The [`HKWorkout`](hkworkout.md) class is a concrete subclass of the [`HKSample`](hksample.md) class; however, they behave somewhat differently than other sample types.

- You don’t need a specific type identifier to create the [`HKWorkoutType`](hkworkouttype.md) instance. All workouts use the same type identifier.
- You must provide an [`HKWorkoutActivityType`](hkworkoutactivitytype.md) value for each workout. This value defines the type of activity performed during the workout.
- After saving the workout to the HealthKit store, you must associate additional samples with the workout (for example, active energy burned or distance samples). These samples provide fine-grained details. Use the [`add(_:to:completion:)`](hkhealthstore/add(_:to:completion:).md) method to associate them with the workout.

![An illustration showing how a workout is created and added to the store.](https://docs-assets.developer.apple.com/published/3e2441ede3d4e430ec577a6823e2f76d/media-3570087%402x.png)

The workout records a summary of information about a single physical activity (for example, the duration, total distance, and total energy burned). It also acts as a container for other [`HKSample`](hksample.md) objects. You can associate any number of samples with a workout, adding details over the course of the workout. For example, you may want to break a single run into a number of shorter intervals, and then add samples to track the user’s heart rate, energy burned, distance traveled, and steps taken for each interval. For more information, see [`Adding samples to a workout`](adding-samples-to-a-workout.md).

> **Note**:  If a workout has summary information, it also needs a set of associated samples that add up to the summary’s total. See [`Adding samples to a workout`](adding-samples-to-a-workout.md).

HealthKit supports a wide range of activity types. For a complete list, see [`HKWorkoutActivityType`](hkworkoutactivitytype.md).

Workouts are mostly immutable. You set their properties when you instantiate the workout, and they can’t change. However, you can continue to add samples to the workouts.

##### Fill the Activity Rings

Workouts can contribute to the Move and Exercise rings in the Activity app. To affect the rings, you must associate one or more active energy burned samples with the workout. Additionally:

- In watchOS. Use a workout session to track the user’s activity. When the session has ended, create a workout object and the associated active energy burned samples. For more information, see [`HKWorkoutSession`](hkworkoutsession.md).

The system updates the Move ring based on the active energy burned samples. It updates the Exercise ring based on the amount of time the user spent actually exerting themselves during the workout session, as calculated by the watch’s sensors.

- In iOS. No additional work is necessary. Workout objects automatically contribute to both the Move and Exercise rings. The Exercise ring increases by the workout’s total duration, and the Move ring increases by the number of calories in the associated active energy burned samples. HealthKit also increases the Stand ring by one hour for each wall-clock hour that the workout overlaps.

Create and save workouts on the device that makes the most sense for your application—typically the device processing the user’s workout.

##### Extend Workouts

Like many HealthKit classes, the `HKWorkout` class should not be subclassed. You may extend workouts by adding metadata with custom keys as appropriate for your app.

For more information, see the methods [`init(activityType:start:end:duration:totalEnergyBurned:totalDistance:metadata:)`](hkworkout/init(activitytype:start:end:duration:totalenergyburned:totaldistance:metadata:).md) and [`init(activityType:start:end:workoutEvents:totalEnergyBurned:totalDistance:metadata:)`](hkworkout/init(activitytype:start:end:workoutevents:totalenergyburned:totaldistance:metadata:).md).

## Topics

### Creating workouts
- [convenience init(activityType: HKWorkoutActivityType, start: Date, end: Date)](hkworkout/init(activitytype:start:end:).md)
  Instantiates a new workout.
- [convenience init(activityType: HKWorkoutActivityType, start: Date, end: Date, duration: TimeInterval, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, metadata: [String : Any]?)](hkworkout/init(activitytype:start:end:duration:totalenergyburned:totaldistance:metadata:).md)
  Instantiates a new workout that includes the energy burned, distance, and metadata for the workout.
- [convenience init(activityType: HKWorkoutActivityType, start: Date, end: Date, workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, metadata: [String : Any]?)](hkworkout/init(activitytype:start:end:workoutevents:totalenergyburned:totaldistance:metadata:).md)
  Instantiates a new workout whose duration is calculated based on the start and end dates and the provided workout events.
- [convenience init(activityType: HKWorkoutActivityType, start: Date, end: Date, duration: TimeInterval, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, device: HKDevice?, metadata: [String : Any]?)](hkworkout/init(activitytype:start:end:duration:totalenergyburned:totaldistance:device:metadata:).md)
  Instantiates a new workout activity that includes the device that produced the sample data.
- [convenience init(activityType: HKWorkoutActivityType, start: Date, end: Date, workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, device: HKDevice?, metadata: [String : Any]?)](hkworkout/init(activitytype:start:end:workoutevents:totalenergyburned:totaldistance:device:metadata:).md)
  Instantiates a workout that includes both workout events and the device that produced the sample data.
- [convenience init(activityType: HKWorkoutActivityType, start: Date, end: Date, workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, totalFlightsClimbed: HKQuantity?, device: HKDevice?, metadata: [String : Any]?)](hkworkout/init(activitytype:start:end:workoutevents:totalenergyburned:totaldistance:totalflightsclimbed:device:metadata:).md)
  Instantiates a workout using a variety of data, including the number of flights of stairs climbed.
- [convenience init(activityType: HKWorkoutActivityType, start: Date, end: Date, workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, totalSwimmingStrokeCount: HKQuantity?, device: HKDevice?, metadata: [String : Any]?)](hkworkout/init(activitytype:start:end:workoutevents:totalenergyburned:totaldistance:totalswimmingstrokecount:device:metadata:).md)
  Instantiates a workout using a variety of data, including the number of strokes while swimming.
### Accessing workout data
- [var duration: TimeInterval](hkworkout/duration.md)
  The workout’s duration.
- [var workoutActivityType: HKWorkoutActivityType](hkworkout/workoutactivitytype.md)
  The type of activity performed during the workout.
- [var workoutActivities: [HKWorkoutActivity]](hkworkout/workoutactivities.md)
- [var workoutEvents: [HKWorkoutEvent]?](hkworkout/workoutevents.md)
  An array of workout event objects.
- [func statistics(for: HKQuantityType) -> HKStatistics?](hkworkout/statistics(for:).md)
  Returns the workout’s statistics for the provided quantity type.
- [var allStatistics: [HKQuantityType : HKStatistics]](hkworkout/allstatistics.md)
  A dictionary that contains all the statistics for the workout.
- [var totalDistance: HKQuantity?](hkworkout/totaldistance.md)
  The total distance traveled during the workout.
- [var totalEnergyBurned: HKQuantity?](hkworkout/totalenergyburned.md)
  The total active energy burned during the workout.
- [var totalFlightsClimbed: HKQuantity?](hkworkout/totalflightsclimbed.md)
  The total number of flights of stairs climbed during the workout.
- [var totalSwimmingStrokeCount: HKQuantity?](hkworkout/totalswimmingstrokecount.md)
  The total stroke count for the workout.
### Specifying sort identifiers
- [let HKWorkoutSortIdentifierDuration: String](hkworkoutsortidentifierduration.md)
  A constant for sorting workouts based on their duration.
- [let HKWorkoutSortIdentifierTotalDistance: String](hkworkoutsortidentifiertotaldistance.md)
  A constant for sorting workouts based on their total distance.
- [let HKWorkoutSortIdentifierTotalEnergyBurned: String](hkworkoutsortidentifiertotalenergyburned.md)
  A constant for sorting workouts based on the total energy burned.
### Specifying predicate key paths
- [let HKPredicateKeyPathWorkoutType: String](hkpredicatekeypathworkouttype.md)
  The key path for accessing the workout’s type.
- [let HKPredicateKeyPathWorkoutDuration: String](hkpredicatekeypathworkoutduration.md)
  The key path for accessing the workout’s duration.
- [let HKPredicateKeyPathWorkoutTotalDistance: String](hkpredicatekeypathworkouttotaldistance.md)
  The key path for accessing the workout’s total distance.
- [let HKPredicateKeyPathWorkoutTotalEnergyBurned: String](hkpredicatekeypathworkouttotalenergyburned.md)
  The key path for accessing the workout’s total energy burned.
- [let HKPredicateKeyPathWorkoutAverageQuantity: String](hkpredicatekeypathworkoutaveragequantity.md)
  The key path for accessing workouts with a matching average quantity.
- [let HKPredicateKeyPathWorkoutMaximumQuantity: String](hkpredicatekeypathworkoutmaximumquantity.md)
  The key path for accessing workouts with a matching maximum quantity.
- [let HKPredicateKeyPathWorkoutMinimumQuantity: String](hkpredicatekeypathworkoutminimumquantity.md)
  The key path for accessing workouts with a matching minimum quantity.
- [let HKPredicateKeyPathWorkoutSumQuantity: String](hkpredicatekeypathworkoutsumquantity.md)
  The key path for accessing workouts with a matching sum.
### Specifying metadata keys
- [Workout Metadata Keys](workout-metadata-keys.md)
  Constants that can be used to add metadata to workouts.
### Instance Properties
- [var workoutPlan: WorkoutPlan?](hkworkout/workoutplan.md)

## Relationships

### Inherits From
- [HKSample](hksample.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Adding samples to a workout](adding-samples-to-a-workout.md)
  Create associated samples that add details to a workout.
- [Accessing condensed workout samples](accessing-condensed-workout-samples.md)
  Read series data from condensed workouts.
- [Dividing a HealthKit workout into activities](dividing-a-healthkit-workout-into-activities.md)
  Partition multisport and interval workouts into activities that represent the different parts of the workout.
- [class HKWorkoutActivity](hkworkoutactivity.md)
  An object that describes an activity within a longer workout.
- [class HKWorkoutBuilder](hkworkoutbuilder.md)
  A builder object that incrementally constructs a workout.
- [class HKWorkoutType](hkworkouttype.md)
  A type that identifies samples that store information about a workout.
- [let HKWorkoutTypeIdentifier: String](hkworkouttypeidentifier.md)
  The workout type identifier.
- [enum HKWorkoutActivityType](hkworkoutactivitytype.md)
  The type of activity performed during a workout.
- [enum HKWorkoutSessionType](hkworkoutsessiontype.md)
  The type of session.
- [class HKWorkoutEvent](hkworkoutevent.md)
  An object representing an important event during a workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkout)*