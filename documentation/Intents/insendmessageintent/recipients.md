# recipients

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The array of users to receive the message.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var recipients: [INPerson]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<INPerson *> * recipients;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<INPerson *> * recipients;
```

## Mentions

- [Improving interactions between Siri and your messaging app](../../SiriKit/improving-interactions-between-siri-and-your-messaging-app.md)

#### Discussion

Use this property to identify the intended recipients of the message. During the resolution phase, use the information in each [`INPerson`](../inperson.md) object to resolve the named individual to a specific user of your app.

## See Also

### Specifying Details About a Message
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
- [var attachments: [INSendMessageAttachment]?](./attachments.md)
  Audio files to include in the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageintent/recipients)*