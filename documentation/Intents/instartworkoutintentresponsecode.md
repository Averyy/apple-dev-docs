# INStartWorkoutIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the response state.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
enum INStartWorkoutIntentResponseCode
```

```c
enum INStartWorkoutIntentResponseCode : NSInteger;
```

## Topics

### Response State
- [INStartWorkoutIntentResponseCode.unspecified](./instartworkoutintentresponsecode/unspecified.md)
  A response code that indicates an unknown state.
- [INStartWorkoutIntentResponseCode.ready](./instartworkoutintentresponsecode/ready.md)
  A response code that indicates app readiness.
- [INStartWorkoutIntentResponseCode.continueInApp](./instartworkoutintentresponsecode/continueinapp.md)
  A response code that indicates your app extension is ready to transfer control to the app to start the workout.
- [INStartWorkoutIntentResponseCode.success](./instartworkoutintentresponsecode/success.md)
  A response code that indicates your app succeeded.
- [INStartWorkoutIntentResponseCode.handleInApp](./instartworkoutintentresponsecode/handleinapp.md)
  A response code that indicates you want to handle the intent in your app instead.
- [INStartWorkoutIntentResponseCode.failure](./instartworkoutintentresponsecode/failure.md)
  A response code that indicates you were unable to start the specified workout.
- [INStartWorkoutIntentResponseCode.failureRequiringAppLaunch](./instartworkoutintentresponsecode/failurerequiringapplaunch.md)
  A response code that indicates the user must launch your app to start the workout.
- [INStartWorkoutIntentResponseCode.failureOngoingWorkout](./instartworkoutintentresponsecode/failureongoingworkout.md)
  A response code that indicates a workout is already in progress, so another can’t start.
- [INStartWorkoutIntentResponseCode.failureNoMatchingWorkout](./instartworkoutintentresponsecode/failurenomatchingworkout.md)
  A response code that indicates you didn’t find the specified workout.
### Initializers
- [init?(rawValue: Int)](./instartworkoutintentresponsecode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Response Code
- [var code: INStartWorkoutIntentResponseCode](./instartworkoutintentresponse/code.md)
  The code that indicates whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartworkoutintentresponsecode)*