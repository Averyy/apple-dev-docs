# INSetTaskAttributeIntentResponseCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user must modify tasks from within your app.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSetTaskAttributeIntentResponseCode is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
case failureRequiringAppLaunch
```

```c
INSetTaskAttributeIntentResponseCodeFailureRequiringAppLaunch
```

## Discussion

Use this response code when you cannot modify task attributes from your Intents extension but the user can do so from your app. Do not use this code for general errors or to force the user to launch your app.

## See Also

### Constants
- [INSetTaskAttributeIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a response code.
- [INSetTaskAttributeIntentResponseCode.ready](./ready.md)
  You are ready to handle the intent.
- [INSetTaskAttributeIntentResponseCode.inProgress](./inprogress.md)
  The modification of the task list is still in progress.
- [INSetTaskAttributeIntentResponseCode.success](./success.md)
  You successfully modified the task attributes.
- [INSetTaskAttributeIntentResponseCode.failure](./failure.md)
  You were unable to modify the task attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insettaskattributeintentresponsecode/failurerequiringapplaunch)*