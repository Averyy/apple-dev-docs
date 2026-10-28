# AudioContext.WorkoutIntensityLevel

**Framework**: App Intents  
**Kind**: struct  
**Role**: Structure

The intensity level of a workout session.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct WorkoutIntensityLevel
```

## Overview

Use this type to specify a workout intensity level when donating entities for workout contexts. You can also initialize it with an `HKWorkoutActivityType` to donate entities for a specific workout type.

## Topics

### Initializers
- [init(HKWorkoutActivityType)](./workoutintensitylevel/init%28_%29.md)
  Creates an intensity level from an `HKWorkoutActivityType`.
- [init(rawValue: UInt)](./workoutintensitylevel/init%28rawvalue%29.md)
### Instance Properties
- [let rawValue: UInt](./workoutintensitylevel/rawvalue.md)
### Type Properties
- [static let high: AudioContext.WorkoutIntensityLevel](./workoutintensitylevel/high.md)
  A high-intensity workout such as running, HIIT, or cross-training.
- [static let low: AudioContext.WorkoutIntensityLevel](./workoutintensitylevel/low.md)
  A low-intensity workout such as yoga, stretching, or walking.
- [static let medium: AudioContext.WorkoutIntensityLevel](./workoutintensitylevel/medium.md)
  A medium-intensity workout such as cycling, hiking, or swimming.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/audiocontext/workoutintensitylevel)*