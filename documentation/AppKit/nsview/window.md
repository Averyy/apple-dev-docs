# window

**Framework**: AppKit  
**Kind**: property

The view’s window object, if it is installed in a window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
unowned(unsafe) var window: NSWindow? { get }
```

#### Discussion

The value of this property is `nil` if the view is not currently installed in a window.

## See Also

- [var superview: NSView?](nsview/superview.md)
  The view that is the parent of the current view.
- [var subviews: [NSView]](nsview/subviews.md)
  The array of views embedded in the current view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/window)*