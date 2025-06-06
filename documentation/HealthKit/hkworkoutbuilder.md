# HKWorkoutBuilder

**Framework**: HealthKit  
**Kind**: class

A builder object that incrementally constructs a workout.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class HKWorkoutBuilder
```

#### Overview

Incrementally collect samples and events associated with a workout. When the workout ends, call [`finishWorkout(completion:)`](hkworkoutbuilder/finishworkout(completion:).md) to create an [`HKWorkout`](hkworkout.md) sample and save it to the HealthKit store.

For watchOS, use an [`HKWorkoutSession`](hkworkoutsession.md) and an [`HKLiveWorkoutBuilder`](hkliveworkoutbuilder.md) instead.

## Topics

### Creating the builder
- [init(healthStore: HKHealthStore, configuration: HKWorkoutConfiguration, device: HKDevice?)](hkworkoutbuilder/init(healthstore:configuration:device:).md)
  Returns a new workout builder object that is not connected to a workout session or other data source.
- [var device: HKDevice?](hkworkoutbuilder/device.md)
  The device associated with the workout.
- [var workoutConfiguration: HKWorkoutConfiguration](hkworkoutbuilder/workoutconfiguration.md)
  The configuration information for the workout.
### Starting the workout
- [func beginCollection(withStart: Date, completion: (Bool, (any Error)?) -> Void)](hkworkoutbuilder/begincollection(withstart:completion:).md)
  Sets the workout’s start date and begins building the workout.
- [var startDate: Date?](hkworkoutbuilder/startdate.md)
  The workout’s start date and time.
- [func elapsedTime(at: Date) -> TimeInterval](hkworkoutbuilder/elapsedtime(at:).md)
  Calculates the duration of the workout at the specified time.
### Associating samples with the workout
- [func add([HKSample], completion: (Bool, (any Error)?) -> Void)](hkworkoutbuilder/add(_:completion:).md)
  Adds a sample to be associated with the workout.
- [func seriesBuilder(for: HKSeriesType) -> HKSeriesBuilder?](hkworkoutbuilder/seriesbuilder(for:).md)
  Returns the series builder for the specified type, creating a new builder, if necessary.
- [func statistics(for: HKQuantityType) -> HKStatistics?](hkworkoutbuilder/statistics(for:).md)
  Returns the statistics calculated for matching samples added to the workout.
### Adding metadata to the workout
- [func addMetadata([String : Any], completion: (Bool, (any Error)?) -> Void)](hkworkoutbuilder/addmetadata(_:completion:).md)
  Adds metadata to be saved with the workout.
- [var metadata: [String : Any]](hkworkoutbuilder/metadata.md)
  The metadata the builder saves with the workout.
### Adding events to the workout
- [func addWorkoutEvents([HKWorkoutEvent], completion: (Bool, (any Error)?) -> Void)](hkworkoutbuilder/addworkoutevents(_:completion:).md)
  Adds a workout event to the builder.
- [var workoutEvents: [HKWorkoutEvent]](hkworkoutbuilder/workoutevents.md)
  The list of events added to the workout.
### Managing workout activities
- [func addWorkoutActivity(HKWorkoutActivity, completion: (Bool, (any Error)?) -> Void)](hkworkoutbuilder/addworkoutactivity(_:completion:).md)
  Adds a workout activity to the workout builder.
- [func updateActivity(uuid: UUID, adding: [String : Any], completion: (Bool, (any Error)?) -> Void)](hkworkoutbuilder/updateactivity(uuid:adding:completion:).md)
  Adds metadata to a workout activity that you’ve already added to the workout builder.
- [func updateActivity(uuid: UUID, end: Date, completion: (Bool, (any Error)?) -> Void)](hkworkoutbuilder/updateactivity(uuid:end:completion:).md)
  Sets the end date for a workout activity that you’ve already added to the workout builder.
- [var workoutActivities: [HKWorkoutActivity]](hkworkoutbuilder/workoutactivities.md)
### Ending the workout
- [func endCollection(withEnd: Date, completion: (Bool, (any Error)?) -> Void)](hkworkoutbuilder/endcollection(withend:completion:).md)
  Stops the collection of data, sets the workout’s end date, and deactivates the workout builder.
- [var endDate: Date?](hkworkoutbuilder/enddate.md)
  The workout’s end date and time.
- [func finishWorkout(completion: (HKWorkout?, (any Error)?) -> Void)](hkworkoutbuilder/finishworkout(completion:).md)
  Creates the workout, using the samples and events added to the builder, and saves it to the HealthKit store.
- [func discardWorkout()](hkworkoutbuilder/discardworkout.md)
  Stops the collection of data and discards the current results without saving the workout.
### Accessing workout statistics
- [var allStatistics: [HKQuantityType : HKStatistics]](hkworkoutbuilder/allstatistics.md)
  A dictionary that contains all the statistics for the workout builder.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [HKLiveWorkoutBuilder](hkliveworkoutbuilder.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Adding samples to a workout](adding-samples-to-a-workout.md)
  Create associated samples that add details to a workout.
- [Accessing condensed workout samples](accessing-condensed-workout-samples.md)
  Read series data from condensed workouts.
- [Dividing a HealthKit workout into activities](dividing-a-healthkit-workout-into-activities.md)
  Partition multisport and interval workouts into activities that represent the different parts of the workout.
- [class HKWorkout](hkworkout.md)
  A workout sample that stores information about a single physical activity.
- [class HKWorkoutActivity](hkworkoutactivity.md)
  An object that describes an activity within a longer workout.
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder)*