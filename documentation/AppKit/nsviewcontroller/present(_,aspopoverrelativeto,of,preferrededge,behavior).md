# present(_:asPopoverRelativeTo:of:preferredEdge:behavior:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Presents another view controller as a popover.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func present(_ viewController: NSViewController, asPopoverRelativeTo positioningRect: NSRect, of positioningView: NSView, preferredEdge: NSRectEdge, behavior: NSPopover.Behavior)
```

```objc
- (void) presentViewController:(NSViewController *) viewController asPopoverRelativeToRect:(NSRect) positioningRect ofView:(NSView *) positioningView preferredEdge:(NSRectEdge) preferredEdge behavior:(NSPopoverBehavior) behavior;
```

## Discussion

This method calls the [`present(_:animator:)`](./present%28_,animator%29.md) method on `self` (the presenting view controller), and passes a popover animator to that method.

The presented view controller is the delegate and the content view controller of the popover. You can use [`NSPopoverDelegate`](../nspopoverdelegate.md) methods to customize the popover.

To dismiss the popover, call the [`dismiss(_:)`](./dismiss%28_%29-91my5.md) method on `self` (the presenting view controller).

## Parameters

- `viewController`: The other view controller to present as a popover.
- `positioningRect`: The content size of the popover.
- `positioningView`: The view relative to which the popover should be positioned. Must not be `nil`, or else the view controller raises an [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md) exception.
- `preferredEdge`: The edge of `positioningView` that the popover should prefer to be anchored to.
- `behavior`: The popover’s closing behavior. See the [`NSPopover.Behavior`](../nspopover/behavior-swift.enum.md) enumeration.

## See Also

### Presenting Another View Controller’s Content
- [func present(NSViewController, animator: any NSViewControllerPresentationAnimator)](./present%28_,animator%29.md)
  Presents another view controller using a specified, custom animator for presentation and dismissal.
- [func dismiss(NSViewController)](./dismiss%28_%29-91my5.md)
  Dismisses a presented view controller, using the same animator that presented it.
- [func present(NSViewController, asPopoverRelativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge, behavior: NSPopover.Behavior, hasFullSizeContent: Bool)](./present%28_,aspopoverrelativeto,of,preferrededge,behavior,hasfullsizecontent%29.md)
- [func presentAsModalWindow(NSViewController)](./presentasmodalwindow%28_%29.md)
  Presents another view controller as a modal window, also known as an alert.
- [func presentAsSheet(NSViewController)](./presentassheet%28_%29.md)
  Presents another view controller as a sheet.
- [func present(inWidget: NSViewController)](./present%28inwidget%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/present(_:aspopoverrelativeto:of:preferrededge:behavior:))*