# stickerBrowserView(_:stickerAt:)

**Framework**: Messages  
**Kind**: method  
**Required**: Yes

Asks the data source for the sticker object that the browser will display at the provided index.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func stickerBrowserView(_ stickerBrowserView: MSStickerBrowserView, stickerAt index: Int) -> MSSticker
```

#### Return Value

A valid sticker object.

#### Discussion

Do not perform any time-intensive activities in this method. For example, creating a sticker from a local image file should be fine, but you can’t download an image for your sticker.

## Parameters

- `stickerBrowserView`: The sticker browser view that displays these stickers.
- `index`: The index of the desired sticker.

## See Also

- [func numberOfStickers(in: MSStickerBrowserView) -> Int](msstickerbrowserviewdatasource/numberofstickers(in:).md)
  Asks the data source for the number of stickers that the browser will display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickerbrowserviewdatasource/stickerbrowserview(_:stickerat:))*