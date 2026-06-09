# AudioContext.WorkoutIntensityLevel

**Framework**: App Intents  
**Kind**: struct

The intensity level of a workout session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct WorkoutIntensityLevel
```

#### Overview

Use this type to specify a workout intensity level when donating entities for workout contexts. You can also initialize it with an `HKWorkoutActivityType` to donate entities for a specific workout type.

## Topics

### Initializers
- [init(HKWorkoutActivityType)](audiocontext/workoutintensitylevel/init(_:).md)
  Creates an intensity level from an `HKWorkoutActivityType`.
- [init(rawValue: UInt)](audiocontext/workoutintensitylevel/init(rawvalue:).md)
### Instance Properties
- [let rawValue: UInt](audiocontext/workoutintensitylevel/rawvalue.md)
### Type Properties
- [static let high: AudioContext.WorkoutIntensityLevel](audiocontext/workoutintensitylevel/high.md)
  A high-intensity workout such as running, HIIT, or cross-training.
- [static let low: AudioContext.WorkoutIntensityLevel](audiocontext/workoutintensitylevel/low.md)
  A low-intensity workout such as yoga, stretching, or walking.
- [static let medium: AudioContext.WorkoutIntensityLevel](audiocontext/workoutintensitylevel/medium.md)
  A medium-intensity workout such as cycling, hiking, or swimming.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/audiocontext/workoutintensitylevel)*