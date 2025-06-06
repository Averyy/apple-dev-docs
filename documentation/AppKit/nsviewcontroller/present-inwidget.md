# present(inWidget:)

**Framework**: AppKit  
**Kind**: method

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func present(inWidget viewController: NSViewController)
```

## See Also

- [func present(NSViewController, animator: any NSViewControllerPresentationAnimator)](nsviewcontroller/present(_:animator:).md)
  Presents another view controller using a specified, custom animator for presentation and dismissal.
- [func dismiss(NSViewController)](nsviewcontroller/dismiss(_:)-91my5.md)
  Dismisses a presented view controller, using the same animator that presented it.
- [func present(NSViewController, asPopoverRelativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge, behavior: NSPopover.Behavior)](nsviewcontroller/present(_:aspopoverrelativeto:of:preferrededge:behavior:).md)
  Presents another view controller as a popover.
- [func present(NSViewController, asPopoverRelativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge, behavior: NSPopover.Behavior, hasFullSizeContent: Bool)](nsviewcontroller/present(_:aspopoverrelativeto:of:preferrededge:behavior:hasfullsizecontent:).md)
- [func presentAsModalWindow(NSViewController)](nsviewcontroller/presentasmodalwindow(_:).md)
  Presents another view controller as a modal window, also known as an alert.
- [func presentAsSheet(NSViewController)](nsviewcontroller/presentassheet(_:).md)
  Presents another view controller as a sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/present(inwidget:))*