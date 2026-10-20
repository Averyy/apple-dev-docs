# presentAsModalWindow(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Presents another view controller as a modal window, also known as an alert.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func presentAsModalWindow(_ viewController: NSViewController)
```

```objc
- (void) presentViewControllerAsModalWindow:(NSViewController *) viewController;
```

#### Discussion

This method calls the [`present(_:animator:)`](./present%28_,animator%29.md) method on `self` (the presenting view controller), and passes a modal window animator to that method.

The presented view controller is the delegate and the content view controller of its window. You can use [`NSWindowDelegate`](../nswindowdelegate.md) methods to prevent the closing of the modal window, if needed.

To dismiss the modal window, call the [`dismiss(_:)`](./dismiss%28_%29-91my5.md) method on `self` (the presenting view controller).

## Parameters

- `viewController`: The other view controller to present as a modal window.

## See Also

### Presenting Another View Controller’s Content
- [func present(NSViewController, animator: any NSViewControllerPresentationAnimator)](./present%28_,animator%29.md)
  Presents another view controller using a specified, custom animator for presentation and dismissal.
- [func dismiss(NSViewController)](./dismiss%28_%29-91my5.md)
  Dismisses a presented view controller, using the same animator that presented it.
- [func present(NSViewController, asPopoverRelativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge, behavior: NSPopover.Behavior)](./present%28_,aspopoverrelativeto,of,preferrededge,behavior%29.md)
  Presents another view controller as a popover.
- [func present(NSViewController, asPopoverRelativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge, behavior: NSPopover.Behavior, hasFullSizeContent: Bool)](./present%28_,aspopoverrelativeto,of,preferrededge,behavior,hasfullsizecontent%29.md)
- [func presentAsSheet(NSViewController)](./presentassheet%28_%29.md)
  Presents another view controller as a sheet.
- [func present(inWidget: NSViewController)](./present%28inwidget%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/presentasmodalwindow(_:))*