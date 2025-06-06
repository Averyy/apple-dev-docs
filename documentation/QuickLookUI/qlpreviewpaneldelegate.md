# QLPreviewPanelDelegate

**Framework**: Quick Look UI  
**Kind**: protocol

A protocol for the delegate of the Quick Look preview panel.

**Availability**:
- macOS 12.0+

## Declaration

```swift
protocol QLPreviewPanelDelegate : NSWindowDelegate
```

#### Overview

You can implement these methods to perform custom tasks in response to events in the preview panel.

## Topics

### Optional Methods
- [func previewPanel(QLPreviewPanel!, handle: NSEvent!) -> Bool](qlpreviewpaneldelegate/previewpanel(_:handle:).md)
  Handles an event that the preview panel receives, but doesn’t handle.
- [func previewPanel(QLPreviewPanel!, sourceFrameOnScreenFor: (any QLPreviewItem)!) -> NSRect](qlpreviewpaneldelegate/previewpanel(_:sourceframeonscreenfor:).md)
  Returns the screen rectangle for a given preview item.
- [func previewPanel(QLPreviewPanel!, transitionImageFor: (any QLPreviewItem)!, contentRect: UnsafeMutablePointer<NSRect>!) -> Any!](qlpreviewpaneldelegate/previewpanel(_:transitionimagefor:contentrect:).md)
  Returns the image to use for the transition zoom effect for a given item.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSWindowDelegate](../AppKit/NSWindowDelegate.md)

## See Also

- [class QLPreviewPanel](qlpreviewpanel.md)
  A class that implements the Quick Look preview panel to display a preview of a list of items.
- [class QLPreviewView](qlpreviewview.md)
  A Quick Look preview of an item that you can embed into your view hierarchy.
- [protocol QLPreviewItem](qlpreviewitem.md)
  A protocol that defines a set of properties you implement to make a preview of your application’s content.
- [protocol QLPreviewPanelDataSource](qlpreviewpaneldatasource.md)
  A protocol that the Quick Look preview panel uses to access the contents of its data source object.
- [typealias QLPreviewItemLoadingBlock](qlpreviewitemloadingblock.md)
  A type that defines a block used to load a Quick Look preview item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpaneldelegate)*