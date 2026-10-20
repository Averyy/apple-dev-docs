# cacheDisplay(in:to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the specified area of the view, and its descendants, into a provided bitmap-representation object.

**Availability**:
- macOS

## Declaration

```swift
func cacheDisplay(in rect: NSRect, to bitmapImageRep: NSBitmapImageRep)
```

```objc
- (void) cacheDisplayInRect:(NSRect) rect toBitmapImageRep:(NSBitmapImageRep *) bitmapImageRep;
```

#### Discussion

You are responsible for initializing the bitmap to the desired configuration before calling this method. However, once initialized, you can reuse the same bitmap multiple times to refresh the cached copy of your view’s contents.

The bitmap produced by this method is transparent (that is, has an alpha value of 0) wherever the view and its descendants do not draw any content.

## Parameters

- `rect`: A rectangle defining the region to be drawn into `bitmapImageRep`.
- `bitmapImageRep`: An [`NSBitmapImageRep`](../nsbitmapimagerep.md) object. For pixel-format compatibility, `bitmapImageRep` should have been obtained from [`bitmapImageRepForCachingDisplay(in:)`](./bitmapimagerepforcachingdisplay%28in%29.md).

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
- [func needsToDraw(NSRect) -> Bool](./needstodraw%28_%29.md)
  Returns a Boolean value indicating whether the specified rectangle intersects any part of the area that the view is being asked to draw.
- [var wantsDefaultClipping: Bool](./wantsdefaultclipping.md)
  A Boolean value indicating whether AppKit’s default clipping behavior is in effect.
- [func bitmapImageRepForCachingDisplay(in: NSRect) -> NSBitmapImageRep?](./bitmapimagerepforcachingdisplay%28in%29.md)
  Returns a bitmap-representation object suitable for caching the specified portion of the view.
- [enum NSBorderType](../nsbordertype.md)
  These constants specify the type of a view’s border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/cachedisplay(in:to:))*