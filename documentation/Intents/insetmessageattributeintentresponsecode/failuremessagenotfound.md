# INSetMessageAttributeIntentResponseCode.failureMessageNotFound

**Framework**: Intents  
**Kind**: case  
**Role**: Case

One or more of the specified messages were not found.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case failureMessageNotFound
```

```c
INSetMessageAttributeIntentResponseCodeFailureMessageNotFound
```

#### Discussion

Use this response code when you could not find one or more of the specified messages.

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
- [INSetMessageAttributeIntentResponseCode.failureMessageAttributeNotSet](./failuremessageattributenotset.md)
  The message attributes couldn’t be modified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetmessageattributeintentresponsecode/failuremessagenotfound)*