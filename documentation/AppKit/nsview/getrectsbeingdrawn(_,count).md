# getRectsBeingDrawn(_:count:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns by indirection a list of nonoverlapping rectangles that define the area the view is being asked to draw in [`draw(_:)`](./draw%28_%29.md).

**Availability**:
- macOS

## Declaration

```swift
func getRectsBeingDrawn(_ rects: UnsafeMutablePointer<UnsafePointer<NSRect>?>?, count: UnsafeMutablePointer<Int>?)
```

```objc
- (void) getRectsBeingDrawn:(const NSRect **) rects count:(NSInteger *) count;
```

## Discussion

An implementation of [`draw(_:)`](./draw%28_%29.md) can use this information to test whether objects or regions within the view intersect with the rectangles in the list, and thereby avoid unnecessary drawing that would be completely clipped away.

The [`needsToDraw(_:)`](./needstodraw%28_%29.md) method gives you a convenient way to test individual objects for intersection with the area being drawn in [`draw(_:)`](./draw%28_%29.md). However, you may want to retrieve and directly inspect the rectangle list if this is a more efficient way to perform intersection testing.

You should send this message only from within a [`draw(_:)`](./draw%28_%29.md) implementation. The `aRect` parameter of [`draw(_:)`](./draw%28_%29.md) is the rectangle enclosing the returned list of rectangles; you can use it in an initial pass to reject objects that are clearly outside the area to be drawn.

## Parameters

- `rects`: On return, contains a list of nonoverlapping rectangles defining areas to be drawn in. The rectangles returned in `rects` are in the coordinate space of the view.
- `count`: On return, the number of rectangles in the `rects` list.

## See Also

### Drawing the View’s Content
- [func updateLayer()](./updatelayer%28%29.md)
  Updates the view’s content by modifying its underlying layer.
- [func draw(NSRect)](./draw%28_%29.md)
  Overridden by subclasses to draw the view’s image within the specified rectangle.
- [var clipsToBounds: Bool](./clipstobounds.md)
  A Boolean value that indicates whether the view, and its subviews, confine their drawing areas to the bounds of the view.
- [var canDrawConcurrently: Bool](./candrawconcurrently.md)
  A Boolean value indicating whether the view can draw its contents on a background thread.
- [var visibleRect: NSRect](./visiblerect.md)
  The portion of the view that isn’t clipped by its superviews.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/getrectsbeingdrawn(_:count:))*