# INCreateTaskListIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the state of the response.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
enum INCreateTaskListIntentResponseCode
```

```c
enum INCreateTaskListIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INCreateTaskListIntentResponseCode.unspecified](./increatetasklistintentresponsecode/unspecified.md)
  The response didn’t specify a response code.
- [INCreateTaskListIntentResponseCode.ready](./increatetasklistintentresponsecode/ready.md)
  You’re ready to handle the intent.
- [INCreateTaskListIntentResponseCode.inProgress](./increatetasklistintentresponsecode/inprogress.md)
  Task list creation is still in progress.
- [INCreateTaskListIntentResponseCode.success](./increatetasklistintentresponsecode/success.md)
  You successfully created the task list.
- [INCreateTaskListIntentResponseCode.failure](./increatetasklistintentresponsecode/failure.md)
  You were unable to create the task list.
- [INCreateTaskListIntentResponseCode.failureRequiringAppLaunch](./increatetasklistintentresponsecode/failurerequiringapplaunch.md)
  The user must create the task list from within your app.
### Initializers
- [init?(rawValue: Int)](./increatetasklistintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INCreateTaskListIntentResponseCode](./increatetasklistintentresponse/code.md)
  The code indicating whether your app successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatetasklistintentresponsecode)*