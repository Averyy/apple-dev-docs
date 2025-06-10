# QLPreviewPanel

**Framework**: Quick Look UI  
**Kind**: class

A class that implements the Quick Look preview panel to display a preview of a list of items.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
class QLPreviewPanel
```

#### Overview

Every application has a single shared instance of [`QLPreviewPanel`](qlpreviewpanel.md) accessible through [`shared()`](qlpreviewpanel/shared().md). The preview panel follows the responder chain and adapts to the first responder willing to control it. A preview panel controller provides the content through methods defined in the [`QLPreviewPanelDataSource`](qlpreviewpaneldatasource.md) protocol.

You can’t subclass [`QLPreviewPanel`](qlpreviewpanel.md); you can, however, customize its behavior using a [`delegate`](qlpreviewpanel/delegate.md). See the [`QLPreviewPanelDelegate`](qlpreviewpaneldelegate.md) protocol for the methods to customize a preview panel’s behavior.

## Topics

### Accessing the Shared Panel
- [class func shared() -> QLPreviewPanel!](qlpreviewpanel/shared.md)
  Returns the shared Quick Look preview panel instance.
- [class func sharedPreviewPanelExists() -> Bool](qlpreviewpanel/sharedpreviewpanelexists.md)
  Returns a Boolean value that indicates whether the system has created a shared Quick Look preview panel.
### Accessing the Preview Panel Controller
- [var currentController: Any!](qlpreviewpanel/currentcontroller.md)
  The current first responder accepting to control the preview panel.
- [func updateController()](qlpreviewpanel/updatecontroller.md)
  Asks the preview panel to update its current controller.
### Managing the Preview Items
- [var dataSource: (any QLPreviewPanelDataSource)!](qlpreviewpanel/datasource.md)
  The preview panel data source.
- [func reloadData()](qlpreviewpanel/reloaddata.md)
  Asks the preview panel to reload its data from its data source.
- [func refreshCurrentPreviewItem()](qlpreviewpanel/refreshcurrentpreviewitem.md)
  Asks the preview panel to recompute the preview of the current preview item.
- [var currentPreviewItemIndex: Int](qlpreviewpanel/currentpreviewitemindex.md)
  The index of the current preview item.
- [var currentPreviewItem: (any QLPreviewItem)!](qlpreviewpanel/currentpreviewitem.md)
  The currently previewed item.
- [var displayState: Any!](qlpreviewpanel/displaystate.md)
  The preview panel’s display state.
### The Panel’s Delegate
- [var delegate: AnyObject!](qlpreviewpanel/delegate.md)
  The delegate object that controls the preview panel’s behavior.
### Managing Full Screen Mode
- [func enterFullScreenMode(NSScreen!, withOptions: [AnyHashable : Any]!) -> Bool](qlpreviewpanel/enterfullscreenmode(_:withoptions:).md)
  Instructs the panel to enter full screen mode.
- [func exitFullScreenMode(options: [AnyHashable : Any]!)](qlpreviewpanel/exitfullscreenmode(options:).md)
  Instructs the panel to exit full screen mode.
- [var isInFullScreenMode: Bool](qlpreviewpanel/isinfullscreenmode.md)
  The property that indicates whether the panel is in full screen mode.

## Relationships

### Inherits From
- [NSPanel](../AppKit/NSPanel.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSMenuItemValidation](../AppKit/NSMenuItemValidation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [NSUserInterfaceValidations](../AppKit/NSUserInterfaceValidations.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class QLPreviewView](qlpreviewview.md)
  A Quick Look preview of an item that you can embed into your view hierarchy.
- [protocol QLPreviewItem](qlpreviewitem.md)
  A protocol that defines a set of properties you implement to make a preview of your application’s content.
- [protocol QLPreviewPanelDataSource](qlpreviewpaneldatasource.md)
  A protocol that the Quick Look preview panel uses to access the contents of its data source object.
- [protocol QLPreviewPanelDelegate](qlpreviewpaneldelegate.md)
  A protocol for the delegate of the Quick Look preview panel.
- [typealias QLPreviewItemLoadingBlock](qlpreviewitemloadingblock.md)
  A type that defines a block used to load a Quick Look preview item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewpanel)*