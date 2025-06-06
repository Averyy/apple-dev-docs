# clipsToBounds

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the view, and its subviews, confine their drawing areas to the bounds of the view.

**Availability**:
- macOS 10.9+

## Declaration

```swift
@MainActor
var clipsToBounds: Bool { get set }
```

#### Discussion

Setting this value to [`true`](https://developer.apple.com/documentation/swift/true) causes the view, and its subviews, to clip themselves to the bounds of the view. Setting it to [`false`](https://developer.apple.com/documentation/swift/false) prevents views and subviews whose frames extend beyond the visible bounds of the view from clipping themselves. A value of [`false`](https://developer.apple.com/documentation/swift/false) has no effect on [`hitTest(_:)`](nsview/hittest(_:).md) but does affect [`visibleRect`](nsview/visiblerect.md), as well as the area drawn inside [`draw(_:)`](nsview/draw(_:).md).

By default this value is [`false`](https://developer.apple.com/documentation/swift/false). In macOS 13 and earlier, the default value is [`true`](https://developer.apple.com/documentation/swift/true).

Because of this change in default value, views built on macOS 13 and earlier may require layout adjustments such as the following on newer versions of macOS:

- Showing or hiding UI elements by setting a parent’s frame size to zero. To hide a view hierarchy by shrinking the parent view, or positioning a child view outside a parent’s bounds, set the [`clipsToBounds`](nsview/clipstobounds.md) property of the parent view to [`true`](https://developer.apple.com/documentation/swift/true). Alternatively, set [`isHidden`](nsview/ishidden.md) to [`true`](https://developer.apple.com/documentation/swift/true) on the parent view instead.
- Filling the `dirtyRect` of a view inside [`draw(_:)`](nsview/draw(_:).md). It’s a common practice to set the background color on a view by calling [`setFill()`](nscolor/setfill().md) on a background color and then calling [`fill(using:)`](https://developer.apple.com/documentation/CoreFoundation/CGRect/fill(using:)) on the `dirtyRect` parameter passed into an override of [`draw(_:)`](nsview/draw(_:).md). Because the `dirtyRect` now extends outside your view’s bounds, call [`fill(using:)`](https://developer.apple.com/documentation/CoreFoundation/CGRect/fill(using:)) on the view’s bounds instead of the `dirtyRect`, or set the view’s [`clipsToBounds`](nsview/clipstobounds.md) to [`true`](https://developer.apple.com/documentation/swift/true).
- Differentiating a view’s bounds from its `dirtyRect`. Use the `dirtyRect` parameter passed to [`draw(_:)`](nsview/draw(_:).md) to determine what to draw, not where to draw it. Use the view’s [`bounds`](nsview/bounds.md) to determine the layout of what your view draws.

## See Also

- [func updateLayer()](nsview/updatelayer.md)
  Updates the view’s content by modifying its underlying layer.
- [func draw(NSRect)](nsview/draw(_:).md)
  Overridden by subclasses to draw the view’s image within the specified rectangle.
- [var canDrawConcurrently: Bool](nsview/candrawconcurrently.md)
  A Boolean value indicating whether the view can draw its contents on a background thread.
- [var visibleRect: NSRect](nsview/visiblerect.md)
  The portion of the view that isn’t clipped by its superviews.
- [func getRectsBeingDrawn(UnsafeMutablePointer<UnsafePointer<NSRect>?>?, count: UnsafeMutablePointer<Int>?)](nsview/getrectsbeingdrawn(_:count:).md)
  Returns by indirection a list of nonoverlapping rectangles that define the area the view is being asked to draw in [`draw(_:)`](nsview/draw(_:).md).
- [func needsToDraw(NSRect) -> Bool](nsview/needstodraw(_:).md)
  Returns a Boolean value indicating whether the specified rectangle intersects any part of the area that the view is being asked to draw.
- [var wantsDefaultClipping: Bool](nsview/wantsdefaultclipping.md)
  A Boolean value indicating whether AppKit’s default clipping behavior is in effect.
- [func bitmapImageRepForCachingDisplay(in: NSRect) -> NSBitmapImageRep?](nsview/bitmapimagerepforcachingdisplay(in:).md)
  Returns a bitmap-representation object suitable for caching the specified portion of the view.
- [func cacheDisplay(in: NSRect, to: NSBitmapImageRep)](nsview/cachedisplay(in:to:).md)
  Draws the specified area of the view, and its descendants, into a provided bitmap-representation object.
- [enum NSBorderType](nsbordertype.md)
  These constants specify the type of a view’s border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/clipstobounds)*