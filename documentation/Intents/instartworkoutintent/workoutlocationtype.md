# workoutLocationType

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The location of the workout.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var workoutLocationType: INWorkoutLocationType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INWorkoutLocationType workoutLocationType;
```

*macOS*

```objc
@property (atomic, assign, readonly) INWorkoutLocationType workoutLocationType;
```

## Discussion

When you measure indoor and outdoor workouts differently, use this property to determine the workout’s location.

## See Also

### Specifying Workout Details
- [var workoutName: INSpeakableString?](./workoutname.md)
  The name of the workout.
- [var goalValue: Double?](./goalvalue-5oazy.md)
  The user-supplied numerical goal of the workout.
- [var workoutGoalUnitType: INWorkoutGoalUnitType](./workoutgoalunittype.md)
  The units associated with the workout goal.
- [var isOpenEnded: Bool?](./isopenended-8hecn.md)
  A Boolean value that indicates whether the workout is open ended.
- [goalValue](./goalvalue-1dzvb.md)
  The numerical goal of the workout.
- [isOpenEnded](./isopenended-avvd.md)
  A Boolean value indicating whether the workout is open ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartworkoutintent/workoutlocationtype)*