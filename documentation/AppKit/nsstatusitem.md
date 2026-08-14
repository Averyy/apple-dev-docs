# NSStatusItem

**Framework**: AppKit  
**Kind**: class

An individual element displayed in the system menu bar.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSStatusItem
```

#### Overview

The [`NSStatusBar`](nsstatusbar.md) method [`statusItem(withLength:)`](nsstatusbar/statusitem(withlength:).md) creates instances of this class and automatically adds them to the menu bar. Use the [`button`](nsstatusitem/button.md) property to customize the appearance and behavior of the status item.

## Topics

### Getting the item’s status bar
- [var statusBar: NSStatusBar?](nsstatusitem/statusbar.md)
  The status bar that displays the status item.
### Managing the status item’s behavior
- [var behavior: NSStatusItem.Behavior](nsstatusitem/behavior-swift.property.md)
  The set of allowed behaviors for the status item.
- [NSStatusItem.Behavior](nsstatusitem/behavior-swift.struct.md)
  A set of optional status item behaviors.
- [var button: NSStatusBarButton?](nsstatusitem/button.md)
  The button displayed in the status bar.
- [var menu: NSMenu?](nsstatusitem/menu.md)
  The pull-down menu displayed when the user clicks the status item.
### Configuring the status item’s appearance
- [var isVisible: Bool](nsstatusitem/isvisible.md)
  A Boolean value indicating if the menu bar currently displays the status item.
- [var length: CGFloat](nsstatusitem/length.md)
  The amount of space in the status bar that should be allocated to the status item.
- [class let squareLength: CGFloat](nsstatusitem/squarelength.md)
  A status item length that is equal to the status bar’s thickness.
- [class let variableLength: CGFloat](nsstatusitem/variablelength.md)
  A status item length that dynamically adjusts to the width of its contents.
- [var view: NSView?](nsstatusitem/view.md)
  The custom view the status item displays at its position in the status bar.
### Configuring target-action behavior
- [var target: AnyObject?](nsstatusitem/target.md)
  The object that receives the status item’s action message when someone clicks the status item.
- [var action: Selector?](nsstatusitem/action.md)
  The selector the status item sends to its target when someone clicks the status item.
### Managing the expanded interface
- [var expandedInterfaceDelegate: (any NSStatusItemExpandedInterfaceDelegate)?](nsstatusitem/expandedinterfacedelegate.md)
  The delegate that manages the lifecycle of the status item’s expanded interface.
- [var expandedInterfaceSession: NSStatusItemExpandedInterfaceSession?](nsstatusitem/expandedinterfacesession.md)
  A session object that tracks the lifecycle of the status item’s active expanded interface.
### Setting the autosave name
- [var autosaveName: NSStatusItem.AutosaveName!](nsstatusitem/autosavename-swift.property.md)
  A unique name for saving and restoring information about a status item.
- [NSStatusItem.AutosaveName](nsstatusitem/autosavename-swift.typealias.md)
### Deprecated
- [var isEnabled: Bool](nsstatusitem/isenabled.md)
  A Boolean that indicates whether the status item is enabled to respond to clicks.
- [var doubleAction: Selector?](nsstatusitem/doubleaction.md)
  The selector that is sent to the status item’s target when the status item is double-clicked.
- [func sendAction(on: NSEvent.EventTypeMask) -> Int](nsstatusitem/sendaction(on:).md)
  Sets the conditions on which the status item sends action messages to its target.
- [func popUpMenu(NSMenu)](nsstatusitem/popupmenu(_:).md)
  Displays a menu under a custom status bar item.
- [var title: String?](nsstatusitem/title.md)
  The string that is displayed at the status item’s position in the status bar.
- [var attributedTitle: NSAttributedString?](nsstatusitem/attributedtitle.md)
  The attributed string that is displayed at the status item’s position in the status bar.
- [var image: NSImage?](nsstatusitem/image.md)
  The image that is displayed at the status item’s position in the status bar.
- [var alternateImage: NSImage?](nsstatusitem/alternateimage.md)
  The alternate image to be displayed when a status bar item is highlighted.
- [var highlightMode: Bool](nsstatusitem/highlightmode.md)
  A Boolean that indicates whether the status item is highlighted when it is clicked.
- [var toolTip: String?](nsstatusitem/tooltip.md)
  The tool tip string that is displayed when the cursor pauses over the status item.
- [func drawStatusBarBackground(in: NSRect, withHighlight: Bool)](nsstatusitem/drawstatusbarbackground(in:withhighlight:).md)
  Draws the menu background pattern for a custom status-bar item in regular or highlight pattern.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class NSStatusBar](nsstatusbar.md)
  An object that manages a collection of status items displayed within the system-wide menu bar.
- [class NSStatusBarButton](nsstatusbarbutton.md)
  The appearance and behavior of an item in the systemwide menu bar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusitem)*