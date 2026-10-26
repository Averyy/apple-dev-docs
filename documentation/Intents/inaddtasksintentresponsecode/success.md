# INAddTasksIntentResponseCode.success

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You successfully created the task.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INAddTasksIntentResponseCode is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
case success
```

```c
INAddTasksIntentResponseCodeSuccess
```

#### Discussion

Use this code after adding the tasks to the task list successfully. Your response should contain the details of the task list and tasks that you changed.

## See Also

### Constants
- [INAddTasksIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a response code.
- [INAddTasksIntentResponseCode.ready](./ready.md)
  You’re ready to handle the intent.
- [INAddTasksIntentResponseCode.inProgress](./inprogress.md)
  The addition of tasks into the task list is still in progress.
- [INAddTasksIntentResponseCode.failure](./failure.md)
  You were unable to add the tasks to the task list.
- [INAddTasksIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must add the tasks from within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtasksintentresponsecode/success)*