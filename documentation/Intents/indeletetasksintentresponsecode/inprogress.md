# INDeleteTasksIntentResponseCode.inProgress

**Framework**: Intents  
**Kind**: case  
**Role**: Case

A response code that indicates deletion is still in progress.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0
- iPadOS 13.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
case inProgress
```

```c
INDeleteTasksIntentResponseCodeInProgress
```

## Discussion

Return this code if you began deleting tasks from the task list but didn’t confirm the process was complete. For example, when a server handles the deletion and you’ve not yet received a confirmation from that server. Configure a timer to fire if your server doesn’t return within a few seconds. Use your timer’s handler block to provide the in-progress response back to Siri.

## See Also

### Response state
- [INDeleteTasksIntentResponseCode.unspecified](./unspecified.md)
  A response code that indicates an unknown state.
- [INDeleteTasksIntentResponseCode.ready](./ready.md)
  A response code that indicates app readiness.
- [INDeleteTasksIntentResponseCode.success](./success.md)
  A response code that indicates your app succeeded.
- [INDeleteTasksIntentResponseCode.failure](./failure.md)
  A response code that indicates you were unable to delete the task.
- [INDeleteTasksIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  A response code that indicates the user must launch your app to delete the tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indeletetasksintentresponsecode/inprogress)*