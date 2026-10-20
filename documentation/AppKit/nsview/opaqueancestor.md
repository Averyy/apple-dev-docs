# opaqueAncestor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The view’s closest opaque ancestor, which might be the view itself.

**Availability**:
- macOS

## Declaration

```swift
unowned(unsafe) var opaqueAncestor: NSView? { get }
```

```objc
@property (assign, readonly, nullable) NSView * opaqueAncestor;
```

## See Also

### Related Documentation
- [func displayIfNeededIgnoringOpacity()](./displayifneededignoringopacity%28%29.md)
  Acts as [`displayIfNeeded()`](./displayifneeded%28%29.md), except that this method doesn’t back up to the first opaque ancestor—it simply causes the view and its descendants to execute their drawing code.
- [func displayIgnoringOpacity(NSRect)](./displayignoringopacity%28_%29.md)
  Displays the view but confines drawing to a specified region and does not back up to the first opaque ancestor—it simply causes the view and its descendants to execute their drawing code.
- [func displayIfNeededIgnoringOpacity(NSRect)](./displayifneededignoringopacity%28_%29.md)
  Acts as [`displayIfNeeded()`](./displayifneeded%28%29.md), but confining drawing to `aRect` and not backing up to the first opaque ancestor—it simply causes the view and its descendants to execute their drawing code.
- [var isOpaque: Bool](./isopaque.md)
  A Boolean value indicating whether the view fills its frame rectangle with opaque content.
### Getting the Related Objects
- [var superview: NSView?](./superview.md)
  The view that is the parent of the current view.
- [var subviews: [NSView]](./subviews.md)
  The array of views embedded in the current view.
- [var window: NSWindow?](./window.md)
  The view’s window object, if it is installed in a window.
- [func isDescendant(of: NSView) -> Bool](./isdescendant%28of%29.md)
  Returns a Boolean value that indicates whether the view is a subview of the specified view.
- [func ancestorShared(with: NSView) -> NSView?](./ancestorshared%28with%29.md)
  Returns the closest ancestor shared by the view and another specified view.
- [var enclosingMenuItem: NSMenuItem?](./enclosingmenuitem.md)
  The menu item containing the view or any of its superviews in the view hierarchy.
- [var enclosingScrollView: NSScrollView?](./enclosingscrollview.md)
  The nearest ancestor scroll view that contains the current view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/opaqueancestor)*