# INCreateTaskListIntentResponseCode.inProgress

**Framework**: Intents  
**Kind**: case  
**Role**: Case

Task list creation is still in progress.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
case inProgress
```

```c
INCreateTaskListIntentResponseCodeInProgress
```

#### Discussion

Return this code if you initiated the task list creation process but didn’t receive a timely response. You might use this code when a server handles creation and you haven’t yet received a confirmation from that server.

When handling the intent, you might want to first configure a timer to fire if your server doesn’t return within a few seconds. Use your timer’s handler block to provide the in-progress response back to Siri.

## See Also

### Constants
- [INCreateTaskListIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a response code.
- [INCreateTaskListIntentResponseCode.ready](./ready.md)
  You’re ready to handle the intent.
- [INCreateTaskListIntentResponseCode.success](./success.md)
  You successfully created the task list.
- [INCreateTaskListIntentResponseCode.failure](./failure.md)
  You were unable to create the task list.
- [INCreateTaskListIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must create the task list from within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatetasklistintentresponsecode/inprogress)*