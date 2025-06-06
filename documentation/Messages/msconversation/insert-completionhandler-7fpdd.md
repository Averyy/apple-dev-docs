# insert(_:completionHandler:)

**Framework**: Messages  
**Kind**: method

Inserts a sticker into the current context.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func insert(_ sticker: MSSticker) async throws
```

## Mentions

- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func insert(_ sticker: MSSticker) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func insert(_ sticker: MSSticker) async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Use this method to insert a sticker into the current context.

- For the [`MSMessagesAppPresentationContext.messages`](msmessagesapppresentationcontext/messages.md) context, the method places the sticker in the Message app’s input field. Users can then send the sticker by tapping Send.
- For the [`MSMessagesAppPresentationContext.media`](msmessagesapppresentationcontext/media.md) context, the method places the image in the Messages camera or FaceTime.

This method operates asynchronously. Although the method returns immediately, the actual work is deferred and performed in the background. As soon as the attachment is inserted, the system calls the completion block on a background queue.

> **Note**:  This method does not send the sticker. It inserts the sticker into the Messages app’s input field. The sticker is not sent until the user taps Send.

 This method does not send the sticker. It inserts the sticker into the Messages app’s input field. The sticker is not sent until the user taps Send.

## Parameters

- `sticker`: The sticker to be inserted.
- `completionHandler`: A block that is called as soon as the insertion is complete. This block is passed the following parameter:

## See Also

- [func insertAttachment(URL, withAlternateFilename: String?, completionHandler: (((any Error)?) -> Void)?)](msconversation/insertattachment(_:withalternatefilename:completionhandler:).md)
  Inserts an attachment into the current context.
- [func insert(MSMessage, completionHandler: (((any Error)?) -> Void)?)](msconversation/insert(_:completionhandler:)-3g248.md)
  Inserts a message object into the Messages app’s input field.
- [func insertText(String, completionHandler: (((any Error)?) -> Void)?)](msconversation/inserttext(_:completionhandler:).md)
  Inserts text into the Messages app’s input field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msconversation/insert(_:completionhandler:)-7fpdd)*