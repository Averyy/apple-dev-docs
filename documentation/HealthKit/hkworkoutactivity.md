# HKWorkoutActivity

**Framework**: HealthKit  
**Kind**: class

An object that describes an activity within a longer workout.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class HKWorkoutActivity
```

## Mentions

- [Dividing a HealthKit workout into activities](dividing-a-healthkit-workout-into-activities.md)

#### Overview

Workout activity objects partition a workout into a set of separate activities. For example, you can use workout activities to record the swim, bike, and running portions of a multisport event, like a triathlon, or to represent the active and rest periods during interval training. All [`HKWorkout`](hkworkout.md) instance have at least one, associated [`HKWorkoutActivity`](hkworkoutactivity.md). If you don’t explicitly set workout activities, HealthKit assigns a workout activity that matches the [`HKWorkout`](hkworkout.md) object’s activity type. For more information, see [`Dividing a HealthKit workout into activities`](dividing-a-healthkit-workout-into-activities.md).

## Topics

### Creating workout activities
- [init(workoutConfiguration: HKWorkoutConfiguration, start: Date, end: Date?, metadata: [String : Any]?)](hkworkoutactivity/init(workoutconfiguration:start:end:metadata:).md)
  Creates a workout activity using the provided configuration, start date, end date, and metadata.
### Accessing workout data
- [var uuid: UUID](hkworkoutactivity/uuid.md)
  The activity’s universally unique identifier (UUID).
- [var startDate: Date](hkworkoutactivity/startdate.md)
  The activitiy’s start date and time.
- [var endDate: Date?](hkworkoutactivity/enddate.md)
  The activity’s end date and time.
- [var duration: TimeInterval](hkworkoutactivity/duration.md)
  The activity’s duration, measured in seconds.
- [var allStatistics: [HKQuantityType : HKStatistics]](hkworkoutactivity/allstatistics.md)
  A dictionary that contains all the statistics for the activity.
- [func statistics(for: HKQuantityType) -> HKStatistics?](hkworkoutactivity/statistics(for:).md)
  Returns the activity’s statistics for the provided quantity type.
- [var metadata: [String : Any]?](hkworkoutactivity/metadata.md)
  Metadata that describes the activity.
- [var workoutConfiguration: HKWorkoutConfiguration](hkworkoutactivity/workoutconfiguration.md)
  The configuration information for this part of the workout.
- [var workoutEvents: [HKWorkoutEvent]](hkworkoutactivity/workoutevents.md)
  An array of events associated with the containing workout and occurring during the activity’s duration.
### Specifying predicate key paths
- [let HKPredicateKeyPathWorkoutActivity: String](hkpredicatekeypathworkoutactivity.md)
  The key path for accessing a specific workout activity.
- [let HKPredicateKeyPathWorkoutActivityType: String](hkpredicatekeypathworkoutactivitytype.md)
  The key path for accessing activities that match a workout activity type.
- [let HKPredicateKeyPathWorkoutActivityStartDate: String](hkpredicatekeypathworkoutactivitystartdate.md)
  The key path for accessing activities with a matching start date.
- [let HKPredicateKeyPathWorkoutActivityEndDate: String](hkpredicatekeypathworkoutactivityenddate.md)
  The key path for accessing activities with a matching end date.
- [let HKPredicateKeyPathWorkoutActivityDuration: String](hkpredicatekeypathworkoutactivityduration.md)
  The key path for accessing activities with a matching duration.
- [let HKPredicateKeyPathWorkoutActivityAverageQuantity: String](hkpredicatekeypathworkoutactivityaveragequantity.md)
  The key path for accessing activities with a matching average quantity.
- [let HKPredicateKeyPathWorkoutActivityMaximumQuantity: String](hkpredicatekeypathworkoutactivitymaximumquantity.md)
  The key path for accessing activities with a matching maximum quantity.
- [let HKPredicateKeyPathWorkoutActivityMinimumQuantity: String](hkpredicatekeypathworkoutactivityminimumquantity.md)
  The key path for accessing activities with a matching minimum quantity.
- [let HKPredicateKeyPathWorkoutActivitySumQuantity: String](hkpredicatekeypathworkoutactivitysumquantity.md)
  The key path for accessing activities with a matching sum.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
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
- [class HKWorkout](hkworkout.md)
  A workout sample that stores information about a single physical activity.
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutactivity)*