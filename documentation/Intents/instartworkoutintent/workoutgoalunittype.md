# workoutGoalUnitType

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The units associated with the workout goal.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var workoutGoalUnitType: INWorkoutGoalUnitType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INWorkoutGoalUnitType workoutGoalUnitType;
```

*macOS*

```objc
@property (atomic, assign, readonly) INWorkoutGoalUnitType workoutGoalUnitType;
```

## Discussion

If the user specified a goal, this property contains the units for measuring that goal. The units reflect a distance, a time, or a unit of energy. You get the goal’s numerical value from the [`goalValue`](./goalvalue-1dzvb.md) property.

## See Also

### Specifying Workout Details
- [var workoutName: INSpeakableString?](./workoutname.md)
  The name of the workout.
- [var goalValue: Double?](./goalvalue-5oazy.md)
  The user-supplied numerical goal of the workout.
- [var workoutLocationType: INWorkoutLocationType](./workoutlocationtype.md)
  The location of the workout.
- [var isOpenEnded: Bool?](./isopenended-8hecn.md)
  A Boolean value that indicates whether the workout is open ended.
- [goalValue](./goalvalue-1dzvb.md)
  The numerical goal of the workout.
- [isOpenEnded](./isopenended-avvd.md)
  A Boolean value indicating whether the workout is open ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartworkoutintent/workoutgoalunittype)*