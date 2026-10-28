# init(recipients:content:speakableGroupName:conversationIdentifier:serviceName:sender:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes a send message intent object with the specified content and recipients.

**Availability**:
- iOS 11.0+ - Deprecated in 14.0
- iPadOS 11.0+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- macOS 10.13+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 7.0

> **Deprecated**: Use [`init(recipients:outgoingMessageType:content:speakableGroupName:conversationIdentifier:serviceName:sender:attachments:)`](./init%28recipients,outgoingmessagetype,content,speakablegroupname,conversationidentifier,servicename,sender,attachments%29.md) instead.

## Declaration

```swift
convenience init(recipients: [INPerson]?, content: String?, speakableGroupName: INSpeakableString?, conversationIdentifier: String?, serviceName: String?, sender: INPerson?)
```

```objc
- (instancetype) initWithRecipients:(NSArray<INPerson *> *) recipients content:(NSString *) content speakableGroupName:(INSpeakableString *) speakableGroupName conversationIdentifier:(NSString *) conversationIdentifier serviceName:(NSString *) serviceName sender:(INPerson *) sender;
```

## Return Value

An initialized intent or `nil` if the object could not be created.

## Parameters

- `recipients`: The intended recipients of the message.
- `content`: The contents of the message.
- `speakableGroupName`: The name of a group that should receive the message. Specify `nil` if you do not want to send the message to a group address.
- `conversationIdentifier`: The unique identifier for the message conversation. Specify `nil` if your app does not assign identifiers to conversations between users.
- `serviceName`: The specific service to use when sending the message. You may specify `nil` if your app has only one way of sending messages.
- `sender`: The person that created the message.

## See Also

### Deprecated Symbols
- [convenience init(recipients: [INPerson]?, content: String?, groupName: String?, serviceName: String?, sender: INPerson?)](./init%28recipients,content,groupname,servicename,sender%29.md)
  Initializes a send message intent object with the specified content and recipients.
- [convenience init(recipients: [INPerson]?, outgoingMessageType: INOutgoingMessageType, content: String?, speakableGroupName: INSpeakableString?, conversationIdentifier: String?, serviceName: String?, sender: INPerson?)](./init%28recipients,outgoingmessagetype,content,speakablegroupname,conversationidentifier,servicename,sender%29.md)
  Initializes a send message intent object with the specified content and recipients.
- [var groupName: String?](./groupname.md)
  The name of the group to receive the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageintent/init(recipients:content:speakablegroupname:conversationidentifier:servicename:sender:))*