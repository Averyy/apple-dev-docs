# present(_:asPopoverRelativeTo:of:preferredEdge:behavior:)

**Framework**: AppKit  
**Kind**: method

Presents another view controller as a popover.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func present(_ viewController: NSViewController, asPopoverRelativeTo positioningRect: NSRect, of positioningView: NSView, preferredEdge: NSRectEdge, behavior: NSPopover.Behavior)
```

#### Discussion

This method calls the [`present(_:animator:)`](nsviewcontroller/present(_:animator:).md) method on `self` (the presenting view controller), and passes a popover animator to that method.

The presented view controller is the delegate and the content view controller of the popover. You can use [`NSPopoverDelegate`](nspopoverdelegate.md) methods to customize the popover.

To dismiss the popover, call the [`dismiss(_:)`](nsviewcontroller/dismiss(_:)-91my5.md) method on `self` (the presenting view controller).

## Parameters

- `viewController`: The other view controller to present as a popover.
- `positioningRect`: The content size of the popover.
- `positioningView`: The view relative to which the popover should be positioned. Must not be  , or else the view controller raises an   exception.
- `preferredEdge`: The edge of   that the popover should prefer to be anchored to.
- `behavior`: The popover’s closing behavior. See the   enumeration.

## See Also

- [func present(NSViewController, animator: any NSViewControllerPresentationAnimator)](nsviewcontroller/present(_:animator:).md)
  Presents another view controller using a specified, custom animator for presentation and dismissal.
- [func dismiss(NSViewController)](nsviewcontroller/dismiss(_:)-91my5.md)
  Dismisses a presented view controller, using the same animator that presented it.
- [func present(NSViewController, asPopoverRelativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge, behavior: NSPopover.Behavior, hasFullSizeContent: Bool)](nsviewcontroller/present(_:aspopoverrelativeto:of:preferrededge:behavior:hasfullsizecontent:).md)
- [func presentAsModalWindow(NSViewController)](nsviewcontroller/presentasmodalwindow(_:).md)
  Presents another view controller as a modal window, also known as an alert.
- [func presentAsSheet(NSViewController)](nsviewcontroller/presentassheet(_:).md)
  Presents another view controller as a sheet.
- [func present(inWidget: NSViewController)](nsviewcontroller/present(inwidget:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/present(_:aspopoverrelativeto:of:preferrededge:behavior:))*