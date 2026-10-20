# present(_:asPopoverRelativeTo:of:preferredEdge:behavior:hasFullSizeContent:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 14.0+

## Declaration

```swift
func present(_ viewController: NSViewController, asPopoverRelativeTo positioningRect: NSRect, of positioningView: NSView, preferredEdge: NSRectEdge, behavior: NSPopover.Behavior, hasFullSizeContent: Bool)
```

```objc
- (void) presentViewController:(NSViewController *) viewController asPopoverRelativeToRect:(NSRect) positioningRect ofView:(NSView *) positioningView preferredEdge:(NSRectEdge) preferredEdge behavior:(NSPopoverBehavior) behavior hasFullSizeContent:(BOOL) hasFullSizeContent;
```

## See Also

### Presenting Another View Controller’s Content
- [func present(NSViewController, animator: any NSViewControllerPresentationAnimator)](./present%28_,animator%29.md)
  Presents another view controller using a specified, custom animator for presentation and dismissal.
- [func dismiss(NSViewController)](./dismiss%28_%29-91my5.md)
  Dismisses a presented view controller, using the same animator that presented it.
- [func present(NSViewController, asPopoverRelativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge, behavior: NSPopover.Behavior)](./present%28_,aspopoverrelativeto,of,preferrededge,behavior%29.md)
  Presents another view controller as a popover.
- [func presentAsModalWindow(NSViewController)](./presentasmodalwindow%28_%29.md)
  Presents another view controller as a modal window, also known as an alert.
- [func presentAsSheet(NSViewController)](./presentassheet%28_%29.md)
  Presents another view controller as a sheet.
- [func present(inWidget: NSViewController)](./present%28inwidget%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/present(_:aspopoverrelativeto:of:preferrededge:behavior:hasfullsizecontent:))*