# INCreateTaskListIntentResponseCode.ready

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You’re ready to handle the intent.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
case ready
```

```c
INCreateTaskListIntentResponseCodeReady
```

## Discussion

Return this response code during the confirmation phase after you’ve verified that you’re able to create the task list. Don’t return this response code when handling the intent; doing so causes the device to display an error.

## See Also

### Constants
- [INCreateTaskListIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a response code.
- [INCreateTaskListIntentResponseCode.inProgress](./inprogress.md)
  Task list creation is still in progress.
- [INCreateTaskListIntentResponseCode.success](./success.md)
  You successfully created the task list.
- [INCreateTaskListIntentResponseCode.failure](./failure.md)
  You were unable to create the task list.
- [INCreateTaskListIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must create the task list from within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatetasklistintentresponsecode/ready)*