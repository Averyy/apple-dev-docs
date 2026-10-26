# INSetMessageAttributeIntentResponseCode.unspecified

**Framework**: Intents  
**Kind**: case  
**Role**: Case

An unknown response code.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case unspecified
```

```c
INSetMessageAttributeIntentResponseCodeUnspecified
```

## See Also

### Response State
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
- [INSetMessageAttributeIntentResponseCode.failureMessageAttributeNotSet](./failuremessageattributenotset.md)
  The message attributes couldn’t be modified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetmessageattributeintentresponsecode/unspecified)*