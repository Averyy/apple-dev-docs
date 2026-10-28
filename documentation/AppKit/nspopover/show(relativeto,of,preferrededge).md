# show(relativeTo:of:preferredEdge:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Shows the popover anchored to the specified view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func show(relativeTo positioningRect: NSRect, of positioningView: NSView, preferredEdge: NSRectEdge)
```

```objc
- (void) showRelativeToRect:(NSRect) positioningRect ofView:(NSView *) positioningView preferredEdge:(NSRectEdge) preferredEdge;
```

## Discussion

This method raises [`internalInconsistencyException`](../../Foundation/nsexceptionname/internalinconsistencyexception.md) if [`contentViewController`](./contentviewcontroller.md) or the view controller’s view is `nil`. If the popover is already being shown, this method updates the anchored view, rectangle, and preferred edge. If the positioning view is not visible, this method does nothing.

## Parameters

- `positioningRect`: The rectangle within `positioningView` relative to which the popover should be positioned. Normally set to the bounds of `positioningView`. May be an empty rectangle, which will default to the bounds of `positioningView`.
- `positioningView`: The view relative to which the popover should be positioned. Causes the method to raise  [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md) if `nil`.
- `preferredEdge`: The edge of `positioningView` the popover should prefer to be anchored to.

## See Also

### Managing a Popover’s Position and Size
- [var behavior: NSPopover.Behavior](./behavior-swift.property.md)
  Specifies the behavior of the popover.
- [var positioningRect: NSRect](./positioningrect.md)
  The rectangle within the positioning view relative to which the popover should be positioned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopover/show(relativeto:of:preferrededge:))*