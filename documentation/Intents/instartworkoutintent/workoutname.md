# workoutName

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The name of the workout.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
@NSCopying
var workoutName: INSpeakableString? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INSpeakableString * workoutName;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INSpeakableString * workoutName;
```

## Discussion

If the user requested a specific workout, this property contains the name of that workout. The workout name can be user-specified, a workout name defined in your app’s global vocabulary file, or a custom workout name spoken by the user.

## See Also

### Specifying Workout Details
- [var goalValue: Double?](./goalvalue-5oazy.md)
  The user-supplied numerical goal of the workout.
- [var workoutGoalUnitType: INWorkoutGoalUnitType](./workoutgoalunittype.md)
  The units associated with the workout goal.
- [var workoutLocationType: INWorkoutLocationType](./workoutlocationtype.md)
  The location of the workout.
- [var isOpenEnded: Bool?](./isopenended-8hecn.md)
  A Boolean value that indicates whether the workout is open ended.
- [goalValue](./goalvalue-1dzvb.md)
  The numerical goal of the workout.
- [isOpenEnded](./isopenended-avvd.md)
  A Boolean value indicating whether the workout is open ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartworkoutintent/workoutname)*