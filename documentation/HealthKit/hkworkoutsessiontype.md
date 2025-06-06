# HKWorkoutSessionType

**Framework**: HealthKit  
**Kind**: enum

The type of session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS ?+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
enum HKWorkoutSessionType
```

## Topics

### Types
- [HKWorkoutSessionType.mirrored](hkworkoutsessiontype/mirrored.md)
  A mirrored session, running on the companion iOS device.
- [HKWorkoutSessionType.primary](hkworkoutsessiontype/primary.md)
  A primary session running on watchOS.
### Initializers
- [init?(rawValue: Int)](hkworkoutsessiontype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
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
- [class HKWorkoutBuilder](hkworkoutbuilder.md)
  A builder object that incrementally constructs a workout.
- [class HKWorkoutType](hkworkouttype.md)
  A type that identifies samples that store information about a workout.
- [let HKWorkoutTypeIdentifier: String](hkworkouttypeidentifier.md)
  The workout type identifier.
- [enum HKWorkoutActivityType](hkworkoutactivitytype.md)
  The type of activity performed during a workout.
- [class HKWorkoutEvent](hkworkoutevent.md)
  An object representing an important event during a workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsessiontype)*