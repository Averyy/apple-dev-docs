# numberOfStickers(in:)

**Framework**: Messages  
**Kind**: method  
**Required**: Yes

Asks the data source for the number of stickers that the browser will display.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func numberOfStickers(in stickerBrowserView: MSStickerBrowserView) -> Int
```

#### Return Value

The number of stickers. This must be a non-negative number.

## Parameters

- `stickerBrowserView`: The sticker browser view that displays these stickers.

## See Also

- [func stickerBrowserView(MSStickerBrowserView, stickerAt: Int) -> MSSticker](msstickerbrowserviewdatasource/stickerbrowserview(_:stickerat:).md)
  Asks the data source for the sticker object that the browser will display at the provided index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickerbrowserviewdatasource/numberofstickers(in:))*