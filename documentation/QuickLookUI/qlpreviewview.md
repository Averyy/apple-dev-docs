# QLPreviewView

**Framework**: Quick Look UI  
**Kind**: class  
**Role**: Class

A Quick Look preview of an item that you can embed into your view hierarchy.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class QLPreviewView
```

```objc
@interface QLPreviewView : NSView
```

## Topics

### Creating a Preview View
- [init!(frame: NSRect, style: QLPreviewViewStyle)](./qlpreviewview/init%28frame,style%29.md)
  Creates a preview view with the provided frame and style.
- [init!(frame: NSRect)](./qlpreviewview/init%28frame%29.md)
  Creates a preview view with the provided frame.
- [enum QLPreviewViewStyle](./qlpreviewviewstyle.md)
  Styles for a Preview View.
### Displaying a Preview
- [var previewItem: (any QLPreviewItem)!](./qlpreviewview/previewitem.md)
  The item to preview.
- [func refreshPreviewItem()](./qlpreviewview/refreshpreviewitem%28%29.md)
  Updates the preview to display the currently previewed item.
- [var displayState: Any!](./qlpreviewview/displaystate.md)
  The current display state of the [`previewItem`](./qlpreviewview/previewitem.md).
- [var autostarts: Bool](./qlpreviewview/autostarts.md)
  A Boolean value that determines whether the preview starts automatically.
### Closing a Preview
- [var shouldCloseWithWindow: Bool](./qlpreviewview/shouldclosewithwindow.md)
  A Boolean value that determines whether the preview should close when its window closes.
- [func close()](./qlpreviewview/close%28%29.md)
  Closes the view, releasing the current preview item.

## Relationships

### Inherits From
- [NSView](../AppKit/nsview.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../AppKit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](../AppKit/nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Previews
- [class QLPreviewPanel](./qlpreviewpanel.md)
  A class that implements the Quick Look preview panel to display a preview of a list of items.
- [protocol QLPreviewItem](./qlpreviewitem.md)
  A protocol that defines a set of properties you implement to make a preview of your app’s content.
- [protocol QLPreviewPanelDataSource](./qlpreviewpaneldatasource.md)
  A protocol that the Quick Look preview panel uses to access the contents of its data source object.
- [protocol QLPreviewPanelDelegate](./qlpreviewpaneldelegate.md)
  A protocol for the delegate of the Quick Look preview panel.
- [typealias QLPreviewItemLoadingBlock](./qlpreviewitemloadingblock.md)
  A type that defines a block used to load a Quick Look preview item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewview)*