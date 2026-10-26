# INAddTasksIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the state of the response.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INAddTasksIntentResponseCode is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
enum INAddTasksIntentResponseCode
```

```c
enum INAddTasksIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INAddTasksIntentResponseCode.unspecified](./inaddtasksintentresponsecode/unspecified.md)
  The response didn’t specify a response code.
- [INAddTasksIntentResponseCode.ready](./inaddtasksintentresponsecode/ready.md)
  You’re ready to handle the intent.
- [INAddTasksIntentResponseCode.inProgress](./inaddtasksintentresponsecode/inprogress.md)
  The addition of tasks into the task list is still in progress.
- [INAddTasksIntentResponseCode.success](./inaddtasksintentresponsecode/success.md)
  You successfully created the task.
- [INAddTasksIntentResponseCode.failure](./inaddtasksintentresponsecode/failure.md)
  You were unable to add the tasks to the task list.
- [INAddTasksIntentResponseCode.failureRequiringAppLaunch](./inaddtasksintentresponsecode/failurerequiringapplaunch.md)
  The user must add the tasks from within your app.
### Initializers
- [init?(rawValue: Int)](./inaddtasksintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INAddTasksIntentResponseCode](./inaddtasksintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtasksintentresponsecode)*