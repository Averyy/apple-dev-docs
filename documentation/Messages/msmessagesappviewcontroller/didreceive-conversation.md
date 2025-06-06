# didReceive(_:conversation:)

**Framework**: Messages  
**Kind**: method

Invoked when the iMessage app receives a new message object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func didReceive(_ message: MSMessage, conversation: MSConversation)
```

## Mentions

- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime.md)

#### Discussion

Override this method to respond to messages that arrive while your extension is active.

If your app displays information about the currently selected message, check the incoming message’s session against the selected message’s session. If they match, update the information displayed in your user interface to represent the most recent message data (see Listing 1).

Listing 1. Updating the current session

```swift
override func didReceive(_ message: MSMessage, conversation: MSConversation) {
    // Check to see if the incoming message is part of a session
    if let incomingSession = message.session {
        // Check to see if the incoming session matches the current message’s session
        if incomingSession == conversation.selectedMessage?.session {
            // Update your user interface here...
        }
    }
}
```

> **Note**:  There is an inherent race condition when multiple participants send messages using the same session object. You cannot guarantee the order in which the messages are received. To ensure that your app always has the latest data, save your data to a server (for example, using CloudKit) and have your messages just carry an ID for that data. Your app can then look up the current data whenever it receives a new message.

 There is an inherent race condition when multiple participants send messages using the same session object. You cannot guarantee the order in which the messages are received. To ensure that your app always has the latest data, save your data to a server (for example, using CloudKit) and have your messages just carry an ID for that data. Your app can then look up the current data whenever it receives a new message.

This method is called when a new message arrives while your extension is active. You receive notifications about messages sent using your extension only. You cannot interact with messages from other extensions.

The system does not call this method if the controller’s [`presentationStyle`](msmessagesappviewcontroller/presentationstyle.md) property is [`MSMessagesAppPresentationStyle.transcript`](msmessagesapppresentationstyle/transcript.md), or if its [`presentationContext`](msmessagesappviewcontroller/presentationcontext.md) property is [`MSMessagesAppPresentationContext.media`](msmessagesapppresentationcontext/media.md).

## Parameters

- `message`: The received message object.
- `conversation`: The conversation that the user is currently viewing in the Messages app.

## See Also

- [func willSelect(MSMessage, conversation: MSConversation)](msmessagesappviewcontroller/willselect(_:conversation:).md)
  Invoked in response to the user selecting a message object in the transcript, before the system updates the conversation’s [`selectedMessage`](msconversation/selectedmessage.md) property.
- [func didSelect(MSMessage, conversation: MSConversation)](msmessagesappviewcontroller/didselect(_:conversation:).md)
  Invoked in response to the user selecting a message object in the transcript, after the system updates the conversation’s [`selectedMessage`](msconversation/selectedmessage.md) property.
- [func didStartSending(MSMessage, conversation: MSConversation)](msmessagesappviewcontroller/didstartsending(_:conversation:).md)
  Invoked when the user sends a message object.
- [func didCancelSending(MSMessage, conversation: MSConversation)](msmessagesappviewcontroller/didcancelsending(_:conversation:).md)
  Invoked when the user deletes a message object from the Messages app’s input field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesappviewcontroller/didreceive(_:conversation:))*