# INSendMessageIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to send a message to the designated recipients.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INSendMessageIntent
```

```objc
@interface INSendMessageIntent : INIntent
```

## Mentions

- [Dispatching intents to handlers](../SiriKit/dispatching-intents-to-handlers.md)
- [Improving interactions between Siri and your messaging app](../SiriKit/improving-interactions-between-siri-and-your-messaging-app.md)

#### Overview

Siri creates an [`INSendMessageIntent`](./insendmessageintent.md) object when the user asks to send a message to one or more users. This intent object contains the message to send and the recipients of the message, which can include groups of users. Use the information in this object to construct and send the message.

To handle this intent, the handler object in your Intents extension must adopt the [`INSendMessageIntentHandling`](./insendmessageintenthandling.md) protocol. Your handler confirms the request and creates an [`INSendMessageIntentResponse`](./insendmessageintentresponse.md) object with the results.

> **Note**:  To allow a user wearing AirPods to automatically hear messages, you must implement both [`INSearchForMessagesIntent`](./insearchformessagesintent.md) and [`INSendMessageIntent`](./insendmessageintent.md). Add [`announcement`](../UserNotifications/unauthorizationoptions/announcement.md) to the options when calling [`requestAuthorization(options:completionHandler:)`](../UserNotifications/unusernotificationcenter/requestauthorization%28options,completionhandler%29.md). Finally, add [`allowAnnouncement`](../UserNotifications/unnotificationcategoryoptions/allowannouncement.md) to the category option and [`INSearchForMessagesIntent`](./insearchformessagesintent.md) to the category intent identifier.

##### Additional Intent Attributes

Additional attributes of this intent object include the following:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents, Siri Suggestions |
| Always requires unlocked device | No |

Apps can optionally ask the user to unlock the device before handling this intent. To require unlocking of the device, include the name of this class in the `IntentsRestrictedWhileLocked` key of your Intents extension’s `Info.plist` file.

## Topics

### Creating the Intent Object
- [init(recipients: [INPerson]?, outgoingMessageType: INOutgoingMessageType, content: String?, speakableGroupName: INSpeakableString?, conversationIdentifier: String?, serviceName: String?, sender: INPerson?, attachments: [INSendMessageAttachment]?)](./insendmessageintent/init%28recipients,outgoingmessagetype,content,speakablegroupname,conversationidentifier,servicename,sender,attachments%29.md)
  Creates a send message intent object with the specified content and recipients.
### Specifying Details About a Message
- [var recipients: [INPerson]?](./insendmessageintent/recipients.md)
  The array of users to receive the message.
- [var outgoingMessageType: INOutgoingMessageType](./insendmessageintent/outgoingmessagetype.md)
  The format of the message contents.
- [var conversationIdentifier: String?](./insendmessageintent/conversationidentifier.md)
  The identifier for the conversation.
- [var speakableGroupName: INSpeakableString?](./insendmessageintent/speakablegroupname.md)
  The name of the group to receive the message.
- [var content: String?](./insendmessageintent/content.md)
  The content of the message.
- [var serviceName: String?](./insendmessageintent/servicename.md)
  The service to use when sending the message.
- [var sender: INPerson?](./insendmessageintent/sender.md)
  The person or account that’s sending the message.
- [var attachments: [INSendMessageAttachment]?](./insendmessageintent/attachments.md)
  Audio files to include in the message.
### Deprecated Symbols
- [convenience init(recipients: [INPerson]?, content: String?, speakableGroupName: INSpeakableString?, conversationIdentifier: String?, serviceName: String?, sender: INPerson?)](./insendmessageintent/init%28recipients,content,speakablegroupname,conversationidentifier,servicename,sender%29.md)
  Initializes a send message intent object with the specified content and recipients.
- [convenience init(recipients: [INPerson]?, content: String?, groupName: String?, serviceName: String?, sender: INPerson?)](./insendmessageintent/init%28recipients,content,groupname,servicename,sender%29.md)
  Initializes a send message intent object with the specified content and recipients.
- [convenience init(recipients: [INPerson]?, outgoingMessageType: INOutgoingMessageType, content: String?, speakableGroupName: INSpeakableString?, conversationIdentifier: String?, serviceName: String?, sender: INPerson?)](./insendmessageintent/init%28recipients,outgoingmessagetype,content,speakablegroupname,conversationidentifier,servicename,sender%29.md)
  Initializes a send message intent object with the specified content and recipients.
- [var groupName: String?](./insendmessageintent/groupname.md)
  The name of the group to receive the message.

## Relationships

### Inherits From
- [INIntent](./inintent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [INIntentSetImageKeyPath](./inintentsetimagekeypath.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [UNNotificationContentProviding](../UserNotifications/unnotificationcontentproviding.md)

## See Also

### Sending a Message
- [protocol INSendMessageIntentHandling](./insendmessageintenthandling.md)
  An interface to handle sending messages to one or more designated users.
- [class INSendMessageIntentResponse](./insendmessageintentresponse.md)
  Your app’s response to a send message intent.
- [enum INOutgoingMessageType](./inoutgoingmessagetype.md)
  The format of the message.
- [class INSendMessageAttachment](./insendmessageattachment.md)
  A file to include in a message.
- [class INSendMessageIntentDonationMetadata](./insendmessageintentdonationmetadata.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendmessageintent)*