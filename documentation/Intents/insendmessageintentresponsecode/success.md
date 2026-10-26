# INSendMessageIntentResponseCode.success

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You successfully handled the intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case success
```

```c
INSendMessageIntentResponseCodeSuccess
```

#### Discussion

Use this code if your app successfully sent the message.

## See Also

### Response State
- [INSendMessageIntentResponseCode.unspecified](./unspecified.md)
  The response code isn’t specified.
- [INSendMessageIntentResponseCode.ready](./ready.md)
  You are ready to handle the intent.
- [INSendMessageIntentResponseCode.inProgress](./inprogress.md)
  You are in the process of sending the message but have not yet done so.
- [INSendMessageIntentResponseCode.failure](./failure.md)
  You are unable to send the message.
- [INSendMessageIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app before they can send the message.
- [INSendMessageIntentResponseCode.failureMessageServiceNotAvailable](./failuremessageservicenotavailable.md)
  You were unable to send the message because your message service is currently unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageintentresponsecode/success)*