# initWithWorkoutName:goalValue:workoutGoalUnitType:workoutLocationType:isOpenEnded:

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Initializes an intent object with the specified workout information.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```objc
- (instancetype) initWithWorkoutName:(INSpeakableString *) workoutName goalValue:(NSNumber *) goalValue workoutGoalUnitType:(INWorkoutGoalUnitType) workoutGoalUnitType workoutLocationType:(INWorkoutLocationType) workoutLocationType isOpenEnded:(NSNumber *) isOpenEnded;
```

## Return Value

An initialized intent object or `nil` if the object could not be created.

## Discussion

Normally, you do not create instances of this class yourself. Instead, Siri creates instances when the user asks to start a workout. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `workoutName`: The name of the workout. This string can contain a custom workout name, a user-specific workout name, or one of the workout names defined in your app’s global vocabulary file.
- `goalValue`: The numerical portion of the user’s goal. This parameter works in conjunction with the `workoutGoalUnitType` parameter to define the user’s goal for the workout.
- `workoutGoalUnitType`: The units to apply to the `goalValue` parameter.
- `workoutLocationType`: The location of the workout.
- `isOpenEnded`: A Boolean indicating whether the workout ends when the specified goal is met. Specify [`false`](../../Swift/false.md) if the workout should end when the specified goal is met.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartworkoutintent/initwithworkoutname:goalvalue:workoutgoalunittype:workoutlocationtype:isopenended:)*