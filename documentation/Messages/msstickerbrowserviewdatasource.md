# MSStickerBrowserViewDataSource

**Framework**: Messages  
**Kind**: protocol

The protocol for dynamically providing stickers to a browser view.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol MSStickerBrowserViewDataSource : NSObjectProtocol
```

#### Overview

To load its stickers, the [`MSStickerBrowserView`](msstickerbrowserview.md) class performs the following steps:

1. The browser calls the data source’s [`numberOfStickers(in:)`](msstickerbrowserviewdatasource/numberofstickers(in:).md) method to get the number of stickers.
2. The browser repeatedly calls the data source’s [`stickerBrowserView(_:stickerAt:)`](msstickerbrowserviewdatasource/stickerbrowserview(_:stickerat:).md) method to load the individual stickers. Initially, the browser requests only enough stickers to fill the screen. The browser requests additional stickers as the user scrolls and new stickers become visible.

Both methods are required. If the sticker collection changes at runtime, call the [`MSStickerBrowserView`](msstickerbrowserview.md) class’s [`reloadData()`](msstickerbrowserview/reloaddata().md) method to reload the stickers.

## Topics

### Providing Stickers
- [func numberOfStickers(in: MSStickerBrowserView) -> Int](msstickerbrowserviewdatasource/numberofstickers(in:).md)
  Asks the data source for the number of stickers that the browser will display.
- [func stickerBrowserView(MSStickerBrowserView, stickerAt: Int) -> MSSticker](msstickerbrowserviewdatasource/stickerbrowserview(_:stickerat:).md)
  Asks the data source for the sticker object that the browser will display at the provided index.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [MSStickerBrowserViewController](msstickerbrowserviewcontroller.md)

## See Also

- [var dataSource: (any MSStickerBrowserViewDataSource)?](msstickerbrowserview/datasource.md)
  The sticker browser’s data source.
- [func reloadData()](msstickerbrowserview/reloaddata.md)
  Asks the sticker browser to reload its data from the data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickerbrowserviewdatasource)*