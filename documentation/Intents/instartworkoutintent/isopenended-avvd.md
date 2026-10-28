# isOpenEnded

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the workout is open ended.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * isOpenEnded;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSNumber * isOpenEnded;
```

## Discussion

This property contains a Boolean whose value is [`true`](../../Swift/true.md) when the user wants an open-ended workout instead of one with a specific goal.

## See Also

### Specifying Workout Details
- [var workoutName: INSpeakableString?](./workoutname.md)
  The name of the workout.
- [goalValue](./goalvalue-1dzvb.md)
  The numerical goal of the workout.
- [var workoutGoalUnitType: INWorkoutGoalUnitType](./workoutgoalunittype.md)
  The units associated with the workout goal.
- [var workoutLocationType: INWorkoutLocationType](./workoutlocationtype.md)
  The location of the workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartworkoutintent/isopenended-avvd)*