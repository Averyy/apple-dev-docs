# MSMessagesAppPresentationContext.media

**Framework**: Messages  
**Kind**: case

A constant that indicates the iMessage app appears inside the Stickers app throughout iOS including in Messages, FaceTime, the emoji keyboard, and Markup.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case media
```

## Mentions

- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime.md)

#### Discussion

The media context supports only a subset of the Messages framework API. Specifically, the following limits apply:

- The iMessage app can only insert sticker and image attachments. You can’t insert [`MSMessage`](msmessage.md) objects, text, or non-image assets.
- You can’t use any of the [`MSConversation`](msconversation.md) class’s `send` messages ([`sendAttachment(_:withAlternateFilename:completionHandler:)`](msconversation/sendattachment(_:withalternatefilename:completionhandler:).md), [`send(_:completionHandler:)`](msconversation/send(_:completionhandler:)-9krz.md), [`send(_:completionHandler:)`](msconversation/send(_:completionhandler:)-4kje0.md), or [`sendText(_:completionHandler:)`](msconversation/sendtext(_:completionhandler:).md)).
- You can’t display a camera inside an [`MSMessagesAppPresentationContext.media`](msmessagesapppresentationcontext/media.md) context.

## See Also

- [MSMessagesAppPresentationContext.messages](msmessagesapppresentationcontext/messages.md)
  A constant that indicates the iMessage app appears in Messages in the list of iMessage apps that appears when you press the plus button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesapppresentationcontext/media)*