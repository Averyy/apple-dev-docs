# INPauseWorkoutIntentResponseCode

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
enum INPauseWorkoutIntentResponseCode
```

```c
enum INPauseWorkoutIntentResponseCode : NSInteger;
```

## Topics

### Response State
- [INPauseWorkoutIntentResponseCode.unspecified](./inpauseworkoutintentresponsecode/unspecified.md)
  A response code that indicates an unknown state.
- [INPauseWorkoutIntentResponseCode.ready](./inpauseworkoutintentresponsecode/ready.md)
  A response code that indicates app readiness.
- [INPauseWorkoutIntentResponseCode.continueInApp](./inpauseworkoutintentresponsecode/continueinapp.md)
  A response code that indicates your app extension is ready to transfer control to the app to start the workout.
- [INPauseWorkoutIntentResponseCode.success](./inpauseworkoutintentresponsecode/success.md)
  A response code that indicates your app succeeded.
- [INPauseWorkoutIntentResponseCode.handleInApp](./inpauseworkoutintentresponsecode/handleinapp.md)
  A response code that indicates you want to handle the intent in your app instead.
- [INPauseWorkoutIntentResponseCode.failure](./inpauseworkoutintentresponsecode/failure.md)
  A response code that indicates you were unable to start the specified workout.
- [INPauseWorkoutIntentResponseCode.failureRequiringAppLaunch](./inpauseworkoutintentresponsecode/failurerequiringapplaunch.md)
  A response code that indicates the user must launch your app to start the workout.
- [INPauseWorkoutIntentResponseCode.failureNoMatchingWorkout](./inpauseworkoutintentresponsecode/failurenomatchingworkout.md)
  A response code that indicates you didn’t find the specified workout.
### Initializers
- [init?(rawValue: Int)](./inpauseworkoutintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INPauseWorkoutIntentResponseCode](./inpauseworkoutintentresponse/code.md)
  The code that indicates whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpauseworkoutintentresponsecode)*