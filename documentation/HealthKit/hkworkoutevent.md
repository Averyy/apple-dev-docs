# HKWorkoutEvent

**Framework**: HealthKit  
**Kind**: class

An object representing an important event during a workout.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HKWorkoutEvent
```

#### Overview

You can use workout events to toggle a workout between an active and an inactive state, or to mark points of interest during a workout.

Workouts start in an active state. A pause event switches it to an inactive state; a resume event switches it back to an active state. Adding a pause event when the workout is already inactive, or a resume event when the workout is already active, does not affect the workout’s state. These events are ignored.

The lap, segment, and marker events are used to identify periods of interest during a workout. Use lap events to partition a workout into segments of equal distance. Segment events mark important periods during the workout, while markers identify important points in time.

## Topics

### Creating workout events
- [convenience init(type: HKWorkoutEventType, dateInterval: DateInterval, metadata: [String : Any]?)](hkworkoutevent/init(type:dateinterval:metadata:).md)
  Instantiates and returns a new workout event with the specified type, date interval, and metadata.
### Getting property data
- [var dateInterval: DateInterval](hkworkoutevent/dateinterval.md)
  The time and duration of the event.
- [var type: HKWorkoutEventType](hkworkoutevent/type.md)
  The type of workout event.
- [var metadata: [String : Any]?](hkworkoutevent/metadata.md)
  The metadata associated with the workout event.
### Determining the event type
- [enum HKWorkoutEventType](hkworkouteventtype.md)
  Constants that represent events occurring during a workout.
### Deprecated
- [convenience init(type: HKWorkoutEventType, date: Date)](hkworkoutevent/init(type:date:).md)
  Instantiates and returns a new workout event with the specified type and date.
- [convenience init(type: HKWorkoutEventType, date: Date, metadata: [String : Any])](hkworkoutevent/init(type:date:metadata:).md)
  Instantiates and returns a new workout event with the specified type, date, and metadata.
- [var date: Date](hkworkoutevent/date.md)
  The time when the transition occurred.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutevent)*