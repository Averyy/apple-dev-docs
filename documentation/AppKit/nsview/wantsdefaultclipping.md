# wantsDefaultClipping

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether AppKit’s default clipping behavior is in effect.

**Availability**:
- macOS

## Declaration

```swift
var wantsDefaultClipping: Bool { get }
```

```objc
@property (readonly) BOOL wantsDefaultClipping;
```

#### Return Value

[`true`](../../Swift/true.md) if the default clipping is in effect, [`false`](../../Swift/false.md) otherwise. By default, this method returns [`true`](../../Swift/true.md).

#### Discussion

The default value of this property is [`true`](../../Swift/true.md). When the value of this property is [`true`](../../Swift/true.md), AppKit sets the current clipping region to the bounds of the view prior to calling that view’s [`draw(_:)`](./draw%28_%29.md) method. Subclasses may override this property and return [`false`](../../Swift/false.md) to suppress this default clipping behavior. You might do this to avoid the cost of setting up, enforcing, and cleaning up the clipping path. If you do change the value to [`false`](../../Swift/false.md), you are responsible for doing your own clipping or constraining drawing appropriately. Failure to do so could the view to corrupt the contents of other views in the window.

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
- [func bitmapImageRepForCachingDisplay(in: NSRect) -> NSBitmapImageRep?](./bitmapimagerepforcachingdisplay%28in%29.md)
  Returns a bitmap-representation object suitable for caching the specified portion of the view.
- [func cacheDisplay(in: NSRect, to: NSBitmapImageRep)](./cachedisplay%28in,to%29.md)
  Draws the specified area of the view, and its descendants, into a provided bitmap-representation object.
- [enum NSBorderType](../nsbordertype.md)
  These constants specify the type of a view’s border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/wantsdefaultclipping)*