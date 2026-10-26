# INCancelWorkoutIntentResponseCode.failure

**Framework**: Intents  
**Kind**: case  
**Role**: Case

A response code that indicates you were unable to start the specified workout.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case failure
```

```c
INCancelWorkoutIntentResponseCodeFailure
```

#### Discussion

Use this code for both transient and unrecoverable errors that prevented you from performing the task.

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
- [INCancelWorkoutIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  A response code that indicates the user must launch your app to start the workout.
- [INCancelWorkoutIntentResponseCode.failureNoMatchingWorkout](./failurenomatchingworkout.md)
  A response code that indicates you didn’t find the specified workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incancelworkoutintentresponsecode/failure)*