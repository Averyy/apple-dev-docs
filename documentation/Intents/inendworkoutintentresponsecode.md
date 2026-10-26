# INEndWorkoutIntentResponseCode

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
enum INEndWorkoutIntentResponseCode
```

```c
enum INEndWorkoutIntentResponseCode : NSInteger;
```

## Topics

### Response State
- [INEndWorkoutIntentResponseCode.unspecified](./inendworkoutintentresponsecode/unspecified.md)
  A response code that indicates an unknown state.
- [INEndWorkoutIntentResponseCode.ready](./inendworkoutintentresponsecode/ready.md)
  A response code that indicates app readiness.
- [INEndWorkoutIntentResponseCode.continueInApp](./inendworkoutintentresponsecode/continueinapp.md)
  A response code that indicates your app extension is ready to transfer control to the app to start the workout.
- [INEndWorkoutIntentResponseCode.success](./inendworkoutintentresponsecode/success.md)
  A response code that indicates your app succeeded.
- [INEndWorkoutIntentResponseCode.handleInApp](./inendworkoutintentresponsecode/handleinapp.md)
  A response code that indicates you want to handle the intent in your app instead.
- [INEndWorkoutIntentResponseCode.failure](./inendworkoutintentresponsecode/failure.md)
  A response code that indicates you were unable to start the specified workout.
- [INEndWorkoutIntentResponseCode.failureRequiringAppLaunch](./inendworkoutintentresponsecode/failurerequiringapplaunch.md)
  A response code that indicates the user must launch your app to start the workout.
- [INEndWorkoutIntentResponseCode.failureNoMatchingWorkout](./inendworkoutintentresponsecode/failurenomatchingworkout.md)
  A response code that indicates you didn’t find the specified workout.
### Initializers
- [init?(rawValue: Int)](./inendworkoutintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INEndWorkoutIntentResponseCode](./inendworkoutintentresponse/code.md)
  The code that indicates whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inendworkoutintentresponsecode)*