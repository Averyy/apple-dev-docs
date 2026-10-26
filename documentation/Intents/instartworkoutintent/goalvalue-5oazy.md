# goalValue

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The user-supplied numerical goal of the workout.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- watchOS 3.2+

## Declaration

```swift
@nonobjc
final var goalValue: Double? { get }
```

#### Discussion

If the user specified a goal, this property contains the numerical value of that goal. For example, if the user specifies a 40 minute workout then this property has the value `40`. You get the units associated with this goal from the [`workoutGoalUnitType`](./workoutgoalunittype.md) property.

## See Also

### Specifying Workout Details
- [var workoutName: INSpeakableString?](./workoutname.md)
  The name of the workout.
- [var workoutGoalUnitType: INWorkoutGoalUnitType](./workoutgoalunittype.md)
  The units associated with the workout goal.
- [var workoutLocationType: INWorkoutLocationType](./workoutlocationtype.md)
  The location of the workout.
- [var isOpenEnded: Bool?](./isopenended-8hecn.md)
  A Boolean value that indicates whether the workout is open ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartworkoutintent/goalvalue-5oazy)*