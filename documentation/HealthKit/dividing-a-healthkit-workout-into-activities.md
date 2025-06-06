# Dividing a HealthKit workout into activities

**Framework**: HealthKit

Partition multisport and interval workouts into activities that represent the different parts of the workout.

#### Overview

Some workouts benefit from having the workout’s duration broken into a set of discrete activities. For example, a multisport event, like a triathlon, has separate swim, bike, and run portions. Similarly, you can divide interval training into active and rest periods.

![An illustration showing a .swimBikeRun workout and its corresponding .swimming, .biking, .running, and .transition activities. The activities fill the entire time covered by the workout, but none of the activities overlap.](https://docs-assets.developer.apple.com/published/74a2190228254300b6b8371b87c2ec31/media-4083470%402x.png)

To model these activities in HealthKit, use the [`HKWorkoutActivity`](hkworkoutactivity.md) class to specify the different parts of a workout. You can then query for workouts that have matching activities, and analyze those activities independently from the rest of the workout.

[`HKWorkoutActivity`](hkworkoutactivity.md) instances have two main use cases:

> **Note**:  All [`HKWorkout`](hkworkout.md) objects have at least one associated [`HKWorkoutActivity`](hkworkoutactivity.md). If you don’t explicitly add an activity to a workout, HealthKit adds an activity that matches the workout’s activity type. This means you can use [`predicateForWorkoutActivities(workoutActivityType:)`](hkquery/predicateforworkoutactivities(workoutactivitytype:).md) to filter for all the workouts that track an activity type. For example, filtering for workout activities that use [`HKWorkoutActivityType.running`](hkworkoutactivitytype/running.md) includes regular running workouts, running interval training, and [`HKWorkoutActivityType.swimBikeRun`](hkworkoutactivitytype/swimbikerun.md) workouts that include a running activity.

 All [`HKWorkout`](hkworkout.md) objects have at least one associated [`HKWorkoutActivity`](hkworkoutactivity.md). If you don’t explicitly add an activity to a workout, HealthKit adds an activity that matches the workout’s activity type. This means you can use [`predicateForWorkoutActivities(workoutActivityType:)`](hkquery/predicateforworkoutactivities(workoutactivitytype:).md) to filter for all the workouts that track an activity type. For example, filtering for workout activities that use [`HKWorkoutActivityType.running`](hkworkoutactivitytype/running.md) includes regular running workouts, running interval training, and [`HKWorkoutActivityType.swimBikeRun`](hkworkoutactivitytype/swimbikerun.md) workouts that include a running activity.

##### Mark Transitions

Activities can’t overlap, but they also don’t need to cover the entire [`HKWorkout`](hkworkout.md) sample’s duration. You can leave the time between the active portions of the workout blank, or you can explicitly create workout activities for these intervals. For example, explicitly creating activities for the time between active portions of the workout helps you track statistics during those intervals.

For multisport workouts, you can explicitly mark the transitions between activities using an [`HKWorkoutActivityType.transition`](hkworkoutactivitytype/transition.md) type. For interval training, you can use the same activity type as the workout for the rest periods; however, you may want to add custom metadata to indicate whether the activity is an active or resting interval.

How you choose to model the data depends on the needs of your app and the types of intervals you’re tracking. If you’re tracking a workout that alternates between a fast and a slow pace, using workout activities to explicitly track all intervals makes sense. If, however, the intervals alternate between exercising and resting (for example, during many high-intensity interval training exercises), you may want to leave the rest intervals blank.

##### Add Workout Activities to a Workout Session

To add workout activities to a workout session, start by creating the session and start collecting data using the workout builder.

```swift
// Create the workout configuration for a multisport workout.
let configuration = HKWorkoutConfiguration()
configuration.activityType = .swimBikeRun
configuration.locationType = .outdoor

// Create the workout session.
session = try HKWorkoutSession(healthStore: store,
                               configuration: configuration)

// Start the session and the workout builder.
let startDate = Date()
session.startActivity(with: startDate)
workoutBuilder = session.associatedWorkoutBuilder()

// Set the workout builder's data source.
workoutBuilder.dataSource =
HKLiveWorkoutDataSource(healthStore: store,
                        workoutConfiguration: configuration)

// Start collecting data.
try await workoutBuilder.beginCollection(at: startDate)
```

Next, when an activity begins, create a new configuration for the activity, and start the activity using the session’s [`beginNewActivity(configuration:date:metadata:)`](hkworkoutsession/beginnewactivity(configuration:date:metadata:).md) method. The data source automatically begins collecting the default data types for the activity.

```swift
// Start the swimming activity.
let swimmingConfiguration = HKWorkoutConfiguration()
swimmingConfiguration.activityType = .swimming
swimmingConfiguration.locationType = .outdoor
swimmingConfiguration.swimmingLocationType = .openWater

session.beginNewActivity(configuration: swimmingConfiguration,
                         date: Date(),
                         metadata: nil)
```

When the activity ends, call the session’s [`endCurrentActivity(on:)`](hkworkoutsession/endcurrentactivity(on:).md) method. HealthKit also ends the current activity when you begin a new activity.

```swift
// End the activity.
session.endCurrentActivity(on: Date())
```

To explicitly track the intervals between activities, start a new activity using [`HKWorkoutActivityType.transition`](hkworkoutactivitytype/transition.md). End this transition when the next activity begins.

```swift
// Explicitly track the transition between activities.
let transitionConfiguration = HKWorkoutConfiguration()
transitionConfiguration.activityType = .transition
transitionConfiguration.locationType = .outdoor

session.beginNewActivity(configuration: transitionConfiguration,
                         date: Date(),
                         metadata: nil)
```

Finally, when the entire workout session ends, call the session’s [`end()`](hkworkoutsession/end().md) method. This also ends the current activity. Then call the workout builder’s [`finishWorkout(completion:)`](hkworkoutbuilder/finishworkout(completion:).md) method to save the workout to the HealthKit store. This method also returns an [`HKWorkout`](hkworkout.md) object, which you can use to display summary information about the workout.

```swift
// Ending the session also ends the current activity.
session.end()

// Finishing the workout saves the workout
// and returns an HKWorkout object that you can use to display summary data.
let workout = try await workoutBuilder.finishWorkout()

// Do something with the workout here.
print(workout as Any)
```

##### Enable and Disable the Collection of Data

When you start a new workout activity, your data source automatically begins collecting relevant data from Apple Watch. To see the data types that the data source collects, check the data source’s `typesToCollect` property.

When running an [`HKWorkoutActivityType.swimBikeRun`](hkworkoutactivitytype/swimbikerun.md) workout session, HealthKit automatically changes the collected data types based on the current workout activity. For example, the data source collects data like [`activeEnergyBurned`](hkquantitytypeidentifier/activeenergyburned.md), [`distanceSwimming`](hkquantitytypeidentifier/distanceswimming.md), and [`swimmingStrokeCount`](hkquantitytypeidentifier/swimmingstrokecount.md).

If you start an [`HKWorkoutActivityType.running`](hkworkoutactivitytype/running.md) activity, the system automatically updates the data source’s `typesToCollect` property based on the new activity. For example, the data source automatically stops collecting [`distanceSwimming`](hkquantitytypeidentifier/distanceswimming.md) and [`swimmingStrokeCount`](hkquantitytypeidentifier/swimmingstrokecount.md), and starts collecting relevant data like [`distanceWalkingRunning`](hkquantitytypeidentifier/distancewalkingrunning.md) and [`runningStrideLength`](hkquantitytypeidentifier/runningstridelength.md).

Most of the time, you can use the default collected data types. However, if your app calculates and saves its own [`HKSample`](hksample.md) objects during the workout, you may want to manually enable and disable the collection of that data type, letting the data source automatically associate your samples with the workout.

To start collecting a data type, call the data source’s [`enableCollection(for:predicate:)`](hkliveworkoutdatasource/enablecollection(for:predicate:).md) method.

```swift
// Enable the collection of respiratory rate.
guard let dataSource = session.associatedWorkoutBuilder().dataSource else {
    print("*** No data source found! ***")
    return }

let respiratoryRate = HKQuantityType(.respiratoryRate)
dataSource.enableCollection(for: respiratoryRate, predicate: nil)
```

HealthKit then associates any matching samples from your app with the workout activity. You can also disable the collection of a data type by calling [`disableCollection(for:)`](hkliveworkoutdatasource/disablecollection(for:).md).

```swift
// Disable the collection of respiratory rate.
guard let dataSource = session.associatedWorkoutBuilder().dataSource else {
    print("*** No data source found! ***")
    return }

let respiratoryRate = HKQuantityType(.respiratoryRate)
dataSource.disableCollection(for: respiratoryRate)
```

##### Query for Workout Activities

To query for workouts with activities that match a specific predicate, start by creating a workout activity predicate using one of the [`HKQuery`](hkquery.md) class’s `predicateForWorkoutActivities` methods. Next, use [`predicateForWorkouts(activityPredicate:)`](hkquery/predicateforworkouts(activitypredicate:).md) to wrap the activity predicate inside a workout predicate. You can then use the workout predicate in your query.

```swift
// Create a predicate for an average heart rate of greater than 150 bpm.
let highHeartRate = HKQuantity(unit: .count(), doubleValue: 150.0)
let heartRateType = HKQuantityType(.heartRate)

let heartRatePredicate =
HKQuery.predicateForWorkoutActivities(operatorType: .greaterThan,
                                      quantityType: heartRateType,
                                      averageQuantity: highHeartRate)

// Wrap the workout activity predicate inside a workout predicate.
let workoutPredicate = HKQuery.predicateForWorkouts(activityPredicate: heartRatePredicate)

let query = HKSampleQueryDescriptor(predicates: [.workout(workoutPredicate)],
                                    sortDescriptors: [])

let matchingWorkouts = try await query.result(for: store)

// Do something with the samples here.
print(matchingWorkouts)
```

This example returns all the workouts that have an activity with an average heart rate over 150 bpm. Use the workout’s [`workoutActivities`](hkworkout/workoutactivities.md) property to access the activities associated with a workout.

## See Also

- [Adding samples to a workout](adding-samples-to-a-workout.md)
  Create associated samples that add details to a workout.
- [Accessing condensed workout samples](accessing-condensed-workout-samples.md)
  Read series data from condensed workouts.
- [class HKWorkout](hkworkout.md)
  A workout sample that stores information about a single physical activity.
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/dividing-a-healthkit-workout-into-activities)*