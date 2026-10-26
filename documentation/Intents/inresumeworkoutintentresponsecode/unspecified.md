# INResumeWorkoutIntentResponseCode.unspecified

**Framework**: Intents  
**Kind**: case  
**Role**: Case

A response code that indicates an unknown state.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case unspecified
```

```c
INResumeWorkoutIntentResponseCodeUnspecified
```

## See Also

### Response State
- [INResumeWorkoutIntentResponseCode.ready](./ready.md)
  A response code that indicates app readiness.
- [INResumeWorkoutIntentResponseCode.continueInApp](./continueinapp.md)
  A response code that indicates your app extension is ready to transfer control to the app to start the workout.
- [INResumeWorkoutIntentResponseCode.success](./success.md)
  A response code that indicates your app succeeded.
- [INResumeWorkoutIntentResponseCode.handleInApp](./handleinapp.md)
  A response code that indicates you want to handle the intent in your app instead.
- [INResumeWorkoutIntentResponseCode.failure](./failure.md)
  A response code that indicates you were unable to start the specified workout.
- [INResumeWorkoutIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  A response code that indicates the user must launch your app to start the workout.
- [INResumeWorkoutIntentResponseCode.failureNoMatchingWorkout](./failurenomatchingworkout.md)
  A response code that indicates you didn’t find the specified workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inresumeworkoutintentresponsecode/unspecified)*