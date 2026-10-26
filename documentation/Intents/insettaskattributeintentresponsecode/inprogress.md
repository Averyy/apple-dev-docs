# INSetTaskAttributeIntentResponseCode.inProgress

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The modification of the task list is still in progress.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSetTaskAttributeIntentResponseCode is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
case inProgress
```

```c
INSetTaskAttributeIntentResponseCodeInProgress
```

#### Discussion

Return this code if you began adding modifying the task list but did not confirm that the process was complete. You might use this code when a server handles modifications and you have not yet received a confirmation from that server.

When handling the intent, you might want to first configure a timer to fire if your server does not return within a few seconds. Use your timer’s handler block to provide the in-progress response back to Siri.

## See Also

### Constants
- [INSetTaskAttributeIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a response code.
- [INSetTaskAttributeIntentResponseCode.ready](./ready.md)
  You are ready to handle the intent.
- [INSetTaskAttributeIntentResponseCode.success](./success.md)
  You successfully modified the task attributes.
- [INSetTaskAttributeIntentResponseCode.failure](./failure.md)
  You were unable to modify the task attributes.
- [INSetTaskAttributeIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must modify tasks from within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insettaskattributeintentresponsecode/inprogress)*