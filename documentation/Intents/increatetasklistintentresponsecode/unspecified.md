# INCreateTaskListIntentResponseCode.unspecified

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The response didn’t specify a response code.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
case unspecified
```

```c
INCreateTaskListIntentResponseCodeUnspecified
```

## Discussion

Don’t return this response code when handling the intent; doing so causes the device to display an error.

## See Also

### Constants
- [INCreateTaskListIntentResponseCode.ready](./ready.md)
  You’re ready to handle the intent.
- [INCreateTaskListIntentResponseCode.inProgress](./inprogress.md)
  Task list creation is still in progress.
- [INCreateTaskListIntentResponseCode.success](./success.md)
  You successfully created the task list.
- [INCreateTaskListIntentResponseCode.failure](./failure.md)
  You were unable to create the task list.
- [INCreateTaskListIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must create the task list from within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/increatetasklistintentresponsecode/unspecified)*