# updateLayer()

**Framework**: AppKit  
**Kind**: method

Updates the view’s content by modifying its underlying layer.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
func updateLayer()
```

#### Discussion

You use this method to optimize the rendering of your view in situations where you can represent your views contents entirely using a layer object. If your view’s [`wantsUpdateLayer`](nsview/wantsupdatelayer.md) property is [`true`](https://developer.apple.com/documentation/swift/true), the view calls this method instead of [`draw(_:)`](nsview/draw(_:).md) during the view update cycle. Custom views can override this method and use it to modify the properties of the underlying layer object. Modifying layer properties is a much more efficient way to update your view than is redrawing its content each time something changes.

When you want to update the contents of your layer, mark the view as dirty by setting its [`needsDisplay`](nsview/needsdisplay.md) property to [`true`](https://developer.apple.com/documentation/swift/true). Doing so adds the view to the list of views that need to be refreshed during the next update cycle. During that update cycle, this method is called if the [`wantsUpdateLayer`](nsview/wantsupdatelayer.md) property is still [`true`](https://developer.apple.com/documentation/swift/true).

Your implementation of this method should not call `super`.

## See Also

- [var wantsUpdateLayer: Bool](nsview/wantsupdatelayer.md)
  A Boolean value indicating which drawing path the view takes when updating its contents.
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
- [var wantsDefaultClipping: Bool](nsview/wantsdefaultclipping.md)
  A Boolean value indicating whether AppKit’s default clipping behavior is in effect.
- [func bitmapImageRepForCachingDisplay(in: NSRect) -> NSBitmapImageRep?](nsview/bitmapimagerepforcachingdisplay(in:).md)
  Returns a bitmap-representation object suitable for caching the specified portion of the view.
- [func cacheDisplay(in: NSRect, to: NSBitmapImageRep)](nsview/cachedisplay(in:to:).md)
  Draws the specified area of the view, and its descendants, into a provided bitmap-representation object.
- [enum NSBorderType](nsbordertype.md)
  These constants specify the type of a view’s border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/updatelayer())*