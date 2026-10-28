# MSStickerSize

**Framework**: Messages  
**Kind**: enum  
**Role**: Enumeration

The size of the stickers in the browser view.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum MSStickerSize
```

```c
enum MSStickerSize : NSInteger;
```

## Overview

The browser scales down sticker images to fit. If a sticker is smaller than the provided space, the browser centers the sticker in the space.

## Topics

### Constants
- [MSStickerSize.small](./msstickersize/small.md)
  Small stickers.
- [MSStickerSize.regular](./msstickersize/regular.md)
  Medium-sized stickers.
- [MSStickerSize.large](./msstickersize/large.md)
  Large stickers.
### Initializers
- [init?(rawValue: Int)](./msstickersize/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Custom sticker packs
- [Adding Sticker packs and iMessage apps to the system Stickers app, Messages camera, and FaceTime](./adding-sticker-packs-and-imessage-apps-to-the-system-stickers-app-messages-camera-and-facetime.md)
  Enable your Sticker pack or iMessage app in the media context.
- [Adding your sticker packs to Messages](./adding-your-sticker-packs-to-messages.md)
  Drag and drop your sticker pack into the Stickers asset catalog to let people access your stickers from Messages.
- [class MSStickerBrowserViewController](./msstickerbrowserviewcontroller.md)
  A view controller that provides dynamic content to the standard sticker browser.
- [class MSStickerBrowserView](./msstickerbrowserview.md)
  A browser view that displays a dynamically generated list of stickers.
- [class MSStickerView](./msstickerview.md)
  A view for displaying a sticker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickersize)*