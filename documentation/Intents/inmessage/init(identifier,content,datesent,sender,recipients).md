# init(identifier:content:dateSent:sender:recipients:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a message with the specified content.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
convenience init(identifier: String, content: String?, dateSent: Date?, sender: INPerson?, recipients: [INPerson]?)
```

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier content:(NSString *) content dateSent:(NSDate *) dateSent sender:(INPerson *) sender recipients:(NSArray<INPerson *> *) recipients;
```

#### Return Value

A message that SiriKit configures with the specified parameters, or `nil` if there was a problem creating the message.

#### Discussion

For each participant in the message (sender and recipients), create an instance of [`INPerson`](../inperson.md) using one of the initializers that require an `isMe` parameter. Use [`true`](../../Swift/true.md) for the participant that represents the user of the current device; for all other participants, use [`false`](../../Swift/false.md). When creating each of those objects, provide enough information for you to later identify that same person.

## Parameters

- `identifier`: The message’s unique identifier. Specify a value that you can later use to identify the same message.
- `content`: The text that Siri recites to the message recipient.
- `dateSent`: The date and time the app sent the message to each recipient.
- `sender`: The person who sent the message.
- `recipients`: The people who recieved the message.

## See Also

### Creating a Message
- [convenience init(identifier: String, conversationIdentifier: String?, content: String?, dateSent: Date?, sender: INPerson?, recipients: [INPerson]?, groupName: INSpeakableString?, messageType: INMessageType, serviceName: String?, audioMessageFile: INFile?)](./init%28identifier,conversationidentifier,content,datesent,sender,recipients,groupname,messagetype,servicename,audiomessagefile%29.md)
  Creates a message with the specified content and an optional audio message file.
- [init(identifier: String, conversationIdentifier: String?, content: String?, dateSent: Date?, sender: INPerson?, recipients: [INPerson]?, groupName: INSpeakableString?, messageType: INMessageType, serviceName: String?)](./init%28identifier,conversationidentifier,content,datesent,sender,recipients,groupname,messagetype,servicename%29.md)
  Creates a message with the specified content and an optional service name.
- [convenience init(identifier: String, conversationIdentifier: String?, content: String?, dateSent: Date?, sender: INPerson?, recipients: [INPerson]?, groupName: INSpeakableString?, messageType: INMessageType)](./init%28identifier,conversationidentifier,content,datesent,sender,recipients,groupname,messagetype%29.md)
  Creates a message with the specified content and an optional group name.
- [convenience init(identifier: String, conversationIdentifier: String?, content: String?, dateSent: Date?, sender: INPerson?, recipients: [INPerson]?, messageType: INMessageType)](./init%28identifier,conversationidentifier,content,datesent,sender,recipients,messagetype%29.md)
  Creates a message of a distinct type with the specified content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmessage/init(identifier:content:datesent:sender:recipients:))*