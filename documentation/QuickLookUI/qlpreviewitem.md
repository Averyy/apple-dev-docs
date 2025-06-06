# QLPreviewItem

**Framework**: Quick Look UI  
**Kind**: protocol

A protocol that defines a set of properties you implement to make a preview of your application’s content.

**Availability**:
- macOS 10.6+

## Declaration

```swift
protocol QLPreviewItem : NSObjectProtocol
```

#### Overview

Implement the properties in this protocol to make your application’s content visible in a Quick Look preview. Use  [`QLPreviewController`](https://developer.apple.com/documentation/QuickLook/QLPreviewController) to display a Quick Look preview on iOS, [`QLPreviewPanel`](qlpreviewpanel.md) and [`QLPreviewView`](qlpreviewview.md) on macOS.

The properties in the [`QLPreviewItem`](qlpreviewitem.md) protocol are also declared as a category on the `NSURL` class. As a result, you can use [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) objects directly as preview items — provided that you want to use the default titles of those items. The default title for an NSURL object is the last path component of an item’s URL. To supply custom titles for preview objects, implement a class conforming to this protocol, supplying the title with the [`previewItemTitle`](qlpreviewitem/previewitemtitle.md) property.

## Topics

### Instance Properties
- [var previewItemDisplayState: Any!](qlpreviewitem/previewitemdisplaystate.md)
  The display state for the preview item.
- [var previewItemTitle: String!](qlpreviewitem/previewitemtitle.md)
  The title to display for the preview item.
- [var previewItemURL: URL!](qlpreviewitem/previewitemurl.md)
  The URL of the item to preview.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class QLPreviewPanel](qlpreviewpanel.md)
  A class that implements the Quick Look preview panel to display a preview of a list of items.
- [class QLPreviewView](qlpreviewview.md)
  A Quick Look preview of an item that you can embed into your view hierarchy.
- [protocol QLPreviewPanelDataSource](qlpreviewpaneldatasource.md)
  A protocol that the Quick Look preview panel uses to access the contents of its data source object.
- [protocol QLPreviewPanelDelegate](qlpreviewpaneldelegate.md)
  A protocol for the delegate of the Quick Look preview panel.
- [typealias QLPreviewItemLoadingBlock](qlpreviewitemloadingblock.md)
  A type that defines a block used to load a Quick Look preview item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewitem)*