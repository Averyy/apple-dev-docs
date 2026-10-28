# HKWorkoutActivityType.swimBikeRun

**Framework**: HealthKit  
**Kind**: case  
**Role**: Case

The constant for multisport activities like triathlons.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
case swimBikeRun
```

```c
HKWorkoutActivityTypeSwimBikeRun
```

## Mentions

- [Dividing a HealthKit workout into activities](../dividing-a-healthkit-workout-into-activities.md)

## Discussion

Use this constant to create workouts that contain the [`HKWorkoutActivityType.swimming`](./swimming.md), [`HKWorkoutActivityType.cycling`](./cycling.md), and [`HKWorkoutActivityType.running`](./running.md) activities. These activities can happen in any order. For more information, see [`HKWorkoutActivity`](../hkworkoutactivity.md). HealthKit provides optimized calorie calculations for this activity based on the data from Apple Watch’s sensors.

## See Also

### Multisport activities
- [HKWorkoutActivityType.transition](./transition.md)
  A constant for the transition time between activities in a multisport workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/swimbikerun)*