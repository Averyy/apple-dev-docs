# INCreateTaskListIntentResponseCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user must create the task list from within your app.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
case failureRequiringAppLaunch
```

```c
INCreateTaskListIntentResponseCodeFailureRequiringAppLaunch
```

## Discussion

Use this response code when you can’t create the task list from your Intents extension but the user can create it in your app. Don’t use this code for general errors or to force the user to launch your app.

## See Also

### Constants
- [INCreateTaskListIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a response code.
- [INCreateTaskListIntentResponseCode.ready](./ready.md)
  You’re ready to handle the intent.
- [INCreateTaskListIntentResponseCode.inProgress](./inprogress.md)
  Task list creation is still in progress.
- [INCreateTaskListIntentResponseCode.success](./success.md)
  You successfully created the task list.
- [INCreateTaskListIntentResponseCode.failure](./failure.md)
  You were unable to create the task list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatetasklistintentresponsecode/failurerequiringapplaunch)*