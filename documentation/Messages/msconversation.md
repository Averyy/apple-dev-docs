# MSConversation

**Framework**: Messages  
**Kind**: class  
**Role**: Class

An object that represents a conversation in the Messages app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class MSConversation
```

```objc
@interface MSConversation : NSObject
```

## Mentions

- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](./adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime.md)

#### Overview

The [`MSConversation`](./msconversation.md) class represents a conversation in the Messages app. Use conversation objects to access information about the currently selected message or the conversation participants, or to send text, stickers, attachments, or message objects.

## Topics

### Accessing the Selected Message
- [var selectedMessage: MSMessage?](./msconversation/selectedmessage.md)
  The message that the user selected in the conversation transcript.
### Accessing Participants
- [var localParticipantIdentifier: UUID](./msconversation/localparticipantidentifier.md)
  A UUID that identifies the user on this device.
- [var remoteParticipantIdentifiers: [UUID]](./msconversation/remoteparticipantidentifiers.md)
  An array of UUIDs representing the remote participants in this conversation.
### Inserting Content into the Input Field
- [func insertAttachment(URL, withAlternateFilename: String?, completionHandler: (((any Error)?) -> Void)?)](./msconversation/insertattachment%28_,withalternatefilename,completionhandler%29.md)
  Inserts an attachment into the current context.
- [func insert(MSMessage, completionHandler: (((any Error)?) -> Void)?)](./msconversation/insert%28_,completionhandler%29-3g248.md)
  Inserts a message object into the Messages app’s input field.
- [func insert(MSSticker, completionHandler: (((any Error)?) -> Void)?)](./msconversation/insert%28_,completionhandler%29-7fpdd.md)
  Inserts a sticker into the current context.
- [func insertText(String, completionHandler: (((any Error)?) -> Void)?)](./msconversation/inserttext%28_,completionhandler%29.md)
  Inserts text into the Messages app’s input field.
### Directly Sending a Message
- [func sendAttachment(URL, withAlternateFilename: String?, completionHandler: (((any Error)?) -> Void)?)](./msconversation/sendattachment%28_,withalternatefilename,completionhandler%29.md)
  Sends the media file specified by the given URL.
- [func send(MSMessage, completionHandler: (((any Error)?) -> Void)?)](./msconversation/send%28_,completionhandler%29-9krz.md)
  Sends a message object.
- [func send(MSSticker, completionHandler: (((any Error)?) -> Void)?)](./msconversation/send%28_,completionhandler%29-4kje0.md)
  Sends a sticker.
- [func sendText(String, completionHandler: (((any Error)?) -> Void)?)](./msconversation/sendtext%28_,completionhandler%29.md)
  Sends a text message.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Message content
- [class MSSticker](./mssticker.md)
  A sticker that can be sent as a new message or attached to an existing balloon in the Messages app’s  transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msconversation)*