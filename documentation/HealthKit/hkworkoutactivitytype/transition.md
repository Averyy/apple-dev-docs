# HKWorkoutActivityType.transition

**Framework**: HealthKit  
**Kind**: case  
**Role**: Case

A constant for the transition time between activities in a multisport workout.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
case transition
```

```c
HKWorkoutActivityTypeTransition
```

## Mentions

- [Dividing a HealthKit workout into activities](../dividing-a-healthkit-workout-into-activities.md)

#### Discussion

Use this constant to create an [`HKWorkoutActivity`](../hkworkoutactivity.md) instance that represents the transition between sports in a [`HKWorkoutActivityType.swimBikeRun`](./swimbikerun.md) workout.

## See Also

### Multisport activities
- [HKWorkoutActivityType.swimBikeRun](./swimbikerun.md)
  The constant for multisport activities like triathlons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/transition)*