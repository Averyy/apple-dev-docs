# isOpenEnded

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the workout is open ended.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- watchOS 3.2+

## Declaration

```swift
@nonobjc
final var isOpenEnded: Bool? { get }
```

#### Discussion

This property contains a Boolean whose value is [`true`](../../Swift/true.md) when the user wants an open-ended workout instead of a specific-goal workout.

## See Also

### Specifying Workout Details
- [var workoutName: INSpeakableString?](./workoutname.md)
  The name of the workout.
- [var goalValue: Double?](./goalvalue-5oazy.md)
  The user-supplied numerical goal of the workout.
- [var workoutGoalUnitType: INWorkoutGoalUnitType](./workoutgoalunittype.md)
  The units associated with the workout goal.
- [var workoutLocationType: INWorkoutLocationType](./workoutlocationtype.md)
  The location of the workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartworkoutintent/isopenended-8hecn)*