# Protocol Implementations

**Framework**: AppKit

Access the split view controller’s implementations of protocol methods.

#### Overview

[`NSSplitViewController`](nssplitviewcontroller.md) conforms to [`NSSplitViewDelegate`](nssplitviewdelegate.md) to serve as its split view’s delegate. This page lists the split view controller type’s implementations of those protocol methods. If you override these methods in a subclass, you must call `super`.

[`NSSplitViewController`](nssplitviewcontroller.md) also conforms to [`NSUserInterfaceValidations`](nsuserinterfacevalidations.md) by implementing [`validateUserInterfaceItem(_:)`](nssplitviewcontroller/validateuserinterfaceitem(_:).md).

## Topics

### Configuring and Drawing View Dividers
- [func splitView(NSSplitView, effectiveRect: NSRect, forDrawnRect: NSRect, ofDividerAt: Int) -> NSRect](nssplitviewcontroller/splitview(_:effectiverect:fordrawnrect:ofdividerat:).md)
  Allows the split view controller to modify the rectangle where mouse clicks initiate divider dragging.
- [func splitView(NSSplitView, shouldHideDividerAt: Int) -> Bool](nssplitviewcontroller/splitview(_:shouldhidedividerat:).md)
  Allows the split view controller to determine whether the user can drag a divider or adjust it off the edge of the split view.
- [func splitView(NSSplitView, additionalEffectiveRectOfDividerAt: Int) -> NSRect](nssplitviewcontroller/splitview(_:additionaleffectiverectofdividerat:).md)
  Allows the split view controller to return an additional rectangle where mouse clicks can initiate divider dragging.
### Managing Subviews
- [func splitView(NSSplitView, canCollapseSubview: NSView) -> Bool](nssplitviewcontroller/splitview(_:cancollapsesubview:).md)
  Allows the split view controller to determine whether the user can collapse and expand the specified subview.
- [func splitView(NSSplitView, shouldCollapseSubview: NSView, forDoubleClickOnDividerAt: Int) -> Bool](nssplitviewcontroller/splitview(_:shouldcollapsesubview:fordoubleclickondividerat:).md)
  Allows the split view controller to determine if a subview collapses in response to a double click.
### Validating User Interface Items
- [func validateUserInterfaceItem(any NSValidatedUserInterfaceItem) -> Bool](nssplitviewcontroller/validateuserinterfaceitem(_:).md)
  Returns a Boolean value that indicates whether to enable the specified item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller-protocol-implementations)*