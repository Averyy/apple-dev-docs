# superview

**Framework**: AppKit  
**Kind**: property

The view that is the parent of the current view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
unowned(unsafe) var superview: NSView? { get }
```

#### Discussion

The superview is the immediate ancestor of the current view. The value of this property is `nil` when the view is not installed in a view hierarchy. To set the value of this property, use the [`addSubview(_:)`](nsview/addsubview(_:).md) method to embed the current view inside another view.

When checking the value of this property iteratively or recursively, be sure to compare the superview object to the content view of the window to avoid proceeding out of the view hierarchy.

## See Also

- [func removeFromSuperview()](nsview/removefromsuperview.md)
  Unlinks the view from its superview and its window, removes it from the responder chain, and invalidates its cursor rectangles.
- [var subviews: [NSView]](nsview/subviews.md)
  The array of views embedded in the current view.
- [var window: NSWindow?](nsview/window.md)
  The view’s window object, if it is installed in a window.
- [var opaqueAncestor: NSView?](nsview/opaqueancestor.md)
  The view’s closest opaque ancestor, which might be the view itself.
- [func isDescendant(of: NSView) -> Bool](nsview/isdescendant(of:).md)
  Returns a Boolean value that indicates whether the view is a subview of the specified view.
- [func ancestorShared(with: NSView) -> NSView?](nsview/ancestorshared(with:).md)
  Returns the closest ancestor shared by the view and another specified view.
- [var enclosingMenuItem: NSMenuItem?](nsview/enclosingmenuitem.md)
  The menu item containing the view or any of its superviews in the view hierarchy.
- [var enclosingScrollView: NSScrollView?](nsview/enclosingscrollview.md)
  The nearest ancestor scroll view that contains the current view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/superview)*