# INMessage

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An object that describes a sent or received message.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INMessage
```

```objc
@interface INMessage : NSObject
```

## Mentions

- [Improving interactions between Siri and your messaging app](../SiriKit/improving-interactions-between-siri-and-your-messaging-app.md)

## Overview

When your app responds to an [`INSearchForMessagesIntent`](./insearchformessagesintent.md), you create instances of this class to provide Siri with information about the messages in your app. Each message contains a unique identifier, the participants’ details, and the content. You can group messages into larger discussions and, if you app supports multiple services, identify the service that delivers each message.

## Topics

### Creating a Message
- [convenience init(identifier: String, conversationIdentifier: String?, content: String?, dateSent: Date?, sender: INPerson?, recipients: [INPerson]?, groupName: INSpeakableString?, messageType: INMessageType, serviceName: String?, audioMessageFile: INFile?)](./inmessage/init%28identifier,conversationidentifier,content,datesent,sender,recipients,groupname,messagetype,servicename,audiomessagefile%29.md)
  Creates a message with the specified content and an optional audio message file.
- [init(identifier: String, conversationIdentifier: String?, content: String?, dateSent: Date?, sender: INPerson?, recipients: [INPerson]?, groupName: INSpeakableString?, messageType: INMessageType, serviceName: String?)](./inmessage/init%28identifier,conversationidentifier,content,datesent,sender,recipients,groupname,messagetype,servicename%29.md)
  Creates a message with the specified content and an optional service name.
- [convenience init(identifier: String, conversationIdentifier: String?, content: String?, dateSent: Date?, sender: INPerson?, recipients: [INPerson]?, groupName: INSpeakableString?, messageType: INMessageType)](./inmessage/init%28identifier,conversationidentifier,content,datesent,sender,recipients,groupname,messagetype%29.md)
  Creates a message with the specified content and an optional group name.
- [convenience init(identifier: String, conversationIdentifier: String?, content: String?, dateSent: Date?, sender: INPerson?, recipients: [INPerson]?, messageType: INMessageType)](./inmessage/init%28identifier,conversationidentifier,content,datesent,sender,recipients,messagetype%29.md)
  Creates a message of a distinct type with the specified content.
- [convenience init(identifier: String, content: String?, dateSent: Date?, sender: INPerson?, recipients: [INPerson]?)](./inmessage/init%28identifier,content,datesent,sender,recipients%29.md)
  Creates a message with the specified content.
### Identifying the Message
- [var identifier: String](./inmessage/identifier.md)
  The message’s unique identifier.
- [var conversationIdentifier: String?](./inmessage/conversationidentifier.md)
  The identifier of the conversation that contains this message.
### Getting the Participants
- [var sender: INPerson?](./inmessage/sender.md)
  The person who sent the message.
- [var recipients: [INPerson]?](./inmessage/recipients.md)
  The people who received the message.
### Getting the Content
- [var content: String?](./inmessage/content.md)
  The text that Siri recites to the message recipient.
- [var audioMessageFile: INFile?](./inmessage/audiomessagefile.md)
  An audio recording that Siri plays to the message recipient.
### Getting the Supplementary Attributes
- [var dateSent: Date?](./inmessage/datesent.md)
  The date and time the app sent the message to each recipient.
- [var groupName: INSpeakableString?](./inmessage/groupname.md)
  The name of the grouped conversation.
- [var messageType: INMessageType](./inmessage/messagetype.md)
  The type of content the message contains.
- [enum INMessageType](./inmessagetype.md)
  Constants that describe the kinds of content a message can contain.
- [var serviceName: String?](./inmessage/servicename.md)
  The name of the service that delivers the message.
### Initializers
- [init?(coder: NSCoder)](./inmessage/init%28coder%29.md)
- [convenience init(identifier: String, conversationIdentifier: String?, content: String?, dateSent: Date?, sender: INPerson?, recipients: [INPerson]?, groupName: INSpeakableString?, messageType: INMessageType, serviceName: String?, attachmentFiles: [INFile]?)](./inmessage/init%28identifier,conversationidentifier,content,datesent,sender,recipients,groupname,messagetype,servicename,attachmentfiles%29.md)
- [convenience init(identifier: String, conversationIdentifier: String?, content: String?, dateSent: Date?, sender: INPerson?, recipients: [INPerson]?, groupName: INSpeakableString?, serviceName: String?, linkMetadata: INMessageLinkMetadata?)](./inmessage/init%28identifier,conversationidentifier,content,datesent,sender,recipients,groupname,servicename,linkmetadata%29.md)
- [convenience init(identifier: String, conversationIdentifier: String?, content: String?, dateSent: Date?, sender: INPerson?, recipients: [INPerson]?, groupName: INSpeakableString?, serviceName: String?, messageType: INMessageType, numberOfAttachments: NSNumber?)](./inmessage/init%28identifier,conversationidentifier,content,datesent,sender,recipients,groupname,servicename,messagetype,numberofattachments%29.md)
- [convenience init(identifier: String, conversationIdentifier: String?, content: String?, dateSent: Date?, sender: INPerson?, recipients: [INPerson]?, groupName: INSpeakableString?, serviceName: String?, messageType: INMessageType, referencedMessage: INMessage?, reaction: INMessageReaction?)](./inmessage/init%28identifier,conversationidentifier,content,datesent,sender,recipients,groupname,servicename,messagetype,referencedmessage,reaction%29.md)
- [init(identifier: String, conversationIdentifier: String?, content: String?, dateSent: Date?, sender: INPerson?, recipients: [INPerson]?, groupName: INSpeakableString?, serviceName: String?, messageType: INMessageType, referencedMessage: INMessage?, sticker: INSticker?, reaction: INMessageReaction?)](./inmessage/init%28identifier,conversationidentifier,content,datesent,sender,recipients,groupname,servicename,messagetype,referencedmessage,sticker,reaction%29.md)
### Instance Properties
- [var attachmentFiles: [INFile]?](./inmessage/attachmentfiles.md)
- [var linkMetadata: INMessageLinkMetadata?](./inmessage/linkmetadata.md)
- [var numberOfAttachments: NSNumber?](./inmessage/numberofattachments.md)
- [var reaction: INMessageReaction?](./inmessage/reaction.md)
- [var sticker: INSticker?](./inmessage/sticker.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Managing Message Information
- [enum INMessageAttribute](./inmessageattribute.md)
  Constants that indicate an attribute of a message.
- [struct INMessageAttributeOptions](./inmessageattributeoptions.md)
  Constants that indicate a message search filter.
- [class INPerson](./inperson.md)
  Information about a person participating in a SiriKit interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmessage)*