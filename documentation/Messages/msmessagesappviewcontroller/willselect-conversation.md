# willSelect(_:conversation:)

**Framework**: Messages  
**Kind**: method

Invoked in response to the user selecting a message object in the transcript, before the system updates the conversation’s [`selectedMessage`](msconversation/selectedmessage.md) property.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func willSelect(_ message: MSMessage, conversation: MSConversation)
```

## Mentions

- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime.md)

#### Discussion

This method is called when the user selects one of your app’s message objects in the transcript while your extension is active. You can access the previously selected message (if any) from the `conversation` object’s  [`selectedMessage`](msconversation/selectedmessage.md) property.

This method is called when a new message arrives while your extension is active. You receive notifications about messages sent using your extension only. You cannot interact with messages from other extensions.

The system does not call this method if the controller’s [`presentationStyle`](msmessagesappviewcontroller/presentationstyle.md) property is [`MSMessagesAppPresentationStyle.transcript`](msmessagesapppresentationstyle/transcript.md), or if its [`presentationContext`](msmessagesappviewcontroller/presentationcontext.md) property is [`MSMessagesAppPresentationContext.media`](msmessagesapppresentationcontext/media.md).

## Parameters

- `message`: The message selected by the user.
- `conversation`: The current conversation.

## See Also

- [func didSelect(MSMessage, conversation: MSConversation)](msmessagesappviewcontroller/didselect(_:conversation:).md)
  Invoked in response to the user selecting a message object in the transcript, after the system updates the conversation’s [`selectedMessage`](msconversation/selectedmessage.md) property.
- [func didReceive(MSMessage, conversation: MSConversation)](msmessagesappviewcontroller/didreceive(_:conversation:).md)
  Invoked when the iMessage app receives a new message object.
- [func didStartSending(MSMessage, conversation: MSConversation)](msmessagesappviewcontroller/didstartsending(_:conversation:).md)
  Invoked when the user sends a message object.
- [func didCancelSending(MSMessage, conversation: MSConversation)](msmessagesappviewcontroller/didcancelsending(_:conversation:).md)
  Invoked when the user deletes a message object from the Messages app’s input field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/willselect(_:conversation:))*