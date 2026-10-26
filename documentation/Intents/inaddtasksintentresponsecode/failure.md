# INAddTasksIntentResponseCode.failure

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You were unable to add the tasks to the task list.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INAddTasksIntentResponseCode is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
case failure
```

```c
INAddTasksIntentResponseCodeFailure
```

#### Discussion

Use this response code for both transient and unrecoverable errors that prevented you from adding the tasks to the task list.

## See Also

### Constants
- [INAddTasksIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a response code.
- [INAddTasksIntentResponseCode.ready](./ready.md)
  You’re ready to handle the intent.
- [INAddTasksIntentResponseCode.inProgress](./inprogress.md)
  The addition of tasks into the task list is still in progress.
- [INAddTasksIntentResponseCode.success](./success.md)
  You successfully created the task.
- [INAddTasksIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must add the tasks from within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtasksintentresponsecode/failure)*