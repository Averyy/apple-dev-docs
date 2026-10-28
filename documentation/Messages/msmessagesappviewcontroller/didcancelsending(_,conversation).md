# didCancelSending(_:conversation:)

**Framework**: Messages  
**Kind**: method  
**Role**: Instance Method

Invoked when the user deletes a message object from the Messages app’s input field.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func didCancelSending(_ message: MSMessage, conversation: MSConversation)
```

```objc
- (void) didCancelSendingMessage:(MSMessage *) message conversation:(MSConversation *) conversation;
```

## Mentions

- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](../adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime.md)

## Discussion

Override this method to respond when a message is canceled. This method is called if you use the conversation’s [`insert(_:completionHandler:)`](../msconversation/insert%28_,completionhandler%29-3g248.md) method to add an [`MSMessage`](../msmessage.md) object to the Messages app’s input field, and the user subsequently deletes the message object.

The system does not call this method if the controller’s [`presentationStyle`](./presentationstyle.md) property is [`MSMessagesAppPresentationStyle.transcript`](../msmessagesapppresentationstyle/transcript.md), or if its [`presentationContext`](./presentationcontext.md) property is [`MSMessagesAppPresentationContext.media`](../msmessagesapppresentationcontext/media.md).

## Parameters

- `message`: The deleted message object.
- `conversation`: The conversation that the user is currently viewing in the Messages app.

## See Also

### Tracking Messages
- [func willSelect(MSMessage, conversation: MSConversation)](./willselect%28_,conversation%29.md)
  Invoked in response to the user selecting a message object in the transcript, before the system updates the conversation’s [`selectedMessage`](../msconversation/selectedmessage.md) property.
- [func didSelect(MSMessage, conversation: MSConversation)](./didselect%28_,conversation%29.md)
  Invoked in response to the user selecting a message object in the transcript, after the system updates the conversation’s [`selectedMessage`](../msconversation/selectedmessage.md) property.
- [func didReceive(MSMessage, conversation: MSConversation)](./didreceive%28_,conversation%29.md)
  Invoked when the iMessage app receives a new message object.
- [func didStartSending(MSMessage, conversation: MSConversation)](./didstartsending%28_,conversation%29.md)
  Invoked when the user sends a message object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/didcancelsending(_:conversation:))*