# init(recipients:outgoingMessageType:content:speakableGroupName:conversationIdentifier:serviceName:sender:attachments:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a send message intent object with the specified content and recipients.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(recipients: [INPerson]?, outgoingMessageType: INOutgoingMessageType, content: String?, speakableGroupName: INSpeakableString?, conversationIdentifier: String?, serviceName: String?, sender: INPerson?, attachments: [INSendMessageAttachment]?)
```

```objc
- (instancetype) initWithRecipients:(NSArray<INPerson *> *) recipients outgoingMessageType:(INOutgoingMessageType) outgoingMessageType content:(NSString *) content speakableGroupName:(INSpeakableString *) speakableGroupName conversationIdentifier:(NSString *) conversationIdentifier serviceName:(NSString *) serviceName sender:(INPerson *) sender attachments:(NSArray<INSendMessageAttachment *> *) attachments;
```

## Return Value

An initialized intent or `nil` if the system can’t create the object.

## Discussion

Create an [`INSendMessageIntent`](../insendmessageintent.md) and donate it in an [`INInteraction`](../ininteraction.md) when the user sends a message directly in your app. When the user initiates sending a message from outside your app, such as asking Siri or tapping a contact in the Share Sheet, the system creates the intent and provides it to your intent handler.

## Parameters

- `recipients`: The intended recipients of the message.
- `outgoingMessageType`: The format of the message.
- `content`: The contents of the message.
- `speakableGroupName`: The name of the group to receive the message. Specify `nil` if you don’t want to send the message to a group address.
- `conversationIdentifier`: The unique identifier for the message conversation. Specify `nil` if your app doesn’t assign identifiers to conversations between users.
- `serviceName`: The specific service to use when sending the message. You may specify `nil` if your app has only one way of sending messages.
- `sender`: The person who creates the message.
- `attachments`: Audio files to include with the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageintent/init(recipients:outgoingmessagetype:content:speakablegroupname:conversationidentifier:servicename:sender:attachments:))*