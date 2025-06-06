# present(_:animator:)

**Framework**: AppKit  
**Kind**: method

Presents another view controller using a specified, custom animator for presentation and dismissal.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func present(_ viewController: NSViewController, animator: any NSViewControllerPresentationAnimator)
```

#### Discussion

Do not call this method unless you want to use a custom animator. To use one of the standard animators to present another view controller, instead call one of the dedicated presentation methods:

- [`present(_:asPopoverRelativeTo:of:preferredEdge:behavior:)`](nsviewcontroller/present(_:aspopoverrelativeto:of:preferrededge:behavior:).md)
- [`presentAsModalWindow(_:)`](nsviewcontroller/presentasmodalwindow(_:).md)
- [`presentAsSheet(_:)`](nsviewcontroller/presentassheet(_:).md)

Each of these methods calls this method in turn. User interaction is blocked during presentation and dismissal.

## Parameters

- `viewController`: The other view controller to present from the view controller.
- `animator`: The animation delegate to employ for presentation and dismissal of the other view controller. The animator that you specify is retained until the   method is called and the dismissal animation completes.

## See Also

- [func dismiss(NSViewController)](nsviewcontroller/dismiss(_:)-91my5.md)
  Dismisses a presented view controller, using the same animator that presented it.
- [func present(NSViewController, asPopoverRelativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge, behavior: NSPopover.Behavior)](nsviewcontroller/present(_:aspopoverrelativeto:of:preferrededge:behavior:).md)
  Presents another view controller as a popover.
- [func present(NSViewController, asPopoverRelativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge, behavior: NSPopover.Behavior, hasFullSizeContent: Bool)](nsviewcontroller/present(_:aspopoverrelativeto:of:preferrededge:behavior:hasfullsizecontent:).md)
- [func presentAsModalWindow(NSViewController)](nsviewcontroller/presentasmodalwindow(_:).md)
  Presents another view controller as a modal window, also known as an alert.
- [func presentAsSheet(NSViewController)](nsviewcontroller/presentassheet(_:).md)
  Presents another view controller as a sheet.
- [func present(inWidget: NSViewController)](nsviewcontroller/present(inwidget:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/present(_:animator:))*