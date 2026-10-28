# INCreateTaskListIntentResponseCode.success

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You successfully created the task list.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
case success
```

```c
INCreateTaskListIntentResponseCodeSuccess
```

## Discussion

Use this code after creating the task list successfully. Your response should contain the details of the task list that you created.

## See Also

### Constants
- [INCreateTaskListIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a response code.
- [INCreateTaskListIntentResponseCode.ready](./ready.md)
  You’re ready to handle the intent.
- [INCreateTaskListIntentResponseCode.inProgress](./inprogress.md)
  Task list creation is still in progress.
- [INCreateTaskListIntentResponseCode.failure](./failure.md)
  You were unable to create the task list.
- [INCreateTaskListIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must create the task list from within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatetasklistintentresponsecode/success)*