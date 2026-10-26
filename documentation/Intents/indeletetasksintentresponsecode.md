# INDeleteTasksIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the response state.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0
- iPadOS 13.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
enum INDeleteTasksIntentResponseCode
```

```c
enum INDeleteTasksIntentResponseCode : NSInteger;
```

## Topics

### Response state
- [INDeleteTasksIntentResponseCode.unspecified](./indeletetasksintentresponsecode/unspecified.md)
  A response code that indicates an unknown state.
- [INDeleteTasksIntentResponseCode.ready](./indeletetasksintentresponsecode/ready.md)
  A response code that indicates app readiness.
- [INDeleteTasksIntentResponseCode.inProgress](./indeletetasksintentresponsecode/inprogress.md)
  A response code that indicates deletion is still in progress.
- [INDeleteTasksIntentResponseCode.success](./indeletetasksintentresponsecode/success.md)
  A response code that indicates your app succeeded.
- [INDeleteTasksIntentResponseCode.failure](./indeletetasksintentresponsecode/failure.md)
  A response code that indicates you were unable to delete the task.
- [INDeleteTasksIntentResponseCode.failureRequiringAppLaunch](./indeletetasksintentresponsecode/failurerequiringapplaunch.md)
  A response code that indicates the user must launch your app to delete the tasks.
### Initializers
- [init?(rawValue: Int)](./indeletetasksintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INDeleteTasksIntentResponseCode](./indeletetasksintentresponse/code.md)
  The code that indicates whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indeletetasksintentresponsecode)*