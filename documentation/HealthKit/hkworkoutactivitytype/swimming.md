# HKWorkoutActivityType.swimming

**Framework**: HealthKit  
**Kind**: case  
**Role**: Case

The constant for swimming.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case swimming
```

```c
HKWorkoutActivityTypeSwimming
```

## Mentions

- [Dividing a HealthKit workout into activities](../dividing-a-healthkit-workout-into-activities.md)

## Discussion

If your app uses the [`HKWorkoutActivityType.swimming`](./swimming.md) or [`HKWorkoutActivityType.other`](./other.md) activity type, you must explain how your app calculates workout data when sensor information is not available. For more information, see the [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/watchos/interaction/workout/). HealthKit provides optimized calorie calculations for this activity based on the data from Apple Watch’s sensors.

## See Also

### Water activities
- [HKWorkoutActivityType.paddleSports](./paddlesports.md)
  The constant for canoeing, kayaking, paddling an outrigger, paddling a stand-up paddle board, and related sports.
- [HKWorkoutActivityType.rowing](./rowing.md)
  The constant for rowing.
- [HKWorkoutActivityType.sailing](./sailing.md)
  The constant for sailing.
- [HKWorkoutActivityType.surfingSports](./surfingsports.md)
  The constant for a variety of surf sports, including surfing, kite surfing, and wind surfing.
- [HKWorkoutActivityType.underwaterDiving](./underwaterdiving.md)
  The constant for underwater diving.
- [HKWorkoutActivityType.waterFitness](./waterfitness.md)
  The constant for aerobic exercise performed in shallow water.
- [HKWorkoutActivityType.waterPolo](./waterpolo.md)
  The constant for playing water polo.
- [HKWorkoutActivityType.waterSports](./watersports.md)
  The constant for a variety of water sports, including water skiing, wake boarding, and related activities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/swimming)*