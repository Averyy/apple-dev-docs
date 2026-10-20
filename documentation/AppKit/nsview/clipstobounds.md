# clipsToBounds

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the view, and its subviews, confine their drawing areas to the bounds of the view.

**Availability**:
- macOS 10.9+

## Declaration

```swift
var clipsToBounds: Bool { get set }
```

```objc
@property BOOL clipsToBounds;
```

#### Discussion

Setting this value to [`true`](../../Swift/true.md) causes the view, and its subviews, to clip themselves to the bounds of the view. Setting it to [`false`](../../Swift/false.md) prevents views and subviews whose frames extend beyond the visible bounds of the view from clipping themselves. A value of [`false`](../../Swift/false.md) has no effect on [`hitTest(_:)`](./hittest%28_%29.md) but does affect [`visibleRect`](./visiblerect.md), as well as the area drawn inside [`draw(_:)`](./draw%28_%29.md).

By default this value is [`false`](../../Swift/false.md). In macOS 13 and earlier, the default value is [`true`](../../Swift/true.md).

Because of this change in default value, views built on macOS 13 and earlier may require layout adjustments such as the following on newer versions of macOS:

- Showing or hiding UI elements by setting a parent’s frame size to zero. To hide a view hierarchy by shrinking the parent view, or positioning a child view outside a parent’s bounds, set the [`clipsToBounds`](./clipstobounds.md) property of the parent view to [`true`](../../Swift/true.md). Alternatively, set [`isHidden`](./ishidden.md) to [`true`](../../Swift/true.md) on the parent view instead.
- Filling the `dirtyRect` of a view inside [`draw(_:)`](./draw%28_%29.md). It’s a common practice to set the background color on a view by calling [`setFill()`](../nscolor/setfill%28%29.md) on a background color and then calling [`fill(using:)`](../../CoreFoundation/cgrect/fill%28using%29.md) on the `dirtyRect` parameter passed into an override of [`draw(_:)`](./draw%28_%29.md). Because the `dirtyRect` now extends outside your view’s bounds, call [`fill(using:)`](../../CoreFoundation/cgrect/fill%28using%29.md) on the view’s bounds instead of the `dirtyRect`, or set the view’s [`clipsToBounds`](./clipstobounds.md) to [`true`](../../Swift/true.md).
- Differentiating a view’s bounds from its `dirtyRect`. Use the `dirtyRect` parameter passed to [`draw(_:)`](./draw%28_%29.md) to determine what to draw, not where to draw it. Use the view’s [`bounds`](./bounds.md) to determine the layout of what your view draws.

## See Also

### Drawing the View’s Content
- [func updateLayer()](./updatelayer%28%29.md)
  Updates the view’s content by modifying its underlying layer.
- [func draw(NSRect)](./draw%28_%29.md)
  Overridden by subclasses to draw the view’s image within the specified rectangle.
- [var canDrawConcurrently: Bool](./candrawconcurrently.md)
  A Boolean value indicating whether the view can draw its contents on a background thread.
- [var visibleRect: NSRect](./visiblerect.md)
  The portion of the view that isn’t clipped by its superviews.
- [func getRectsBeingDrawn(UnsafeMutablePointer<UnsafePointer<NSRect>?>?, count: UnsafeMutablePointer<Int>?)](./getrectsbeingdrawn%28_,count%29.md)
  Returns by indirection a list of nonoverlapping rectangles that define the area the view is being asked to draw in [`draw(_:)`](./draw%28_%29.md).
- [func needsToDraw(NSRect) -> Bool](./needstodraw%28_%29.md)
  Returns a Boolean value indicating whether the specified rectangle intersects any part of the area that the view is being asked to draw.
- [var wantsDefaultClipping: Bool](./wantsdefaultclipping.md)
  A Boolean value indicating whether AppKit’s default clipping behavior is in effect.
- [func bitmapImageRepForCachingDisplay(in: NSRect) -> NSBitmapImageRep?](./bitmapimagerepforcachingdisplay%28in%29.md)
  Returns a bitmap-representation object suitable for caching the specified portion of the view.
- [func cacheDisplay(in: NSRect, to: NSBitmapImageRep)](./cachedisplay%28in,to%29.md)
  Draws the specified area of the view, and its descendants, into a provided bitmap-representation object.
- [enum NSBorderType](../nsbordertype.md)
  These constants specify the type of a view’s border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/clipstobounds)*