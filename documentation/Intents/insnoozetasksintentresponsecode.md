# INSnoozeTasksIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the response state.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

> **Deprecated**: INSnoozeTasksIntentResponseCode is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
enum INSnoozeTasksIntentResponseCode
```

```c
enum INSnoozeTasksIntentResponseCode : NSInteger;
```

## Topics

### Response State
- [INSnoozeTasksIntentResponseCode.unspecified](./insnoozetasksintentresponsecode/unspecified.md)
  A response code that indicates an unknown state.
- [INSnoozeTasksIntentResponseCode.ready](./insnoozetasksintentresponsecode/ready.md)
  A response code that indicates app readiness.
- [INSnoozeTasksIntentResponseCode.inProgress](./insnoozetasksintentresponsecode/inprogress.md)
  A response code that indicates deletion is still in progress.
- [INSnoozeTasksIntentResponseCode.success](./insnoozetasksintentresponsecode/success.md)
  A response code that indicates your app succeeded.
- [INSnoozeTasksIntentResponseCode.failure](./insnoozetasksintentresponsecode/failure.md)
  A response code that indicates you were unable to snooze the task.
- [INSnoozeTasksIntentResponseCode.failureRequiringAppLaunch](./insnoozetasksintentresponsecode/failurerequiringapplaunch.md)
  A response code that indicates the user must launch your app to snooze the tasks.
### Initializers
- [init?(rawValue: Int)](./insnoozetasksintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INSnoozeTasksIntentResponseCode](./insnoozetasksintentresponse/code.md)
  The code that indicates whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insnoozetasksintentresponsecode)*