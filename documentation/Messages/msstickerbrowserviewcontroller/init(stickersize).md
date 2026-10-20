# init(stickerSize:)

**Framework**: Messages  
**Kind**: init  
**Role**: Initializer

Creates a new sticker browser view controller with stickers of the provided size.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(stickerSize: MSStickerSize)
```

```objc
- (instancetype) initWithStickerSize:(MSStickerSize) stickerSize;
```

#### Return Value

A newly instantiated sticker browser controller.

## Parameters

- `stickerSize`: A constant that indicates the size of the stickers. For a list of possible values, see [`MSStickerSize`](../msstickersize.md).

## See Also

### Working with Stickers
- [var stickerBrowserView: MSStickerBrowserView](./stickerbrowserview.md)
  The sticker browser view managed by this controller.
- [var stickerSize: MSStickerSize](./stickersize.md)
  A constant that indicates the size of the stickers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickerbrowserviewcontroller/init(stickersize:))*