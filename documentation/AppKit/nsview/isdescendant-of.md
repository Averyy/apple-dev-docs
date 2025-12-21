# isDescendant(of:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value that indicates whether the view is a subview of the specified view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func isDescendant(of view: NSView) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the view is a subview, or distant subview, of the specified view.

#### Discussion

The method returns [`true`](https://developer.apple.com/documentation/Swift/true) if the view is either an immediate or distant subview of `aView`.

## Parameters

- `view`: The view to test for subview relationship within the view hierarchy.

## See Also

- [var superview: NSView?](nsview/superview.md)
  The view that is the parent of the current view.
- [var subviews: [NSView]](nsview/subviews.md)
  The array of views embedded in the current view.
- [var window: NSWindow?](nsview/window.md)
  The view’s window object, if it is installed in a window.
- [var opaqueAncestor: NSView?](nsview/opaqueancestor.md)
  The view’s closest opaque ancestor, which might be the view itself.
- [func ancestorShared(with: NSView) -> NSView?](nsview/ancestorshared(with:).md)
  Returns the closest ancestor shared by the view and another specified view.
- [var enclosingMenuItem: NSMenuItem?](nsview/enclosingmenuitem.md)
  The menu item containing the view or any of its superviews in the view hierarchy.
- [var enclosingScrollView: NSScrollView?](nsview/enclosingscrollview.md)
  The nearest ancestor scroll view that contains the current view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/isdescendant(of:))*