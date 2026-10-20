# Related UI

**Framework**: AppKit  
**Role**: API Collection

Manage contextual menus, cursors, tool tips, and other system-provided windows and content.

## Topics

### Managing Contextual Menus
- [func menu(for: NSEvent) -> NSMenu?](./nsview/menu%28for%29.md)
  Overridden by subclasses to return a context-sensitive pop-up menu for a given mouse-down event.
- [class var defaultMenu: NSMenu?](./nsview/defaultmenu.md)
  Overridden by subclasses to return the default pop-up menu for instances of the receiving class.
- [func willOpenMenu(NSMenu, with: NSEvent)](./nsview/willopenmenu%28_,with%29.md)
  Called just before a contextual menu for a view is opened on screen.
- [func didCloseMenu(NSMenu, with: NSEvent?)](./nsview/didclosemenu%28_,with%29.md)
  Called after a contextual menu that was displayed from the receiving view has been closed.
### Responding to Cursor Movements
- [func addCursorRect(NSRect, cursor: NSCursor)](./nsview/addcursorrect%28_,cursor%29.md)
  Establishes  the cursor to be used when the mouse pointer lies within a specified region.
- [func removeCursorRect(NSRect, cursor: NSCursor)](./nsview/removecursorrect%28_,cursor%29.md)
  Completely removes a cursor rectangle from the view.
- [func discardCursorRects()](./nsview/discardcursorrects%28%29.md)
  Invalidates all cursor rectangles set up using [`addCursorRect(_:cursor:)`](./nsview/addcursorrect%28_,cursor%29.md).
- [func resetCursorRects()](./nsview/resetcursorrects%28%29.md)
  Overridden by subclasses to define their default cursor rectangles.
### Providing a Tool Tip
- [var toolTip: String?](./nsview/tooltip.md)
  The text for the view’s tooltip.
- [func addToolTip(NSRect, owner: Any, userData: UnsafeMutableRawPointer?) -> NSView.ToolTipTag](./nsview/addtooltip%28_,owner,userdata%29.md)
  Creates a tooltip for a defined area in the view and returns a tag that identifies the tooltip rectangle.
- [func removeAllToolTips()](./nsview/removealltooltips%28%29.md)
  Removes all tooltips assigned to the view.
- [func removeToolTip(NSView.ToolTipTag)](./nsview/removetooltip%28_%29.md)
  Removes the tooltip identified by specified tag.
- [typealias ToolTipTag](./nsview/tooltiptag.md)
  This type describes the rectangle used to identify a tooltip rectangle.
### Displaying Definition Windows
- [func showDefinition(for: NSAttributedString?, at: NSPoint)](./nsview/showdefinition%28for,at%29.md)
  Shows a window displaying the definition of the attributed string at the specified point.
- [func showDefinition(for: NSAttributedString?, range: NSRange, options: [NSView.DefinitionOptionKey : Any]?, baselineOriginProvider: ((NSRange) -> NSPoint)?)](./nsview/showdefinition%28for,range,options,baselineoriginprovider%29.md)
  Shows a window displaying the definition of the specified range of the attributed string.
- [NSView.DefinitionOptionKey](./nsview/definitionoptionkey.md)
  Keys to include in your definition.
- [NSView.DefinitionPresentationType](./nsview/definitionpresentationtype.md)
  Presentation options for the window.
### Getting the Focus View
- [class var focusView: NSView?](./nsview/focusview.md)
  The currently focused view object.
### Synchronizing with Ruler Views
- [func rulerView(NSRulerView, didAdd: NSRulerMarker)](./nsview/rulerview%28_,didadd%29.md)
  Informs the client that `aRulerView` allowed the user to add `aMarker`.
- [func rulerView(NSRulerView, didMove: NSRulerMarker)](./nsview/rulerview%28_,didmove%29.md)
  Informs the client that `aRulerView` allowed the user to move `aMarker`.
- [func rulerView(NSRulerView, didRemove: NSRulerMarker)](./nsview/rulerview%28_,didremove%29.md)
  Informs the client that `aRulerView` allowed the user to remove `aMarker`.
- [func rulerView(NSRulerView, handleMouseDownWith: NSEvent)](./nsview/rulerview%28_,handlemousedownwith%29.md)
  Informs the client that the user has pressed the mouse button while the cursor is in the ruler area of `aRulerView`.
- [func rulerView(NSRulerView, locationFor: NSPoint) -> CGFloat](./nsview/rulerview%28_,locationfor%29.md)
- [func rulerView(NSRulerView, pointForLocation: CGFloat) -> NSPoint](./nsview/rulerview%28_,pointforlocation%29.md)
- [func rulerView(NSRulerView, shouldAdd: NSRulerMarker) -> Bool](./nsview/rulerview%28_,shouldadd%29.md)
  Requests permission for `aRulerView` to add `aMarker`, an NSRulerMarker being dragged onto the ruler by the user.
- [func rulerView(NSRulerView, shouldMove: NSRulerMarker) -> Bool](./nsview/rulerview%28_,shouldmove%29.md)
  Requests permission for `aRulerView` to move `aMarker`.
- [func rulerView(NSRulerView, shouldRemove: NSRulerMarker) -> Bool](./nsview/rulerview%28_,shouldremove%29.md)
  Requests permission for `aRulerView` to remove `aMarker`.
- [func rulerView(NSRulerView, willAdd: NSRulerMarker, atLocation: CGFloat) -> CGFloat](./nsview/rulerview%28_,willadd,atlocation%29.md)
  Informs the client that `aRulerView` will add the new NSRulerMarker, `aMarker`.
- [func rulerView(NSRulerView, willMove: NSRulerMarker, toLocation: CGFloat) -> CGFloat](./nsview/rulerview%28_,willmove,tolocation%29.md)
  Informs the client that `aRulerView` will move `aMarker`, an NSRulerMarker already on the ruler view.
- [func rulerView(NSRulerView, willSetClientView: NSView)](./nsview/rulerview%28_,willsetclientview%29.md)
  Informs the client view that `aRulerView` is about to be appropriated by `newClient`.
### Synchronizing with the display’s refresh rate
- [func displayLink(target: Any, selector: Selector) -> CADisplayLink](./nsview/displaylink%28target,selector%29.md)
  Returns a new display link whose callback will be invoked in-sync with the display the view is on.

## See Also

### Configuring the view
- [View Hierarchy](./view-hierarchy.md)
  Manage the subviews, superview, and window of a view and respond to notifications when the view hierarchy changes.
- [View Coordinates](./view-coordinates.md)
  Manage the frame and bounds rectangles that determine the size and position of the view in the view hierarchy.
- [Appearance](./nsview-appearance.md)
  Change the view’s visibility, vibrancy, and focus ring and respond to appearance-related changes.
- [Core Animation Support](./core-animation-support.md)
  Manage the layer object that provides the view’s visual representation and accelerates drawing operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/related-ui)*