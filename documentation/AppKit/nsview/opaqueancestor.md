# opaqueAncestor

**Framework**: AppKit  
**Kind**: property

The view’s closest opaque ancestor, which might be the view itself.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
unowned(unsafe) var opaqueAncestor: NSView? { get }
```

## See Also

- [func displayIfNeededIgnoringOpacity()](nsview/displayifneededignoringopacity.md)
  Acts as [`displayIfNeeded()`](nsview/displayifneeded().md), except that this method doesn’t back up to the first opaque ancestor—it simply causes the view and its descendants to execute their drawing code.
- [func displayIgnoringOpacity(NSRect)](nsview/displayignoringopacity(_:).md)
  Displays the view but confines drawing to a specified region and does not back up to the first opaque ancestor—it simply causes the view and its descendants to execute their drawing code.
- [func displayIfNeededIgnoringOpacity(NSRect)](nsview/displayifneededignoringopacity(_:).md)
  Acts as [`displayIfNeeded()`](nsview/displayifneeded().md), but confining drawing to `aRect` and not backing up to the first opaque ancestor—it simply causes the view and its descendants to execute their drawing code.
- [var isOpaque: Bool](nsview/isopaque.md)
  A Boolean value indicating whether the view fills its frame rectangle with opaque content.
- [var superview: NSView?](nsview/superview.md)
  The view that is the parent of the current view.
- [var subviews: [NSView]](nsview/subviews.md)
  The array of views embedded in the current view.
- [var window: NSWindow?](nsview/window.md)
  The view’s window object, if it is installed in a window.
- [func isDescendant(of: NSView) -> Bool](nsview/isdescendant(of:).md)
  Returns a Boolean value that indicates whether the view is a subview of the specified view.
- [func ancestorShared(with: NSView) -> NSView?](nsview/ancestorshared(with:).md)
  Returns the closest ancestor shared by the view and another specified view.
- [var enclosingMenuItem: NSMenuItem?](nsview/enclosingmenuitem.md)
  The menu item containing the view or any of its superviews in the view hierarchy.
- [var enclosingScrollView: NSScrollView?](nsview/enclosingscrollview.md)
  The nearest ancestor scroll view that contains the current view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/opaqueancestor)*