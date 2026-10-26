# INSendMessageIntentResponseCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user must launch your app before they can send the message.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
case failureRequiringAppLaunch
```

```c
INSendMessageIntentResponseCodeFailureRequiringAppLaunch
```

#### Discussion

Use this response code when you cannot handle the request through Siri for a reason not covered by any other response code. For example, you might use this code if the user has not set up an account with your app. Do not use it for general errors or to force the user to launch your app.

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
- [INSendMessageIntentResponseCode.failure](./failure.md)
  You are unable to send the message.
- [INSendMessageIntentResponseCode.failureMessageServiceNotAvailable](./failuremessageservicenotavailable.md)
  You were unable to send the message because your message service is currently unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageintentresponsecode/failurerequiringapplaunch)*