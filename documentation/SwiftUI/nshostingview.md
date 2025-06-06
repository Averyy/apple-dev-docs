# NSHostingView

**Framework**: SwiftUI  
**Kind**: class

An AppKit view that hosts a SwiftUI view hierarchy.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency class NSHostingView<Content> where Content : View
```

#### Overview

You use `NSHostingView` objects to integrate SwiftUI views into your AppKit view hierarchies. A hosting view is an [`NSView`](https://developer.apple.com/documentation/AppKit/NSView) object that manages a single SwiftUI view, which may itself contain other SwiftUI views. Because it is an [`NSView`](https://developer.apple.com/documentation/AppKit/NSView) object, you can integrate it into your existing AppKit view hierarchies to implement portions of your UI. For example, you can use a hosting view to implement a custom control.

A hosting view acts as a bridge between your SwiftUI views and your AppKit interface. During layout, the hosting view reports the content size preferences of your SwiftUI views back to the AppKit layout system so that it can size the view appropriately. The hosting view also coordinates event delivery.

## Topics

### Creating a hosting view
- [init(rootView: Content)](nshostingview/init(rootview:).md)
  Creates a hosting view object that wraps the specified SwiftUI view.
- [init?(coder: NSCoder)](nshostingview/init(coder:).md)
  Creates a hosting view object from the contents of the specified archive.
- [func prepareForReuse()](nshostingview/prepareforreuse.md)
### Getting the root view
- [var rootView: Content](nshostingview/rootview.md)
  The root view of the SwiftUI view hierarchy managed by this view controller.
### Configuring the view layout behavior
- [class var requiresConstraintBasedLayout: Bool](nshostingview/requiresconstraintbasedlayout.md)
- [var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection](nshostingview/userinterfacelayoutdirection.md)
- [var isFlipped: Bool](nshostingview/isflipped.md)
- [var layerContentsRedrawPolicy: NSView.LayerContentsRedrawPolicy](nshostingview/layercontentsredrawpolicy.md)
- [func updateConstraints()](nshostingview/updateconstraints.md)
- [func layout()](nshostingview/layout.md)
- [var safeAreaRegions: SafeAreaRegions](nshostingview/safearearegions.md)
  The safe area regions that this view controller adds to its view.
### Managing keyboard interaction
- [func keyDown(with: NSEvent)](nshostingview/keydown(with:).md)
  Called when the user presses a key on the keyboard while this view is in the responder chain.
- [func keyUp(with: NSEvent)](nshostingview/keyup(with:).md)
  Called when the user releases a key on the keyboard while this view is in the responder chain.
- [func performKeyEquivalent(with: NSEvent) -> Bool](nshostingview/performkeyequivalent(with:).md)
- [func insertText(Any)](nshostingview/inserttext(_:).md)
- [func didChangeValue(forKey: String)](nshostingview/didchangevalue(forkey:).md)
- [func makeTouchBar() -> NSTouchBar?](nshostingview/maketouchbar.md)
### Responding to mouse events
- [func mouseDown(with: NSEvent)](nshostingview/mousedown(with:).md)
- [func mouseUp(with: NSEvent)](nshostingview/mouseup(with:).md)
- [func otherMouseDown(with: NSEvent)](nshostingview/othermousedown(with:).md)
- [func otherMouseUp(with: NSEvent)](nshostingview/othermouseup(with:).md)
- [func rightMouseDown(with: NSEvent)](nshostingview/rightmousedown(with:).md)
- [func rightMouseUp(with: NSEvent)](nshostingview/rightmouseup(with:).md)
- [func mouseEntered(with: NSEvent)](nshostingview/mouseentered(with:).md)
- [func mouseExited(with: NSEvent)](nshostingview/mouseexited(with:).md)
- [func mouseDragged(with: NSEvent)](nshostingview/mousedragged(with:).md)
- [func mouseMoved(with: NSEvent)](nshostingview/mousemoved(with:).md)
- [func otherMouseDragged(with: NSEvent)](nshostingview/othermousedragged(with:).md)
- [func rightMouseDragged(with: NSEvent)](nshostingview/rightmousedragged(with:).md)
- [func cursorUpdate(with: NSEvent)](nshostingview/cursorupdate(with:).md)
### Responding to touch events
- [func touchesBegan(with: NSEvent)](nshostingview/touchesbegan(with:).md)
- [func touchesCancelled(with: NSEvent)](nshostingview/touchescancelled(with:).md)
- [func touchesEnded(with: NSEvent)](nshostingview/touchesended(with:).md)
- [func touchesMoved(with: NSEvent)](nshostingview/touchesmoved(with:).md)
### Responding to gestures
- [func magnify(with: NSEvent)](nshostingview/magnify(with:).md)
- [func rotate(with: NSEvent)](nshostingview/rotate(with:).md)
- [func scrollWheel(with: NSEvent)](nshostingview/scrollwheel(with:).md)
### Handling drag and drop
- [func validRequestor(forSendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?](nshostingview/validrequestor(forsendtype:returntype:).md)
### Providing a context menu
- [func menu(for: NSEvent) -> NSMenu?](nshostingview/menu(for:).md)
### Responding to actions
- [func responds(to: Selector!) -> Bool](nshostingview/responds(to:).md)
- [func forwardingTarget(for: Selector!) -> Any?](nshostingview/forwardingtarget(for:).md)
- [func doCommand(by: Selector)](nshostingview/docommand(by:).md)
### Configuring the responder behavior
- [var acceptsFirstResponder: Bool](nshostingview/acceptsfirstresponder.md)
- [var needsPanelToBecomeKey: Bool](nshostingview/needspaneltobecomekey.md)
### Managing the view hierarchy
- [func viewWillMove(toWindow: NSWindow?)](nshostingview/viewwillmove(towindow:).md)
- [func viewDidMoveToWindow()](nshostingview/viewdidmovetowindow.md)
- [func viewDidChangeBackingProperties()](nshostingview/viewdidchangebackingproperties.md)
- [func viewDidChangeEffectiveAppearance()](nshostingview/viewdidchangeeffectiveappearance.md)
### Modifying the frame rectangle
- [var intrinsicContentSize: NSSize](nshostingview/intrinsiccontentsize.md)
- [func setFrameSize(NSSize)](nshostingview/setframesize(_:).md)
- [var firstBaselineOffsetFromTop: CGFloat](nshostingview/firstbaselineoffsetfromtop.md)
- [var lastBaselineOffsetFromBottom: CGFloat](nshostingview/lastbaselineoffsetfrombottom.md)
- [var sizingOptions: NSHostingSizingOptions](nshostingview/sizingoptions.md)
  The options for how the hosting view creates and updates constraints based on the size of its SwiftUI content.
- [var firstTextLineCenter: CGFloat?](nshostingview/firsttextlinecenter.md)
### Testing for hits
- [func hitTest(NSPoint) -> NSView?](nshostingview/hittest(_:).md)
### Managing accessibility behaviors
- [var accessibilityFocusedUIElement: Any?](nshostingview/accessibilityfocuseduielement.md)
- [func accessibilityChildren() -> [Any]?](nshostingview/accessibilitychildren.md)
- [func accessibilityChildrenInNavigationOrder() -> [any NSAccessibilityElementProtocol]?](nshostingview/accessibilitychildreninnavigationorder.md)
- [func accessibilityHitTest(NSPoint) -> Any?](nshostingview/accessibilityhittest(_:).md)
- [func accessibilityRole() -> NSAccessibility.Role?](nshostingview/accessibilityrole.md)
- [func accessibilitySubrole() -> NSAccessibility.Subrole?](nshostingview/accessibilitysubrole.md)
- [func isAccessibilityElement() -> Bool](nshostingview/isaccessibilityelement.md)
### Bridging with SwiftUI
- [var sceneBridgingOptions: NSHostingSceneBridgingOptions](nshostingview/scenebridgingoptions.md)
  The options for which aspects of the window will be managed by this hosting view.
### Initializers
- [init?(coder: NSCoder, rootView: Content)](nshostingview/init(coder:rootview:).md)
  Creates a hosting view object from an archive and the specified SwiftUI view.
### Instance Properties
- [var clipsToBounds: Bool](nshostingview/clipstobounds.md)
### Instance Methods
- [func acceptsFirstMouse(for: NSEvent?) -> Bool](nshostingview/acceptsfirstmouse(for:).md)
- [func didAddSubview(NSView)](nshostingview/didaddsubview(_:).md)
- [func observeValue(forKeyPath: String?, of: Any?, change: [NSKeyValueChangeKey : Any]?, context: UnsafeMutableRawPointer?)](nshostingview/observevalue(forkeypath:of:change:context:).md)
- [func shouldDelayWindowOrdering(for: NSEvent) -> Bool](nshostingview/shoulddelaywindowordering(for:).md)
- [func showContextMenuForSelection(Any?)](nshostingview/showcontextmenuforselection(_:).md)
- [func willRemoveSubview(NSView)](nshostingview/willremovesubview(_:).md)

## Relationships

### Inherits From
- [NSView](../AppKit/NSView.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSDraggingSource](../AppKit/NSDraggingSource.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [NSUserInterfaceValidations](../AppKit/NSUserInterfaceValidations.md)

## See Also

- [Unifying your app’s animations](unifying-your-app-s-animations.md)
  Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [class NSHostingController](nshostingcontroller.md)
  An AppKit view controller that hosts SwiftUI view hierarchy.
- [class NSHostingMenu](nshostingmenu.md)
  An AppKit menu with menu items that are defined by a SwiftUI View.
- [struct NSHostingSizingOptions](nshostingsizingoptions.md)
  Options for how hosting views and controllers reflect their content’s size into Auto Layout constraints.
- [struct NSHostingSceneBridgingOptions](nshostingscenebridgingoptions.md)
  Options for how hosting views and controllers manage aspects of the associated window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingview)*