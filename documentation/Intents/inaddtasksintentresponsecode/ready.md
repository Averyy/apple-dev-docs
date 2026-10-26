# INAddTasksIntentResponseCode.ready

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You’re ready to handle the intent.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INAddTasksIntentResponseCode is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
case ready
```

```c
INAddTasksIntentResponseCodeReady
```

#### Discussion

Return this response code during the confirmation phase after you’ve verified that you’re able to add the tasks to the specified task list. Don’t return this response code when handling the intent; doing so causes the device to display an error.

## See Also

### Constants
- [INAddTasksIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a response code.
- [INAddTasksIntentResponseCode.inProgress](./inprogress.md)
  The addition of tasks into the task list is still in progress.
- [INAddTasksIntentResponseCode.success](./success.md)
  You successfully created the task.
- [INAddTasksIntentResponseCode.failure](./failure.md)
  You were unable to add the tasks to the task list.
- [INAddTasksIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must add the tasks from within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtasksintentresponsecode/ready)*