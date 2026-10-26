# INSnoozeTasksIntentResponseCode.failure

**Framework**: Intents  
**Kind**: case  
**Role**: Case

A response code that indicates you were unable to snooze the task.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

> **Deprecated**: INSnoozeTasksIntentResponseCode is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
case failure
```

```c
INSnoozeTasksIntentResponseCodeFailure
```

#### Discussion

Use this response code for both transient and unrecoverable errors that prevent you from snoozing the tasks in the task list.

## See Also

### Response State
- [INSnoozeTasksIntentResponseCode.unspecified](./unspecified.md)
  A response code that indicates an unknown state.
- [INSnoozeTasksIntentResponseCode.ready](./ready.md)
  A response code that indicates app readiness.
- [INSnoozeTasksIntentResponseCode.inProgress](./inprogress.md)
  A response code that indicates deletion is still in progress.
- [INSnoozeTasksIntentResponseCode.success](./success.md)
  A response code that indicates your app succeeded.
- [INSnoozeTasksIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  A response code that indicates the user must launch your app to snooze the tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insnoozetasksintentresponsecode/failure)*