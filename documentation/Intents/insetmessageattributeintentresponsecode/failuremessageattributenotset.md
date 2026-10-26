# INSetMessageAttributeIntentResponseCode.failureMessageAttributeNotSet

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The message attributes couldn’t be modified.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case failureMessageAttributeNotSet
```

```c
INSetMessageAttributeIntentResponseCodeFailureMessageAttributeNotSet
```

#### Discussion

Use this response code when you were unable to modify the attributes of one or more messages.

## See Also

### Response State
- [INSetMessageAttributeIntentResponseCode.unspecified](./unspecified.md)
  An unknown response code.
- [INSetMessageAttributeIntentResponseCode.ready](./ready.md)
  The app is ready to handle the intent.
- [INSetMessageAttributeIntentResponseCode.inProgress](./inprogress.md)
  You are ready to handle the intent.
- [INSetMessageAttributeIntentResponseCode.success](./success.md)
  You successfully handled the intent.
- [INSetMessageAttributeIntentResponseCode.failure](./failure.md)
  You are unable to modify the messages.
- [INSetMessageAttributeIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to modify the messages.
- [INSetMessageAttributeIntentResponseCode.failureMessageNotFound](./failuremessagenotfound.md)
  One or more of the specified messages were not found.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetmessageattributeintentresponsecode/failuremessageattributenotset)*