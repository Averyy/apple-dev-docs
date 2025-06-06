# ancestorShared(with:)

**Framework**: AppKit  
**Kind**: method

Returns the closest ancestor shared by the view and another specified view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func ancestorShared(with view: NSView) -> NSView?
```

#### Return Value

The closest ancestor or `nil` if there’s no such object. Returns `self` if `aView` is identical to the view.

## Parameters

- `view`: Another view to test for closest shared ancestor with the view.

## See Also

- [var superview: NSView?](nsview/superview.md)
  The view that is the parent of the current view.
- [var subviews: [NSView]](nsview/subviews.md)
  The array of views embedded in the current view.
- [var window: NSWindow?](nsview/window.md)
  The view’s window object, if it is installed in a window.
- [var opaqueAncestor: NSView?](nsview/opaqueancestor.md)
  The view’s closest opaque ancestor, which might be the view itself.
- [func isDescendant(of: NSView) -> Bool](nsview/isdescendant(of:).md)
  Returns a Boolean value that indicates whether the view is a subview of the specified view.
- [var enclosingMenuItem: NSMenuItem?](nsview/enclosingmenuitem.md)
  The menu item containing the view or any of its superviews in the view hierarchy.
- [var enclosingScrollView: NSScrollView?](nsview/enclosingscrollview.md)
  The nearest ancestor scroll view that contains the current view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/ancestorshared(with:))*