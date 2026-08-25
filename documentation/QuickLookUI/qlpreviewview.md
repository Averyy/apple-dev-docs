# QLPreviewView

**Framework**: Quick Look UI  
**Kind**: class

A Quick Look preview of an item that you can embed into your view hierarchy.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class QLPreviewView
```

## Topics

### Creating a Preview View
- [init!(frame: NSRect, style: QLPreviewViewStyle)](qlpreviewview/init(frame:style:).md)
  Creates a preview view with the provided frame and style.
- [init!(frame: NSRect)](qlpreviewview/init(frame:).md)
  Creates a preview view with the provided frame.
- [enum QLPreviewViewStyle](qlpreviewviewstyle.md)
  Styles for a Preview View.
### Displaying a Preview
- [var previewItem: (any QLPreviewItem)!](qlpreviewview/previewitem.md)
  The item to preview.
- [func refreshPreviewItem()](qlpreviewview/refreshpreviewitem.md)
  Updates the preview to display the currently previewed item.
- [var displayState: Any!](qlpreviewview/displaystate.md)
  The current display state of the [`previewItem`](qlpreviewview/previewitem.md).
- [var autostarts: Bool](qlpreviewview/autostarts.md)
  A Boolean value that determines whether the preview starts automatically.
### Closing a Preview
- [var shouldCloseWithWindow: Bool](qlpreviewview/shouldclosewithwindow.md)
  A Boolean value that determines whether the preview should close when its window closes.
- [func close()](qlpreviewview/close.md)
  Closes the view, releasing the current preview item.

## Relationships

### Inherits From
- [NSView](../appkit/nsview.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../appkit/nsappearancecustomization.md)
- [NSCoding](../foundation/nscoding.md)
- [NSDraggingDestination](../appkit/nsdraggingdestination.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class QLPreviewPanel](qlpreviewpanel.md)
  A class that implements the Quick Look preview panel to display a preview of a list of items.
- [protocol QLPreviewItem](qlpreviewitem.md)
  A protocol that defines a set of properties you implement to make a preview of your application’s content.
- [protocol QLPreviewPanelDataSource](qlpreviewpaneldatasource.md)
  A protocol that the Quick Look preview panel uses to access the contents of its data source object.
- [protocol QLPreviewPanelDelegate](qlpreviewpaneldelegate.md)
  A protocol for the delegate of the Quick Look preview panel.
- [typealias QLPreviewItemLoadingBlock](qlpreviewitemloadingblock.md)
  A type that defines a block used to load a Quick Look preview item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewview)*