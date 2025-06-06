# Adding your sticker packs to Messages

**Framework**: Messages

Drag and drop your sticker pack into the Stickers asset catalog to let people access your stickers from Messages.

#### Overview

Sticker packs provide static sets of , images that users can send inline as messages or peel off and attach to message bubbles in the transcript. Sticker packs don’t require any code. You add stickers by dragging image files into the Sticker Pack folder inside the Stickers asset catalog. People can use your stickers across the system outside of messages.

Valid image files meet the following specifications:

- The image is a PNG, APNG, GIF, JPEG, HEIC, or HEICS file.
- The file is less than 500 KB.
- For the best results, use images that are between 100 x 100 and 206 x 206 points.

> **Note**:  Always provide @3x images (300 x 300 pixels to 618 x 618 pixels). The system generates the @2x and @1x versions by downscaling the @3x images at runtime.

Messages supports three sticker sizes, which the system displays in a grid-based browser. In the Xcode Attributes inspector, pick one of the following sizes for your sticker pack:

- Small. 100 x 100 points @3x (300 x 300 pixels).
- Medium. 136 x 136 points @3x (408 x 408 pixels).
- Large. 206 x 206 points @3x (618 x 618 pixels).

For optimal quality and performance, provide sticker images of the size you choose. For more information on creating animated stickers, see [`Creating Stickers with Motion`](https://developer.apple.comhttps://developer.apple.com/support/stickers/motion/). For more information on submitting Sticker packs to the App Store, see [`Preparing Sticker Submissions`](https://developer.apple.comhttps://developer.apple.com/app-store/sticker-submissions/).

##### Specify Sticker Availability

You can either restrict your sticker pack to just Messages, or make it available throughout the system. To specify which apps your sticker pack is available in, update your `Info.plist` file. Add the `NSStickerSharingLevel` key inside your Messages extension’s `Info.plist` file. The value for this key is the string `{OS}`. Messages checks for the presence of the `Info.plist` key when your app launches outside of Messages. If you add this key to your app, your sticker pack doesn’t appear in the list.

## See Also

- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime.md)
  Enable your Sticker pack or iMessage app in the media context.
- [class MSStickerBrowserViewController](msstickerbrowserviewcontroller.md)
  A view controller that provides dynamic content to the standard sticker browser.
- [class MSStickerBrowserView](msstickerbrowserview.md)
  A browser view that displays a dynamically generated list of stickers.
- [class MSStickerView](msstickerview.md)
  A view for displaying a sticker.
- [enum MSStickerSize](msstickersize.md)
  The size of the stickers in the browser view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/Messages/adding-your-sticker-packs-to-messages)*