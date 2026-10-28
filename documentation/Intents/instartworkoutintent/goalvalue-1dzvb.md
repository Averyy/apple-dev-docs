# goalValue

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The numerical goal of the workout.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSNumber * goalValue;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSNumber * goalValue;
```

## Discussion

If the user specified a goal, this property contains the numerical value of that goal. You get the units associated with this goal from the [`workoutGoalUnitType`](./workoutgoalunittype.md) property.

## See Also

### Specifying Workout Details
- [var workoutName: INSpeakableString?](./workoutname.md)
  The name of the workout.
- [var workoutGoalUnitType: INWorkoutGoalUnitType](./workoutgoalunittype.md)
  The units associated with the workout goal.
- [var workoutLocationType: INWorkoutLocationType](./workoutlocationtype.md)
  The location of the workout.
- [isOpenEnded](./isopenended-avvd.md)
  A Boolean value indicating whether the workout is open ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartworkoutintent/goalvalue-1dzvb)*