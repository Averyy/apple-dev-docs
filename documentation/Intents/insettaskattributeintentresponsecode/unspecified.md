# INSetTaskAttributeIntentResponseCode.unspecified

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The response didn’t specify a response code.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSetTaskAttributeIntentResponseCode is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
case unspecified
```

```c
INSetTaskAttributeIntentResponseCodeUnspecified
```

## Discussion

Don’t return this response code when handling the intent; doing so causes the device to display an error.

## See Also

### Constants
- [INSetTaskAttributeIntentResponseCode.ready](./ready.md)
  You are ready to handle the intent.
- [INSetTaskAttributeIntentResponseCode.inProgress](./inprogress.md)
  The modification of the task list is still in progress.
- [INSetTaskAttributeIntentResponseCode.success](./success.md)
  You successfully modified the task attributes.
- [INSetTaskAttributeIntentResponseCode.failure](./failure.md)
  You were unable to modify the task attributes.
- [INSetTaskAttributeIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must modify tasks from within your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insettaskattributeintentresponsecode/unspecified)*