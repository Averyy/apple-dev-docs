# send(_:completionHandler:)

**Framework**: Messages  
**Kind**: method

Sends a message object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func send(_ message: MSMessage) async throws
```

## Mentions

- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func send(_ message: MSMessage) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

This method starts sending the message object automatically,  without any additional user interactions. You can call this method only in response to a user action while in the [`MSMessagesAppPresentationContext.messages`](msmessagesapppresentationcontext/messages.md) context.

When calling this method, the following rules apply:

- If the app isn’t visible, the send fails with a [`MSMessageErrorCode.sendWhileNotVisible`](msmessageerrorcode/sendwhilenotvisible.md) error code.
- If the app hasn’t registered a recent touch interaction from the user, the send fails with a [`MSMessageErrorCode.sendWithoutRecentInteraction`](msmessageerrorcode/sendwithoutrecentinteraction.md) error code.
- If the app is in the [`MSMessagesAppPresentationContext.media`](msmessagesapppresentationcontext/media.md) context, the send fails with an [`MSMessageErrorCode.apiUnavailableInPresentationContext`](msmessageerrorcode/apiunavailableinpresentationcontext.md) error.

This method operates asynchronously. Although the method returns immediately, the actual work is deferred and performed in the background. As soon as the message starts to send, the system calls the completion block on a background queue.

Subsequent calls to this method replace any existing message in the input field.

If the message was initialized using the session from an existing message, a new message isn’t added to the transcript. Instead, the system takes the following steps as soon as the user sends the message:

1. The system moves the existing message to the bottom of the conversation transcript.
2. It updates the message with the new content.

## Parameters

- `message`: The message object to send.
- `completionHandler`: A block that’s called as soon as the message starts sending. This block is passed the following parameter:

## See Also

- [func sendAttachment(URL, withAlternateFilename: String?, completionHandler: (((any Error)?) -> Void)?)](msconversation/sendattachment(_:withalternatefilename:completionhandler:).md)
  Sends the media file specified by the given URL.
- [func send(MSSticker, completionHandler: (((any Error)?) -> Void)?)](msconversation/send(_:completionhandler:)-4kje0.md)
  Sends a sticker.
- [func sendText(String, completionHandler: (((any Error)?) -> Void)?)](msconversation/sendtext(_:completionhandler:).md)
  Sends a text message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msconversation/send(_:completionhandler:)-9krz)*