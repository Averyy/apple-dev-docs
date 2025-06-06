# Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime

**Framework**: Messages

Enable your Sticker pack or iMessage app in the media context.

#### Overview

In iOS 12 and later, Sticker packs and iMessage apps can appear in multiple contexts.

People can access stickers throughout iOS through the emoji keyboard. To access effects in the Messages camera or FaceTime, a person taps the effects button. The system then displays all the iMessage apps and Sticker packs that support the media context. A person can launch an app, and use it to add images or stickers to the camera.

iMessage apps only appear in the `messages` context. To enable support for the `media` context, set the `MSSupportedPresentationContexts` key in your extension’s `Info.plist` file. If you indicate support for both `messages` and `media`, your Stickers only present in the `media` context including in Messages.

A Sticker pack or iMessage app’s context limits its available features. For example, In the [`MSMessagesAppPresentationContext.messages`](msmessagesapppresentationcontext/messages.md) context, a person can peel off stickers and attach them to any bubbles in the current conversation. Your app can also programatically send stickers, images, text, or interactive messages.

In the [`MSMessagesAppPresentationContext.media`](msmessagesapppresentationcontext/media.md) context, your app appears in effects in Messages and FaceTime. Therefore, the system limits your app to features that make sense over a photo or video. For instance, a person can’t play an interactive game while taking a photo; however, they can add stickers or images to the picture.

##### Specify the Supported Contexts

To specify the supported contexts:

1. Open the `Info.plist` file for your Sticker pack or iMessage app extension.
2. Add the `MSSupportedPresentationContexts` key, using an Array type.
3. Add String values for the supported contexts. For the [`MSMessagesAppPresentationContext.messages`](msmessagesapppresentationcontext/messages.md) context, add the `MSMessagesAppPresentationContextMessages` value. For [`MSMessagesAppPresentationContext.media`](msmessagesapppresentationcontext/media.md), add `MSMessagesAppPresentationContextMedia`.

You must specify one of the contexts, but if you specify both contexts, they only present in the [`MSMessagesAppPresentationContext.media`](msmessagesapppresentationcontext/media.md) context.

For more information on setting I`nfo.plist` keys, see [`Edit property lists`](https://developer.apple.comhttps://help.apple.com/xcode/mac/9.3/#/dev3f399a2a6).

##### Work with the Media Context

The [`MSMessagesAppPresentationContext.media`](msmessagesapppresentationcontext/media.md) context supports only a subset of the features provided by the Messages framework. People can peel stickers from a sticker browser view, and place them in the Messages camera or FaceTime. They can reposition, resize, rotate, or remove stickers from the viewfinder.

iMessage apps can also insert stickers or images into the viewfinder using the [`insert(_:completionHandler:)`](msconversation/insert(_:completionhandler:)-7fpdd.md) or [`insertAttachment(_:withAlternateFilename:completionHandler:)`](msconversation/insertattachment(_:withalternatefilename:completionhandler:).md) methods. However, if the attachment isn’t an image supported by [`MSSticker`](mssticker.md), then the [`insertAttachment(_:withAlternateFilename:completionHandler:)`](msconversation/insertattachment(_:withalternatefilename:completionhandler:).md) method fails with an [`MSMessageErrorCode.apiUnavailableInPresentationContext`](msmessageerrorcode/apiunavailableinpresentationcontext.md) error.

Additionally, you can’t insert interactive messages or text into the media context. You also can’t send items automatically. Therefore, the following methods from the [`MSConversation`](msconversation.md) class aren’t available:

- [`insert(_:completionHandler:)`](msconversation/insert(_:completionhandler:)-3g248.md)
- [`insertText(_:completionHandler:)`](msconversation/inserttext(_:completionhandler:).md)
- [`sendAttachment(_:withAlternateFilename:completionHandler:)`](msconversation/sendattachment(_:withalternatefilename:completionhandler:).md)
- [`send(_:completionHandler:)`](msconversation/send(_:completionhandler:)-9krz.md)
- [`send(_:completionHandler:)`](msconversation/send(_:completionhandler:)-4kje0.md)
- [`sendText(_:completionHandler:)`](msconversation/sendtext(_:completionhandler:).md)

If you call these methods, they fail with an [`MSMessageErrorCode.apiUnavailableInPresentationContext`](msmessageerrorcode/apiunavailableinpresentationcontext.md) error.

Additionally, because you can’t send or receive interactive messages, the system never calls the following methods in the [`MSMessagesAppPresentationContext.media`](msmessagesapppresentationcontext/media.md) context:

- [`willSelect(_:conversation:)`](msmessagesappviewcontroller/willselect(_:conversation:).md)
- [`didSelect(_:conversation:)`](msmessagesappviewcontroller/didselect(_:conversation:).md)
- [`didReceive(_:conversation:)`](msmessagesappviewcontroller/didreceive(_:conversation:).md)
- [`didStartSending(_:conversation:)`](msmessagesappviewcontroller/didstartsending(_:conversation:).md)
- [`didCancelSending(_:conversation:)`](msmessagesappviewcontroller/didcancelsending(_:conversation:).md)

Finally, the [`MSMessagesAppPresentationContext.media`](msmessagesapppresentationcontext/media.md) context is already inside the Messages camera or FaceTime; therefore, you can’t display another camera inside the current viewfinder.

##### Detect the Current Context

Use the [`MSMessagesAppViewController`](msmessagesappviewcontroller.md) object’s [`presentationContext`](msmessagesappviewcontroller/presentationcontext.md) property to determine your iMessage app’s current context. Enable only the features that make sense in that context.

```swift
if presentationContext == .messages {
    // The system is presenting your iMessage app inside the Messages app.
    // You have full access to the Messages framework.
    // You can insert or send stickers, text, attachments, or interactive messages.
} else if presentationContext == .media {
    // The system is presenting your iMessage app in effects.
    // You can only insert stickers and images.
}
```

## See Also

- [Adding your sticker packs to Messages](adding-your-sticker-packs-to-messages.md)
  Drag and drop your sticker pack into the Stickers asset catalog to let people access your stickers from Messages.
- [class MSStickerBrowserViewController](msstickerbrowserviewcontroller.md)
  A view controller that provides dynamic content to the standard sticker browser.
- [class MSStickerBrowserView](msstickerbrowserview.md)
  A browser view that displays a dynamically generated list of stickers.
- [class MSStickerView](msstickerview.md)
  A view for displaying a sticker.
- [enum MSStickerSize](msstickersize.md)
  The size of the stickers in the browser view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime)*