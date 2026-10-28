# INCancelWorkoutIntentResponseCode.handleInApp

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
INCancelWorkoutIntentResponseCodeHandleInApp
```

## Discussion

Use this code when you want SiriKit to launch your app in the background so that you can handle the intent there. With this code, the user continues to interact with Siri, but your app has an opportunity to end the workout session and update any other workout information.

## See Also

### Response State
- [INCancelWorkoutIntentResponseCode.unspecified](./unspecified.md)
  A response code that indicates an unknown state.
- [INCancelWorkoutIntentResponseCode.ready](./ready.md)
  A response code that indicates app readiness.
- [INCancelWorkoutIntentResponseCode.continueInApp](./continueinapp.md)
  A response code that indicates your app extension is ready to transfer control to the app to start the workout.
- [INCancelWorkoutIntentResponseCode.success](./success.md)
  A response code that indicates your app succeeded.
- [INCancelWorkoutIntentResponseCode.failure](./failure.md)
  A response code that indicates you were unable to start the specified workout.
- [INCancelWorkoutIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  A response code that indicates the user must launch your app to start the workout.
- [INCancelWorkoutIntentResponseCode.failureNoMatchingWorkout](./failurenomatchingworkout.md)
  A response code that indicates you didn’t find the specified workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incancelworkoutintentresponsecode/handleinapp)*