# INPauseWorkoutIntentResponseCode.continueInApp

**Framework**: Intents  
**Kind**: case  
**Role**: Case

A response code that indicates your app extension is ready to transfer control to the app to start the workout.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

> **Deprecated**: Use [`INPauseWorkoutIntentResponseCode.handleInApp`](./handleinapp.md) instead.

## Declaration

```swift
case continueInApp
```

```c
INPauseWorkoutIntentResponseCodeContinueInApp
```

#### Discussion

Upon returning this code, SiriKit launches your app and passes it the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object you provided at initialization time. (If you didn’t provide a user activity object, SiriKit creates one for you). SiriKit adds an [`INInteraction`](../ininteraction.md) object with the intent and your response to the user activity object before delivering it. Your app should use the information in the user activity object to pause the workout.

## See Also

### Response State
- [INPauseWorkoutIntentResponseCode.unspecified](./unspecified.md)
  A response code that indicates an unknown state.
- [INPauseWorkoutIntentResponseCode.ready](./ready.md)
  A response code that indicates app readiness.
- [INPauseWorkoutIntentResponseCode.success](./success.md)
  A response code that indicates your app succeeded.
- [INPauseWorkoutIntentResponseCode.handleInApp](./handleinapp.md)
  A response code that indicates you want to handle the intent in your app instead.
- [INPauseWorkoutIntentResponseCode.failure](./failure.md)
  A response code that indicates you were unable to start the specified workout.
- [INPauseWorkoutIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  A response code that indicates the user must launch your app to start the workout.
- [INPauseWorkoutIntentResponseCode.failureNoMatchingWorkout](./failurenomatchingworkout.md)
  A response code that indicates you didn’t find the specified workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpauseworkoutintentresponsecode/continueinapp)*