# MSStickerSize

**Framework**: Messages  
**Kind**: enum

The size of the stickers in the browser view.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum MSStickerSize
```

#### Overview

The browser scales down sticker images to fit. If a sticker is smaller than the provided space, the browser centers the sticker in the space.

## Topics

### Constants
- [MSStickerSize.small](msstickersize/small.md)
  Small stickers.
- [MSStickerSize.regular](msstickersize/regular.md)
  Medium-sized stickers.
- [MSStickerSize.large](msstickersize/large.md)
  Large stickers.
### Initializers
- [init?(rawValue: Int)](msstickersize/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime.md)
  Enable your Sticker pack or iMessage app in the media context.
- [Adding your sticker packs to Messages](adding-your-sticker-packs-to-messages.md)
  Drag and drop your sticker pack into the Stickers asset catalog to let people access your stickers from Messages.
- [class MSStickerBrowserViewController](msstickerbrowserviewcontroller.md)
  A view controller that provides dynamic content to the standard sticker browser.
- [class MSStickerBrowserView](msstickerbrowserview.md)
  A browser view that displays a dynamically generated list of stickers.
- [class MSStickerView](msstickerview.md)
  A view for displaying a sticker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickersize)*