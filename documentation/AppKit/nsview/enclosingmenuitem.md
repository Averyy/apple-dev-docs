# enclosingMenuItem

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The menu item containing the view or any of its superviews in the view hierarchy.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var enclosingMenuItem: NSMenuItem? { get }
```

```objc
@property (strong, readonly, nullable) NSMenuItem * enclosingMenuItem;
```

## Discussion

The value of this property is `nil` if the view is not in a menu item.

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
- [func isDescendant(of: NSView) -> Bool](./isdescendant%28of%29.md)
  Returns a Boolean value that indicates whether the view is a subview of the specified view.
- [func ancestorShared(with: NSView) -> NSView?](./ancestorshared%28with%29.md)
  Returns the closest ancestor shared by the view and another specified view.
- [var enclosingScrollView: NSScrollView?](./enclosingscrollview.md)
  The nearest ancestor scroll view that contains the current view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/enclosingmenuitem)*