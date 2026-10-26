# INCancelWorkoutIntentResponseCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

A response code that indicates the user must launch your app to start the workout.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case failureRequiringAppLaunch
```

```c
INCancelWorkoutIntentResponseCodeFailureRequiringAppLaunch
```

#### Discussion

Use this code only when you cannot cancel the workout because of extenuating circumstances. For example, you might use this code if the user must log into your app before canceling workouts and is not currently logged in. Don’t use this response code for general errors or to force the user to launch your app.

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
- [INCancelWorkoutIntentResponseCode.handleInApp](./handleinapp.md)
  A response code that indicates you want to handle the intent in your app instead.
- [INCancelWorkoutIntentResponseCode.failure](./failure.md)
  A response code that indicates you were unable to start the specified workout.
- [INCancelWorkoutIntentResponseCode.failureNoMatchingWorkout](./failurenomatchingworkout.md)
  A response code that indicates you didn’t find the specified workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incancelworkoutintentresponsecode/failurerequiringapplaunch)*