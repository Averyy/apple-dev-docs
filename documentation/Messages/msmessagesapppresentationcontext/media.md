# MSMessagesAppPresentationContext.media

**Framework**: Messages  
**Kind**: case  
**Role**: Case

A constant that indicates the iMessage app appears inside the Stickers app throughout iOS including in Messages, FaceTime, the emoji keyboard, and Markup.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case media
```

```c
MSMessagesAppPresentationContextMedia
```

## Mentions

- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](../adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime.md)

#### Discussion

The media context supports only a subset of the Messages framework API. Specifically, the following limits apply:

- The iMessage app can only insert sticker and image attachments. You can’t insert [`MSMessage`](../msmessage.md) objects, text, or non-image assets.
- You can’t use any of the [`MSConversation`](../msconversation.md) class’s `send` messages ([`sendAttachment(_:withAlternateFilename:completionHandler:)`](../msconversation/sendattachment%28_,withalternatefilename,completionhandler%29.md), [`send(_:completionHandler:)`](../msconversation/send%28_,completionhandler%29-9krz.md), [`send(_:completionHandler:)`](../msconversation/send%28_,completionhandler%29-4kje0.md), or [`sendText(_:completionHandler:)`](../msconversation/sendtext%28_,completionhandler%29.md)).
- You can’t display a camera inside an [`MSMessagesAppPresentationContext.media`](./media.md) context.

## See Also

### Presentation Contexts
- [MSMessagesAppPresentationContext.messages](./messages.md)
  A constant that indicates the iMessage app appears in Messages in the list of iMessage apps that appears when you press the plus button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesapppresentationcontext/media)*