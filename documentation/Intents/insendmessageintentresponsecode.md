# INSendMessageIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the response state.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
enum INSendMessageIntentResponseCode
```

```c
enum INSendMessageIntentResponseCode : NSInteger;
```

## Topics

### Response State
- [INSendMessageIntentResponseCode.unspecified](./insendmessageintentresponsecode/unspecified.md)
  The response code isn’t specified.
- [INSendMessageIntentResponseCode.ready](./insendmessageintentresponsecode/ready.md)
  You are ready to handle the intent.
- [INSendMessageIntentResponseCode.inProgress](./insendmessageintentresponsecode/inprogress.md)
  You are in the process of sending the message but have not yet done so.
- [INSendMessageIntentResponseCode.success](./insendmessageintentresponsecode/success.md)
  You successfully handled the intent.
- [INSendMessageIntentResponseCode.failure](./insendmessageintentresponsecode/failure.md)
  You are unable to send the message.
- [INSendMessageIntentResponseCode.failureRequiringAppLaunch](./insendmessageintentresponsecode/failurerequiringapplaunch.md)
  The user must launch your app before they can send the message.
- [INSendMessageIntentResponseCode.failureMessageServiceNotAvailable](./insendmessageintentresponsecode/failuremessageservicenotavailable.md)
  You were unable to send the message because your message service is currently unavailable.
### Enumeration Cases
- [INSendMessageIntentResponseCode.failureRequiringInAppAuthentication](./insendmessageintentresponsecode/failurerequiringinappauthentication.md)
### Initializers
- [init?(rawValue: Int)](./insendmessageintentresponsecode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Response Code
- [var code: INSendMessageIntentResponseCode](./insendmessageintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageintentresponsecode)*