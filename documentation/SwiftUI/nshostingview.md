# NSHostingView

**Framework**: SwiftUI  
**Kind**: class  
**Role**: Class

An AppKit view that hosts a SwiftUI view hierarchy.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
@preconcurrency class NSHostingView<Content> where Content : View
```

#### Overview

You use `NSHostingView` objects to integrate SwiftUI views into your AppKit view hierarchies. A hosting view is an [`NSView`](../AppKit/nsview.md) object that manages a single SwiftUI view, which may itself contain other SwiftUI views. Because it is an [`NSView`](../AppKit/nsview.md) object, you can integrate it into your existing AppKit view hierarchies to implement portions of your UI. For example, you can use a hosting view to implement a custom control.

A hosting view acts as a bridge between your SwiftUI views and your AppKit interface. During layout, the hosting view reports the content size preferences of your SwiftUI views back to the AppKit layout system so that it can size the view appropriately. The hosting view also coordinates event delivery.

## Topics

### Creating a hosting view
- [init(rootView: Content)](./nshostingview/init%28rootview%29.md)
  Creates a hosting view object that wraps the specified SwiftUI view.
- [init?(coder: NSCoder)](./nshostingview/init%28coder%29.md)
  Creates a hosting view object from the contents of the specified archive.
- [func prepareForReuse()](./nshostingview/prepareforreuse%28%29.md)
### Getting the root view
- [var rootView: Content](./nshostingview/rootview.md)
  The root view of the SwiftUI view hierarchy managed by this view controller.
### Configuring the view layout behavior
- [class var requiresConstraintBasedLayout: Bool](./nshostingview/requiresconstraintbasedlayout.md)
- [var userInterfaceLayoutDirection: NSUserInterfaceLayoutDirection](./nshostingview/userinterfacelayoutdirection.md)
- [var isFlipped: Bool](./nshostingview/isflipped.md)
- [var layerContentsRedrawPolicy: NSView.LayerContentsRedrawPolicy](./nshostingview/layercontentsredrawpolicy.md)
- [func updateConstraints()](./nshostingview/updateconstraints%28%29.md)
- [func layout()](./nshostingview/layout%28%29.md)
- [var safeAreaRegions: SafeAreaRegions](./nshostingview/safearearegions.md)
  The safe area regions that this view controller adds to its view.
### Managing keyboard interaction
- [func keyDown(with: NSEvent)](./nshostingview/keydown%28with%29.md)
  Called when the user presses a key on the keyboard while this view is in the responder chain.
- [func keyUp(with: NSEvent)](./nshostingview/keyup%28with%29.md)
  Called when the user releases a key on the keyboard while this view is in the responder chain.
- [func performKeyEquivalent(with: NSEvent) -> Bool](./nshostingview/performkeyequivalent%28with%29.md)
- [func insertText(Any)](./nshostingview/inserttext%28_%29.md)
- [func didChangeValue(forKey: String)](./nshostingview/didchangevalue%28forkey%29.md)
- [func makeTouchBar() -> NSTouchBar?](./nshostingview/maketouchbar%28%29.md)
### Responding to mouse events
- [func mouseDown(with: NSEvent)](./nshostingview/mousedown%28with%29.md)
- [func mouseUp(with: NSEvent)](./nshostingview/mouseup%28with%29.md)
- [func otherMouseDown(with: NSEvent)](./nshostingview/othermousedown%28with%29.md)
- [func otherMouseUp(with: NSEvent)](./nshostingview/othermouseup%28with%29.md)
- [func rightMouseDown(with: NSEvent)](./nshostingview/rightmousedown%28with%29.md)
- [func rightMouseUp(with: NSEvent)](./nshostingview/rightmouseup%28with%29.md)
- [func mouseEntered(with: NSEvent)](./nshostingview/mouseentered%28with%29.md)
- [func mouseExited(with: NSEvent)](./nshostingview/mouseexited%28with%29.md)
- [func mouseDragged(with: NSEvent)](./nshostingview/mousedragged%28with%29.md)
- [func mouseMoved(with: NSEvent)](./nshostingview/mousemoved%28with%29.md)
- [func otherMouseDragged(with: NSEvent)](./nshostingview/othermousedragged%28with%29.md)
- [func rightMouseDragged(with: NSEvent)](./nshostingview/rightmousedragged%28with%29.md)
- [func cursorUpdate(with: NSEvent)](./nshostingview/cursorupdate%28with%29.md)
### Responding to touch events
- [func touchesBegan(with: NSEvent)](./nshostingview/touchesbegan%28with%29.md)
- [func touchesCancelled(with: NSEvent)](./nshostingview/touchescancelled%28with%29.md)
- [func touchesEnded(with: NSEvent)](./nshostingview/touchesended%28with%29.md)
- [func touchesMoved(with: NSEvent)](./nshostingview/touchesmoved%28with%29.md)
### Responding to gestures
- [func magnify(with: NSEvent)](./nshostingview/magnify%28with%29.md)
- [func rotate(with: NSEvent)](./nshostingview/rotate%28with%29.md)
- [func scrollWheel(with: NSEvent)](./nshostingview/scrollwheel%28with%29.md)
### Handling drag and drop
- [func validRequestor(forSendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?](./nshostingview/validrequestor%28forsendtype,returntype%29.md)
### Providing a context menu
- [func menu(for: NSEvent) -> NSMenu?](./nshostingview/menu%28for%29.md)
### Responding to actions
- [func responds(to: Selector!) -> Bool](./nshostingview/responds%28to%29.md)
- [func forwardingTarget(for: Selector!) -> Any?](./nshostingview/forwardingtarget%28for%29.md)
- [func doCommand(by: Selector)](./nshostingview/docommand%28by%29.md)
### Configuring the responder behavior
- [var acceptsFirstResponder: Bool](./nshostingview/acceptsfirstresponder.md)
- [var needsPanelToBecomeKey: Bool](./nshostingview/needspaneltobecomekey.md)
### Managing the view hierarchy
- [func viewWillMove(toWindow: NSWindow?)](./nshostingview/viewwillmove%28towindow%29.md)
- [func viewDidMoveToWindow()](./nshostingview/viewdidmovetowindow%28%29.md)
- [func viewDidChangeBackingProperties()](./nshostingview/viewdidchangebackingproperties%28%29.md)
- [func viewDidChangeEffectiveAppearance()](./nshostingview/viewdidchangeeffectiveappearance%28%29.md)
### Modifying the frame rectangle
- [var intrinsicContentSize: NSSize](./nshostingview/intrinsiccontentsize.md)
- [func setFrameSize(NSSize)](./nshostingview/setframesize%28_%29.md)
- [var firstBaselineOffsetFromTop: CGFloat](./nshostingview/firstbaselineoffsetfromtop.md)
- [var lastBaselineOffsetFromBottom: CGFloat](./nshostingview/lastbaselineoffsetfrombottom.md)
- [var sizingOptions: NSHostingSizingOptions](./nshostingview/sizingoptions.md)
  The options for how the hosting view creates and updates constraints based on the size of its SwiftUI content.
- [var firstTextLineCenter: CGFloat?](./nshostingview/firsttextlinecenter.md)
### Testing for hits
- [func hitTest(CGPoint) -> NSView?](./nshostingview/hittest%28_%29.md)
### Managing accessibility behaviors
- [var accessibilityFocusedUIElement: Any?](./nshostingview/accessibilityfocuseduielement.md)
- [func accessibilityChildren() -> [Any]?](./nshostingview/accessibilitychildren%28%29.md)
- [func accessibilityChildrenInNavigationOrder() -> [any NSAccessibilityElementProtocol]?](./nshostingview/accessibilitychildreninnavigationorder%28%29.md)
- [func accessibilityHitTest(NSPoint) -> Any?](./nshostingview/accessibilityhittest%28_%29.md)
- [func accessibilityRole() -> NSAccessibility.Role?](./nshostingview/accessibilityrole%28%29.md)
- [func accessibilitySubrole() -> NSAccessibility.Subrole?](./nshostingview/accessibilitysubrole%28%29.md)
- [func isAccessibilityElement() -> Bool](./nshostingview/isaccessibilityelement%28%29.md)
### Bridging with SwiftUI
- [var sceneBridgingOptions: NSHostingSceneBridgingOptions](./nshostingview/scenebridgingoptions.md)
  The options for which aspects of the window will be managed by this hosting view.
### Initializers
- [init?(coder: NSCoder, rootView: Content)](./nshostingview/init%28coder,rootview%29.md)
  Creates a hosting view object from an archive and the specified SwiftUI view.
### Instance Properties
- [var clipsToBounds: Bool](./nshostingview/clipstobounds.md)
### Instance Methods
- [func acceptsFirstMouse(for: NSEvent?) -> Bool](./nshostingview/acceptsfirstmouse%28for%29.md)
- [func beginDocument()](./nshostingview/begindocument%28%29.md)
- [func didAddSubview(NSView)](./nshostingview/didaddsubview%28_%29.md)
- [func endDocument()](./nshostingview/enddocument%28%29.md)
- [func observeValue(forKeyPath: String?, of: Any?, change: [NSKeyValueChangeKey : Any]?, context: UnsafeMutableRawPointer?)](./nshostingview/observevalue%28forkeypath,of,change,context%29.md)
- [func shouldDelayWindowOrdering(for: NSEvent) -> Bool](./nshostingview/shoulddelaywindowordering%28for%29.md)
- [func viewDidEndLiveResize()](./nshostingview/viewdidendliveresize%28%29.md)
- [func viewWillStartLiveResize()](./nshostingview/viewwillstartliveresize%28%29.md)
- [func willRemoveSubview(NSView)](./nshostingview/willremovesubview%28_%29.md)

## Relationships

### Inherits From
- [NSView](../AppKit/nsview.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../AppKit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](../AppKit/nsdraggingdestination.md)
- [NSDraggingSource](../AppKit/nsdraggingsource.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [NSUserInterfaceValidations](../AppKit/nsuserinterfacevalidations.md)

## See Also

### Displaying SwiftUI views in AppKit
- [Unifying your app’s animations](./unifying-your-app-s-animations.md)
  Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [class NSHostingController](./nshostingcontroller.md)
  An AppKit view controller that hosts SwiftUI view hierarchy.
- [class NSHostingMenu](./nshostingmenu.md)
  An AppKit menu with menu items that are defined by a SwiftUI View.
- [struct NSHostingSizingOptions](./nshostingsizingoptions.md)
  Options for how hosting views and controllers reflect their content’s size into Auto Layout constraints.
- [class NSHostingSceneRepresentation](./nshostingscenerepresentation.md)
  An AppKit type that hosts and can present SwiftUI scenes
- [struct NSHostingSceneBridgingOptions](./nshostingscenebridgingoptions.md)
  Options for how hosting views and controllers manage aspects of the associated window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingview)*