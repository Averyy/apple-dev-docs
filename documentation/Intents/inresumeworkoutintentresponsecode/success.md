# INResumeWorkoutIntentResponseCode.success

**Framework**: Intents  
**Kind**: case  
**Role**: Case

A response code that indicates your app succeeded.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case success
```

```c
INResumeWorkoutIntentResponseCodeSuccess
```

#### Discussion

Use this code when your app successfully resumes the workout.

## See Also

### Response State
- [INResumeWorkoutIntentResponseCode.unspecified](./unspecified.md)
  A response code that indicates an unknown state.
- [INResumeWorkoutIntentResponseCode.ready](./ready.md)
  A response code that indicates app readiness.
- [INResumeWorkoutIntentResponseCode.continueInApp](./continueinapp.md)
  A response code that indicates your app extension is ready to transfer control to the app to start the workout.
- [INResumeWorkoutIntentResponseCode.handleInApp](./handleinapp.md)
  A response code that indicates you want to handle the intent in your app instead.
- [INResumeWorkoutIntentResponseCode.failure](./failure.md)
  A response code that indicates you were unable to start the specified workout.
- [INResumeWorkoutIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  A response code that indicates the user must launch your app to start the workout.
- [INResumeWorkoutIntentResponseCode.failureNoMatchingWorkout](./failurenomatchingworkout.md)
  A response code that indicates you didn’t find the specified workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inresumeworkoutintentresponsecode/success)*