# wantsDefaultClipping

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether AppKit’s default clipping behavior is in effect.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var wantsDefaultClipping: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the default clipping is in effect, [`false`](https://developer.apple.com/documentation/swift/false) otherwise. By default, this method returns [`true`](https://developer.apple.com/documentation/swift/true).

#### Discussion

The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true). When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), AppKit sets the current clipping region to the bounds of the view prior to calling that view’s [`draw(_:)`](nsview/draw(_:).md) method. Subclasses may override this property and return [`false`](https://developer.apple.com/documentation/swift/false) to suppress this default clipping behavior. You might do this to avoid the cost of setting up, enforcing, and cleaning up the clipping path. If you do change the value to [`false`](https://developer.apple.com/documentation/swift/false), you are responsible for doing your own clipping or constraining drawing appropriately. Failure to do so could the view to corrupt the contents of other views in the window.

## See Also

- [func updateLayer()](nsview/updatelayer.md)
  Updates the view’s content by modifying its underlying layer.
- [func draw(NSRect)](nsview/draw(_:).md)
  Overridden by subclasses to draw the view’s image within the specified rectangle.
- [var clipsToBounds: Bool](nsview/clipstobounds.md)
  A Boolean value that indicates whether the view, and its subviews, confine their drawing areas to the bounds of the view.
- [var canDrawConcurrently: Bool](nsview/candrawconcurrently.md)
  A Boolean value indicating whether the view can draw its contents on a background thread.
- [var visibleRect: NSRect](nsview/visiblerect.md)
  The portion of the view that isn’t clipped by its superviews.
- [func getRectsBeingDrawn(UnsafeMutablePointer<UnsafePointer<NSRect>?>?, count: UnsafeMutablePointer<Int>?)](nsview/getrectsbeingdrawn(_:count:).md)
  Returns by indirection a list of nonoverlapping rectangles that define the area the view is being asked to draw in [`draw(_:)`](nsview/draw(_:).md).
- [func needsToDraw(NSRect) -> Bool](nsview/needstodraw(_:).md)
  Returns a Boolean value indicating whether the specified rectangle intersects any part of the area that the view is being asked to draw.
- [func bitmapImageRepForCachingDisplay(in: NSRect) -> NSBitmapImageRep?](nsview/bitmapimagerepforcachingdisplay(in:).md)
  Returns a bitmap-representation object suitable for caching the specified portion of the view.
- [func cacheDisplay(in: NSRect, to: NSBitmapImageRep)](nsview/cachedisplay(in:to:).md)
  Draws the specified area of the view, and its descendants, into a provided bitmap-representation object.
- [enum NSBorderType](nsbordertype.md)
  These constants specify the type of a view’s border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/wantsdefaultclipping)*