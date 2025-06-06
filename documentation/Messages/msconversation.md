# MSConversation

**Framework**: Messages  
**Kind**: class

An object that represents a conversation in the Messages app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class MSConversation
```

## Mentions

- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime.md)

#### Overview

The [`MSConversation`](msconversation.md) class represents a conversation in the Messages app. Use conversation objects to access information about the currently selected message or the conversation participants, or to send text, stickers, attachments, or message objects.

## Topics

### Accessing the Selected Message
- [var selectedMessage: MSMessage?](msconversation/selectedmessage.md)
  The message that the user selected in the conversation transcript.
### Accessing Participants
- [var localParticipantIdentifier: UUID](msconversation/localparticipantidentifier.md)
  A UUID that identifies the user on this device.
- [var remoteParticipantIdentifiers: [UUID]](msconversation/remoteparticipantidentifiers.md)
  An array of UUIDs representing the remote participants in this conversation.
### Inserting Content into the Input Field
- [func insertAttachment(URL, withAlternateFilename: String?, completionHandler: (((any Error)?) -> Void)?)](msconversation/insertattachment(_:withalternatefilename:completionhandler:).md)
  Inserts an attachment into the current context.
- [func insert(MSMessage, completionHandler: (((any Error)?) -> Void)?)](msconversation/insert(_:completionhandler:)-3g248.md)
  Inserts a message object into the Messages app’s input field.
- [func insert(MSSticker, completionHandler: (((any Error)?) -> Void)?)](msconversation/insert(_:completionhandler:)-7fpdd.md)
  Inserts a sticker into the current context.
- [func insertText(String, completionHandler: (((any Error)?) -> Void)?)](msconversation/inserttext(_:completionhandler:).md)
  Inserts text into the Messages app’s input field.
### Directly Sending a Message
- [func sendAttachment(URL, withAlternateFilename: String?, completionHandler: (((any Error)?) -> Void)?)](msconversation/sendattachment(_:withalternatefilename:completionhandler:).md)
  Sends the media file specified by the given URL.
- [func send(MSMessage, completionHandler: (((any Error)?) -> Void)?)](msconversation/send(_:completionhandler:)-9krz.md)
  Sends a message object.
- [func send(MSSticker, completionHandler: (((any Error)?) -> Void)?)](msconversation/send(_:completionhandler:)-4kje0.md)
  Sends a sticker.
- [func sendText(String, completionHandler: (((any Error)?) -> Void)?)](msconversation/sendtext(_:completionhandler:).md)
  Sends a text message.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MSSticker](mssticker.md)
  A sticker that can be sent as a new message or attached to an existing balloon in the Messages app’s  transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msconversation)*