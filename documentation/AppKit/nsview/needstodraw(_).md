# needsToDraw(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the specified rectangle intersects any part of the area that the view is being asked to draw.

**Availability**:
- macOS

## Declaration

```swift
func needsToDraw(_ rect: NSRect) -> Bool
```

```objc
- (BOOL) needsToDrawRect:(NSRect) rect;
```

#### Discussion

You typically send this message from within a [`draw(_:)`](./draw%28_%29.md) implementation. It gives you a convenient way to determine whether any part of a given graphical entity might need to be drawn. It is optimized to efficiently reject any rectangle that lies outside the bounding box of the area that the view is being asked to draw in [`draw(_:)`](./draw%28_%29.md).

## Parameters

- `rect`: A rectangle defining a region of the view.

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
- [func getRectsBeingDrawn(UnsafeMutablePointer<UnsafePointer<NSRect>?>?, count: UnsafeMutablePointer<Int>?)](./getrectsbeingdrawn%28_,count%29.md)
  Returns by indirection a list of nonoverlapping rectangles that define the area the view is being asked to draw in [`draw(_:)`](./draw%28_%29.md).
- [var wantsDefaultClipping: Bool](./wantsdefaultclipping.md)
  A Boolean value indicating whether AppKit’s default clipping behavior is in effect.
- [func bitmapImageRepForCachingDisplay(in: NSRect) -> NSBitmapImageRep?](./bitmapimagerepforcachingdisplay%28in%29.md)
  Returns a bitmap-representation object suitable for caching the specified portion of the view.
- [func cacheDisplay(in: NSRect, to: NSBitmapImageRep)](./cachedisplay%28in,to%29.md)
  Draws the specified area of the view, and its descendants, into a provided bitmap-representation object.
- [enum NSBorderType](../nsbordertype.md)
  These constants specify the type of a view’s border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/needstodraw(_:))*