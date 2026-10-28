# canDrawConcurrently

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view can draw its contents on a background thread.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var canDrawConcurrently: Bool { get set }
```

```objc
@property BOOL canDrawConcurrently;
```

## Discussion

If your view’s [`draw(_:)`](./draw%28_%29.md) implementation can draw safely on a background thread, set this property to [`true`](../../Swift/true.md). Doing so gives AppKit the ability to run your view’s drawing code off the app’s main thread, which can improve performance. The view’s window must also have its [`allowsConcurrentViewDrawing`](../nswindow/allowsconcurrentviewdrawing.md) property set to [`true`](../../Swift/true.md) (the default) for threaded view drawing to occur.

## See Also

### Drawing the View’s Content
- [func updateLayer()](./updatelayer%28%29.md)
  Updates the view’s content by modifying its underlying layer.
- [func draw(NSRect)](./draw%28_%29.md)
  Overridden by subclasses to draw the view’s image within the specified rectangle.
- [var clipsToBounds: Bool](./clipstobounds.md)
  A Boolean value that indicates whether the view, and its subviews, confine their drawing areas to the bounds of the view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/candrawconcurrently)*