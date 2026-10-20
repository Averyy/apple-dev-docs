# isDescendant(of:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the view is a subview of the specified view.

**Availability**:
- macOS

## Declaration

```swift
func isDescendant(of view: NSView) -> Bool
```

```objc
- (BOOL) isDescendantOf:(NSView *) view;
```

#### Return Value

[`true`](../../Swift/true.md) if the view is a subview, or distant subview, of the specified view.

#### Discussion

The method returns [`true`](../../Swift/true.md) if the view is either an immediate or distant subview of `aView`.

## Parameters

- `view`: The view to test for subview relationship within the view hierarchy.

## See Also

### Getting the Related Objects
- [var superview: NSView?](./superview.md)
  The view that is the parent of the current view.
- [var subviews: [NSView]](./subviews.md)
  The array of views embedded in the current view.
- [var window: NSWindow?](./window.md)
  The view’s window object, if it is installed in a window.
- [var opaqueAncestor: NSView?](./opaqueancestor.md)
  The view’s closest opaque ancestor, which might be the view itself.
- [func ancestorShared(with: NSView) -> NSView?](./ancestorshared%28with%29.md)
  Returns the closest ancestor shared by the view and another specified view.
- [var enclosingMenuItem: NSMenuItem?](./enclosingmenuitem.md)
  The menu item containing the view or any of its superviews in the view hierarchy.
- [var enclosingScrollView: NSScrollView?](./enclosingscrollview.md)
  The nearest ancestor scroll view that contains the current view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/isdescendant(of:))*