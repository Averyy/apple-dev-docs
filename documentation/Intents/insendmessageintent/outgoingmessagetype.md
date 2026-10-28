# outgoingMessageType

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The format of the message contents.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var outgoingMessageType: INOutgoingMessageType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INOutgoingMessageType outgoingMessageType;
```

*macOS*

```objc
@property (atomic, assign, readonly) INOutgoingMessageType outgoingMessageType;
```

## Discussion

If the user asks Siri to send an audio message,_ _the value of this property is [`INOutgoingMessageType.outgoingMessageAudio`](../inoutgoingmessagetype/outgoingmessageaudio.md). An audio message may also include a transcription of the audio message in the [`content`](./content.md) property.

If the user doesn’t specify what type of message to send, the default message type is [`INOutgoingMessageType.outgoingMessageText`](../inoutgoingmessagetype/outgoingmessagetext.md).

## See Also

### Specifying Details About a Message
- [var recipients: [INPerson]?](./recipients.md)
  The array of users to receive the message.
- [var conversationIdentifier: String?](./conversationidentifier.md)
  The identifier for the conversation.
- [var speakableGroupName: INSpeakableString?](./speakablegroupname.md)
  The name of the group to receive the message.
- [var content: String?](./content.md)
  The content of the message.
- [var serviceName: String?](./servicename.md)
  The service to use when sending the message.
- [var sender: INPerson?](./sender.md)
  The person or account that’s sending the message.
- [var attachments: [INSendMessageAttachment]?](./attachments.md)
  Audio files to include in the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageintent/outgoingmessagetype)*