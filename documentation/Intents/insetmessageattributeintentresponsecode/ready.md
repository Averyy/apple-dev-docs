# INSetMessageAttributeIntentResponseCode.ready

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The app is ready to handle the intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case ready
```

```c
INSetMessageAttributeIntentResponseCodeReady
```

#### Discussion

Use this code during the confirmation phase to indicate that you have access to your message service and are able to modify the specified messages.

## See Also

### Response State
- [INSetMessageAttributeIntentResponseCode.unspecified](./unspecified.md)
  An unknown response code.
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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetmessageattributeintentresponsecode/ready)*