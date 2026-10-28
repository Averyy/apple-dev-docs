# MSStickerBrowserViewDataSource

**Framework**: Messages  
**Kind**: protocol  
**Role**: Protocol

The protocol for dynamically providing stickers to a browser view.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol MSStickerBrowserViewDataSource : NSObjectProtocol
```

```objc
@protocol MSStickerBrowserViewDataSource <NSObject>
```

## Overview

To load its stickers, the [`MSStickerBrowserView`](./msstickerbrowserview.md) class performs the following steps:

1. The browser calls the data source’s [`numberOfStickers(in:)`](./msstickerbrowserviewdatasource/numberofstickers%28in%29.md) method to get the number of stickers.
2. The browser repeatedly calls the data source’s [`stickerBrowserView(_:stickerAt:)`](./msstickerbrowserviewdatasource/stickerbrowserview%28_,stickerat%29.md) method to load the individual stickers. Initially, the browser requests only enough stickers to fill the screen. The browser requests additional stickers as the user scrolls and new stickers become visible.

Both methods are required. If the sticker collection changes at runtime, call the [`MSStickerBrowserView`](./msstickerbrowserview.md) class’s [`reloadData()`](./msstickerbrowserview/reloaddata%28%29.md) method to reload the stickers.

## Topics

### Providing Stickers
- [func numberOfStickers(in: MSStickerBrowserView) -> Int](./msstickerbrowserviewdatasource/numberofstickers%28in%29.md)
  Asks the data source for the number of stickers that the browser will display.
- [func stickerBrowserView(MSStickerBrowserView, stickerAt: Int) -> MSSticker](./msstickerbrowserviewdatasource/stickerbrowserview%28_,stickerat%29.md)
  Asks the data source for the sticker object that the browser will display at the provided index.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [MSStickerBrowserViewController](./msstickerbrowserviewcontroller.md)

## See Also

### Managing the Sticker Collection Contents
- [var dataSource: (any MSStickerBrowserViewDataSource)?](./msstickerbrowserview/datasource.md)
  The sticker browser’s data source.
- [func reloadData()](./msstickerbrowserview/reloaddata%28%29.md)
  Asks the sticker browser to reload its data from the data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msstickerbrowserviewdatasource)*