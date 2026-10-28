# INAddTasksIntentResponseCode.inProgress

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The addition of tasks into the task list is still in progress.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INAddTasksIntentResponseCode is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
case inProgress
```

```c
INAddTasksIntentResponseCodeInProgress
```

## Discussion

Return this code if you began adding tasks to the task list but didn’t confirm that the process was complete. You might use this code when a server handles the creation and you’ve not yet received a confirmation from that server.

When handling the intent, you might want to first configure a timer to fire if your server doesn’t return within a few seconds. Use your timer’s handler block to provide the in-progress response back to Siri.

## See Also

### Constants
- [INAddTasksIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a response code.
- [INAddTasksIntentResponseCode.ready](./ready.md)
  You’re ready to handle the intent.
- [INAddTasksIntentResponseCode.success](./success.md)
  You successfully created the task.
- [INAddTasksIntentResponseCode.failure](./failure.md)
  You were unable to add the tasks to the task list.
- [INAddTasksIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must add the tasks from within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtasksintentresponsecode/inprogress)*