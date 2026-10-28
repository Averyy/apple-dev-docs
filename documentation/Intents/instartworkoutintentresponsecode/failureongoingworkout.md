# INStartWorkoutIntentResponseCode.failureOngoingWorkout

**Framework**: Intents  
**Kind**: case  
**Role**: Case

A response code that indicates a workout is already in progress, so another can’t start.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case failureOngoingWorkout
```

```c
INStartWorkoutIntentResponseCodeFailureOngoingWorkout
```

## Discussion

Use this code when the user is already in the middle of a workout.

## See Also

### Response State
- [INStartWorkoutIntentResponseCode.unspecified](./unspecified.md)
  A response code that indicates an unknown state.
- [INStartWorkoutIntentResponseCode.ready](./ready.md)
  A response code that indicates app readiness.
- [INStartWorkoutIntentResponseCode.continueInApp](./continueinapp.md)
  A response code that indicates your app extension is ready to transfer control to the app to start the workout.
- [INStartWorkoutIntentResponseCode.success](./success.md)
  A response code that indicates your app succeeded.
- [INStartWorkoutIntentResponseCode.handleInApp](./handleinapp.md)
  A response code that indicates you want to handle the intent in your app instead.
- [INStartWorkoutIntentResponseCode.failure](./failure.md)
  A response code that indicates you were unable to start the specified workout.
- [INStartWorkoutIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  A response code that indicates the user must launch your app to start the workout.
- [INStartWorkoutIntentResponseCode.failureNoMatchingWorkout](./failurenomatchingworkout.md)
  A response code that indicates you didn’t find the specified workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartworkoutintentresponsecode/failureongoingworkout)*