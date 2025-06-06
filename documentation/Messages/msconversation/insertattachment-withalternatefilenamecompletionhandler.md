# insertAttachment(_:withAlternateFilename:completionHandler:)

**Framework**: Messages  
**Kind**: method

Inserts an attachment into the current context.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func insertAttachment(_ URL: URL, withAlternateFilename filename: String?) async throws
```

## Mentions

- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime.md)

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func insertAttachment(_ URL: URL, withAlternateFilename filename: String?) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func insertAttachment(_ URL: URL, withAlternateFilename filename: String?) async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Use this method to insert a media attachment into the current context. For the [`MSMessagesAppPresentationContext.messages`](msmessagesapppresentationcontext/messages.md) context, this method inserts the attachment into the Message app’s input field. Users can then send the media file by tapping Send.

For the [`MSMessagesAppPresentationContext.media`](msmessagesapppresentationcontext/media.md) context, the method only supports images. It places the image in the Messages camera or FaceTime. If the attachment is not an image type supported by [`MSSticker`](mssticker.md), the method fails with an [`MSMessageErrorCode.apiUnavailableInPresentationContext`](msmessageerrorcode/apiunavailableinpresentationcontext.md) error.

This method operates asynchronously. Although the method returns immediately, the actual work is deferred and performed in the background. As soon as the attachment is inserted, the system calls the completion block on a background queue.

> **Note**:  This method does not send the media file. It inserts the media file into the Messages app’s input field. The file is not sent until the user taps Send.

 This method does not send the media file. It inserts the media file into the Messages app’s input field. The file is not sent until the user taps Send.

## Parameters

- `URL`: A URL for the media file to be inserted. This URL must refer to a file saved on the device.
- `filename`: An alternate name for the file. Use an alternate filename to better describe the attachment or to make the name more readable. If you pass a string, the Messages app uses the string as the attachment’s filename. If you pass  , it parses the filename from the URL.
- `completionHandler`: A block that is called as soon as the insertion is complete. This block is passed the following parameter:

## See Also

- [func insert(MSMessage, completionHandler: (((any Error)?) -> Void)?)](msconversation/insert(_:completionhandler:)-3g248.md)
  Inserts a message object into the Messages app’s input field.
- [func insert(MSSticker, completionHandler: (((any Error)?) -> Void)?)](msconversation/insert(_:completionhandler:)-7fpdd.md)
  Inserts a sticker into the current context.
- [func insertText(String, completionHandler: (((any Error)?) -> Void)?)](msconversation/inserttext(_:completionhandler:).md)
  Inserts text into the Messages app’s input field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msconversation/insertattachment(_:withalternatefilename:completionhandler:))*