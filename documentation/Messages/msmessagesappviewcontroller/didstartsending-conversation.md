# didStartSending(_:conversation:)

**Framework**: Messages  
**Kind**: method

Invoked when the user sends a message object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func didStartSending(_ message: MSMessage, conversation: MSConversation)
```

## Mentions

- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime.md)

#### Discussion

Override this method to respond when the user sends an [`MSMessage`](msmessage.md) object. This method is called if you use the conversation’s [`insert(_:completionHandler:)`](msconversation/insert(_:completionhandler:)-3g248.md) method to add an [`MSMessage`](msmessage.md) object to the Messages app’s input field, and the user taps Send. It does not guarantee  that the message will be successfully sent or delivered.

The system does not call this method if the controller’s [`presentationStyle`](msmessagesappviewcontroller/presentationstyle.md) property is [`MSMessagesAppPresentationStyle.transcript`](msmessagesapppresentationstyle/transcript.md), or if its [`presentationContext`](msmessagesappviewcontroller/presentationcontext.md) property is [`MSMessagesAppPresentationContext.media`](msmessagesapppresentationcontext/media.md).

## Parameters

- `message`: The message being sent.
- `conversation`: The conversation that the user is currently viewing in the Messages app.

## See Also

- [func willSelect(MSMessage, conversation: MSConversation)](msmessagesappviewcontroller/willselect(_:conversation:).md)
  Invoked in response to the user selecting a message object in the transcript, before the system updates the conversation’s [`selectedMessage`](msconversation/selectedmessage.md) property.
- [func didSelect(MSMessage, conversation: MSConversation)](msmessagesappviewcontroller/didselect(_:conversation:).md)
  Invoked in response to the user selecting a message object in the transcript, after the system updates the conversation’s [`selectedMessage`](msconversation/selectedmessage.md) property.
- [func didReceive(MSMessage, conversation: MSConversation)](msmessagesappviewcontroller/didreceive(_:conversation:).md)
  Invoked when the iMessage app receives a new message object.
- [func didCancelSending(MSMessage, conversation: MSConversation)](msmessagesappviewcontroller/didcancelsending(_:conversation:).md)
  Invoked when the user deletes a message object from the Messages app’s input field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/didstartsending(_:conversation:))*