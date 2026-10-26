# INAddTasksIntentResponseCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user must add the tasks from within your app.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INAddTasksIntentResponseCode is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
case failureRequiringAppLaunch
```

```c
INAddTasksIntentResponseCodeFailureRequiringAppLaunch
```

#### Discussion

Use this response code when you can’t add the tasks from your Intents extension but the user can do so from your app. Don’t use this code for general errors or to force the user to launch your app.

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
- [INAddTasksIntentResponseCode.failure](./failure.md)
  You were unable to add the tasks to the task list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtasksintentresponsecode/failurerequiringapplaunch)*