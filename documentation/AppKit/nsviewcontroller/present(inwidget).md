# present(inWidget:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use WidgetKit instead. Today View extensions have been deprecated.

## Declaration

```swift
func present(inWidget viewController: NSViewController)
```

```objc
- (void) presentViewControllerInWidget:(NSViewController *) viewController;
```

## See Also

### Presenting Another View Controller’s Content
- [func present(NSViewController, animator: any NSViewControllerPresentationAnimator)](./present%28_,animator%29.md)
  Presents another view controller using a specified, custom animator for presentation and dismissal.
- [func dismiss(NSViewController)](./dismiss%28_%29-91my5.md)
  Dismisses a presented view controller, using the same animator that presented it.
- [func present(NSViewController, asPopoverRelativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge, behavior: NSPopover.Behavior)](./present%28_,aspopoverrelativeto,of,preferrededge,behavior%29.md)
  Presents another view controller as a popover.
- [func present(NSViewController, asPopoverRelativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge, behavior: NSPopover.Behavior, hasFullSizeContent: Bool)](./present%28_,aspopoverrelativeto,of,preferrededge,behavior,hasfullsizecontent%29.md)
- [func presentAsModalWindow(NSViewController)](./presentasmodalwindow%28_%29.md)
  Presents another view controller as a modal window, also known as an alert.
- [func presentAsSheet(NSViewController)](./presentassheet%28_%29.md)
  Presents another view controller as a sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/present(inwidget:))*