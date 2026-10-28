# init(identifier:conversationIdentifier:content:dateSent:sender:recipients:groupName:messageType:serviceName:audioMessageFile:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a message with the specified content and an optional audio message file.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
convenience init(identifier: String, conversationIdentifier: String?, content: String?, dateSent: Date?, sender: INPerson?, recipients: [INPerson]?, groupName: INSpeakableString?, messageType: INMessageType, serviceName: String?, audioMessageFile: INFile?)
```

```objc
- (instancetype) initWithIdentifier:(NSString *) identifier conversationIdentifier:(NSString *) conversationIdentifier content:(NSString *) content dateSent:(NSDate *) dateSent sender:(INPerson *) sender recipients:(NSArray<INPerson *> *) recipients groupName:(INSpeakableString *) groupName messageType:(INMessageType) messageType serviceName:(NSString *) serviceName audioMessageFile:(INFile *) audioMessageFile;
```

## Return Value

A message that SiriKit configures with the specified parameters, or `nil` if there was a problem creating the message.

## Discussion

Use the `conversationIdentifier` parameter to associate individual messages with a larger discussion among a specific group of people.

For each participant in the message (sender and recipients), create an instance of [`INPerson`](../inperson.md) using one of the initializers that require an `isMe` parameter. Use [`true`](../../Swift/true.md) for the participant that represents the user of the current device; for all other participants, use [`false`](../../Swift/false.md). When creating each of those objects, provide enough information for you to later identify that same person.

If your app supports more than one message service, specify the `serviceName` parameter to indicate which service the app uses to deliver a specific message.

To enable Siri to play an audio message, specify the `audioMessageFile` parameter and set the `messageType` parameter to [`INMessageType.audio`](../inmessagetype/audio.md). Siri’s access to the file lasts only for the duration of the current session and the system never sends the file to Apple’s servers. Siri supports all common audio formats; to request additional formats, use the [Feedback Assistant](https://feedbackassistant.apple.com/welcome).

## Parameters

- `identifier`: The message’s unique identifier. Specify a value that you can later use to identify the same message.
- `conversationIdentifier`: The identifier of the conversation that contains this message.
- `content`: The text that Siri recites to the message recipient.
- `dateSent`: The date and time the app sent the message to each recipient.
- `sender`: The person who sent the message.
- `recipients`: The people who recieved the message.
- `groupName`: The name of the grouped conversation. Provide a value only when the message belongs to a named group; otherwise, specify `nil`.
- `messageType`: The type of content the message contains. For possible values, see [`INMessageType`](../inmessagetype.md).
- `serviceName`: The name of the service that delivers the message.
- `audioMessageFile`: An audio recording that Siri plays to the message recipient.

## See Also

### Creating a Message
- [init(identifier: String, conversationIdentifier: String?, content: String?, dateSent: Date?, sender: INPerson?, recipients: [INPerson]?, groupName: INSpeakableString?, messageType: INMessageType, serviceName: String?)](./init%28identifier,conversationidentifier,content,datesent,sender,recipients,groupname,messagetype,servicename%29.md)
  Creates a message with the specified content and an optional service name.
- [convenience init(identifier: String, conversationIdentifier: String?, content: String?, dateSent: Date?, sender: INPerson?, recipients: [INPerson]?, groupName: INSpeakableString?, messageType: INMessageType)](./init%28identifier,conversationidentifier,content,datesent,sender,recipients,groupname,messagetype%29.md)
  Creates a message with the specified content and an optional group name.
- [convenience init(identifier: String, conversationIdentifier: String?, content: String?, dateSent: Date?, sender: INPerson?, recipients: [INPerson]?, messageType: INMessageType)](./init%28identifier,conversationidentifier,content,datesent,sender,recipients,messagetype%29.md)
  Creates a message of a distinct type with the specified content.
- [convenience init(identifier: String, content: String?, dateSent: Date?, sender: INPerson?, recipients: [INPerson]?)](./init%28identifier,content,datesent,sender,recipients%29.md)
  Creates a message with the specified content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmessage/init(identifier:conversationidentifier:content:datesent:sender:recipients:groupname:messagetype:servicename:audiomessagefile:))*