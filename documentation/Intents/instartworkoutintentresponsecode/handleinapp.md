# INStartWorkoutIntentResponseCode.handleInApp

**Framework**: Intents  
**Kind**: case  
**Role**: Case

A response code that indicates you want to handle the intent in your app instead.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case handleInApp
```

```c
INStartWorkoutIntentResponseCodeHandleInApp
```

#### Discussion

Use this code when you want SiriKit to launch your app in the background so that you can handle the intent there. With this code, the user continues to interact with Siri, but your app has an opportunity to set up a workout session or any other information needed to manage the user’s workout more effectively.

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
- [INStartWorkoutIntentResponseCode.failure](./failure.md)
  A response code that indicates you were unable to start the specified workout.
- [INStartWorkoutIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  A response code that indicates the user must launch your app to start the workout.
- [INStartWorkoutIntentResponseCode.failureOngoingWorkout](./failureongoingworkout.md)
  A response code that indicates a workout is already in progress, so another can’t start.
- [INStartWorkoutIntentResponseCode.failureNoMatchingWorkout](./failurenomatchingworkout.md)
  A response code that indicates you didn’t find the specified workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartworkoutintentresponsecode/handleinapp)*