# INSendMessageIntentResponseCode.failure

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You are unable to send the message.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case failure
```

```c
INSendMessageIntentResponseCodeFailure
```

## Discussion

Use this code for both transient and unrecoverable errors that would prevent you from sending the message.

## See Also

### Response State
- [INSendMessageIntentResponseCode.unspecified](./unspecified.md)
  The response code isn’t specified.
- [INSendMessageIntentResponseCode.ready](./ready.md)
  You are ready to handle the intent.
- [INSendMessageIntentResponseCode.inProgress](./inprogress.md)
  You are in the process of sending the message but have not yet done so.
- [INSendMessageIntentResponseCode.success](./success.md)
  You successfully handled the intent.
- [INSendMessageIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app before they can send the message.
- [INSendMessageIntentResponseCode.failureMessageServiceNotAvailable](./failuremessageservicenotavailable.md)
  You were unable to send the message because your message service is currently unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageintentresponsecode/failure)*