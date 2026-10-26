# INDeleteTasksIntentResponseCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

A response code that indicates the user must launch your app to delete the tasks.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0
- iPadOS 13.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
case failureRequiringAppLaunch
```

```c
INDeleteTasksIntentResponseCodeFailureRequiringAppLaunch
```

#### Discussion

Use this response code when you can’t delete the tasks from your Intents extension, but the user can do so from your app. Don’t use this code for general errors or to force the user to launch your app.

## See Also

### Response state
- [INDeleteTasksIntentResponseCode.unspecified](./unspecified.md)
  A response code that indicates an unknown state.
- [INDeleteTasksIntentResponseCode.ready](./ready.md)
  A response code that indicates app readiness.
- [INDeleteTasksIntentResponseCode.inProgress](./inprogress.md)
  A response code that indicates deletion is still in progress.
- [INDeleteTasksIntentResponseCode.success](./success.md)
  A response code that indicates your app succeeded.
- [INDeleteTasksIntentResponseCode.failure](./failure.md)
  A response code that indicates you were unable to delete the task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indeletetasksintentresponsecode/failurerequiringapplaunch)*