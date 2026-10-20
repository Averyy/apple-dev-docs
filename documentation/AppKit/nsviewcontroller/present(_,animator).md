# present(_:animator:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Presents another view controller using a specified, custom animator for presentation and dismissal.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func present(_ viewController: NSViewController, animator: any NSViewControllerPresentationAnimator)
```

```objc
- (void) presentViewController:(NSViewController *) viewController animator:(id<NSViewControllerPresentationAnimator>) animator;
```

#### Discussion

Do not call this method unless you want to use a custom animator. To use one of the standard animators to present another view controller, instead call one of the dedicated presentation methods:

- [`present(_:asPopoverRelativeTo:of:preferredEdge:behavior:)`](./present%28_,aspopoverrelativeto,of,preferrededge,behavior%29.md)
- [`presentAsModalWindow(_:)`](./presentasmodalwindow%28_%29.md)
- [`presentAsSheet(_:)`](./presentassheet%28_%29.md)

Each of these methods calls this method in turn. User interaction is blocked during presentation and dismissal.

## Parameters

- `viewController`: The other view controller to present from the view controller.

  > **Note**:  The view controller you provide in this parameter must not already be visible elsewhere, or else this method raises an exception.
  >
  > The view in the presented view controller must have a window, or else this method raises an exception.
- `animator`: The animation delegate to employ for presentation and dismissal of the other view controller. The animator that you specify is retained until the [`dismiss(_:)`](./dismiss%28_%29-91my5.md) method is called and the dismissal animation completes.

  > **Note**:  This parameter’s value must not be `nil`, or else this method raises an exception.

## See Also

### Presenting Another View Controller’s Content
- [func dismiss(NSViewController)](./dismiss%28_%29-91my5.md)
  Dismisses a presented view controller, using the same animator that presented it.
- [func present(NSViewController, asPopoverRelativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge, behavior: NSPopover.Behavior)](./present%28_,aspopoverrelativeto,of,preferrededge,behavior%29.md)
  Presents another view controller as a popover.
- [func present(NSViewController, asPopoverRelativeTo: NSRect, of: NSView, preferredEdge: NSRectEdge, behavior: NSPopover.Behavior, hasFullSizeContent: Bool)](./present%28_,aspopoverrelativeto,of,preferrededge,behavior,hasfullsizecontent%29.md)
- [func presentAsModalWindow(NSViewController)](./presentasmodalwindow%28_%29.md)
  Presents another view controller as a modal window, also known as an alert.
- [func presentAsSheet(NSViewController)](./presentassheet%28_%29.md)
  Presents another view controller as a sheet.
- [func present(inWidget: NSViewController)](./present%28inwidget%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewcontroller/present(_:animator:))*