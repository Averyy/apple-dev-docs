# presentAsModalWindow(_:)

**Framework**: AppKit  
**Kind**: method

Presents another view controller as a modal window, also known as an alert.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func presentAsModalWindow(_ viewController: NSViewController)
```

#### Discussion

This method calls the [`present(_:animator:)`](nsviewcontroller/present(_:animator:).md) method on `self` (the presenting view controller), and passes a modal window animator to that method.

The presented view controller is the delegate and the content view controller of its window. You can use [`NSWindowDelegate`](nswindowdelegate.md) methods to prevent the closing of the modal window, if needed.

To dismiss the modal window, call the [`dismiss(_:)`](nsviewcontroller/dismiss(_:)-91my5.md) method on `self` (the presenting view controller).

## Parameters

- `viewController`: The other view controller to present as a modal window.

## See Also

- [func present(NSViewController, animator: any NSViewControllerPresentationAnimator)](nsviewcontroller/present(_:animator:).md)
  Presents another view controller using a specified, custom animator for presentation and dismissal.
- [func dismiss(NSViewController)](nsviewcontroller/dismiss(_:)-91my5.md)
  Dismisses a presented view controller, using the same animator that presented it.
- [func present(NSViewController, asPopoverRelativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge, behavior: NSPopover.Behavior)](nsviewcontroller/present(_:aspopoverrelativeto:of:preferrededge:behavior:).md)
  Presents another view controller as a popover.
- [func present(NSViewController, asPopoverRelativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge, behavior: NSPopover.Behavior, hasFullSizeContent: Bool)](nsviewcontroller/present(_:aspopoverrelativeto:of:preferrededge:behavior:hasfullsizecontent:).md)
- [func presentAsSheet(NSViewController)](nsviewcontroller/presentassheet(_:).md)
  Presents another view controller as a sheet.
- [func present(inWidget: NSViewController)](nsviewcontroller/present(inwidget:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/presentasmodalwindow(_:))*