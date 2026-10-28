# INSnoozeTasksIntentResponseCode.inProgress

**Framework**: Intents  
**Kind**: case  
**Role**: Case

A response code that indicates deletion is still in progress.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

> **Deprecated**: INSnoozeTasksIntentResponseCode is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
case inProgress
```

```c
INSnoozeTasksIntentResponseCodeInProgress
```

## Discussion

Return this code if you began snoozing tasks in the task list but didn’t confirm that the process was complete. For example, when a server handles the snoozing and you’ve not yet received a confirmation from that server. Configure a timer to fire if your server doesn’t return within a few seconds. Use your timer’s handler block to provide the in-progress response back to Siri.

## See Also

### Response State
- [INSnoozeTasksIntentResponseCode.unspecified](./unspecified.md)
  A response code that indicates an unknown state.
- [INSnoozeTasksIntentResponseCode.ready](./ready.md)
  A response code that indicates app readiness.
- [INSnoozeTasksIntentResponseCode.success](./success.md)
  A response code that indicates your app succeeded.
- [INSnoozeTasksIntentResponseCode.failure](./failure.md)
  A response code that indicates you were unable to snooze the task.
- [INSnoozeTasksIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  A response code that indicates the user must launch your app to snooze the tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insnoozetasksintentresponsecode/inprogress)*