# attachments

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

Audio files to include in the message.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var attachments: [INSendMessageAttachment]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<INSendMessageAttachment *> * attachments;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<INSendMessageAttachment *> * attachments;
```

## See Also

### Specifying Details About a Message
- [var recipients: [INPerson]?](./recipients.md)
  The array of users to receive the message.
- [var outgoingMessageType: INOutgoingMessageType](./outgoingmessagetype.md)
  The format of the message contents.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageintent/attachments)*