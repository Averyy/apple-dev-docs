# dismiss(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Dismisses a presented view controller, using the same animator that presented it.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func dismiss(_ viewController: NSViewController)
```

```objc
- (void) dismissViewController:(NSViewController *) viewController;
```

#### Discussion

In macOS, this is the universal way to dismiss a view controller, no matter how it was presented.

## Parameters

- `viewController`: The presented view controller that you are dismissing.

## See Also

### Presenting Another View Controller’s Content
- [func present(NSViewController, animator: any NSViewControllerPresentationAnimator)](./present%28_,animator%29.md)
  Presents another view controller using a specified, custom animator for presentation and dismissal.
- [func present(NSViewController, asPopoverRelativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge, behavior: NSPopover.Behavior)](./present%28_,aspopoverrelativeto,of,preferrededge,behavior%29.md)
  Presents another view controller as a popover.
- [func present(NSViewController, asPopoverRelativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge, behavior: NSPopover.Behavior, hasFullSizeContent: Bool)](./present%28_,aspopoverrelativeto,of,preferrededge,behavior,hasfullsizecontent%29.md)
- [func presentAsModalWindow(NSViewController)](./presentasmodalwindow%28_%29.md)
  Presents another view controller as a modal window, also known as an alert.
- [func presentAsSheet(NSViewController)](./presentassheet%28_%29.md)
  Presents another view controller as a sheet.
- [func present(inWidget: NSViewController)](./present%28inwidget%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/dismiss(_:)-91my5)*