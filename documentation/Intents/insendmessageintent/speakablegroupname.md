# speakableGroupName

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The name of the group to receive the message.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
@NSCopying
var speakableGroupName: INSpeakableString? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INSpeakableString * speakableGroupName;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INSpeakableString * speakableGroupName;
```

## Discussion

Use this property to identify the group that is the intended recipient of the message. Your app is responsible for managing groups and for using this parameter to identify the appropriate group.

## See Also

### Specifying Details About a Message
- [var recipients: [INPerson]?](./recipients.md)
  The array of users to receive the message.
- [var outgoingMessageType: INOutgoingMessageType](./outgoingmessagetype.md)
  The format of the message contents.
- [var conversationIdentifier: String?](./conversationidentifier.md)
  The identifier for the conversation.
- [var content: String?](./content.md)
  The content of the message.
- [var serviceName: String?](./servicename.md)
  The service to use when sending the message.
- [var sender: INPerson?](./sender.md)
  The person or account that’s sending the message.
- [var attachments: [INSendMessageAttachment]?](./attachments.md)
  Audio files to include in the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageintent/speakablegroupname)*