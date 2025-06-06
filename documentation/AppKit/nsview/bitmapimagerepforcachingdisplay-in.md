# bitmapImageRepForCachingDisplay(in:)

**Framework**: AppKit  
**Kind**: method

Returns a bitmap-representation object suitable for caching the specified portion of the view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func bitmapImageRepForCachingDisplay(in rect: NSRect) -> NSBitmapImageRep?
```

#### Return Value

An autoreleased [`NSBitmapImageRep`](nsbitmapimagerep.md) object or `nil` if the object could not be created.

#### Discussion

Passing the visible rectangle of the view (`[self visibleRect]`) returns a bitmap suitable for caching the current contents of the view, including all of its descendants.

## Parameters

- `rect`: A rectangle defining the area of the view to be cached.

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
- [var wantsDefaultClipping: Bool](nsview/wantsdefaultclipping.md)
  A Boolean value indicating whether AppKit’s default clipping behavior is in effect.
- [func cacheDisplay(in: NSRect, to: NSBitmapImageRep)](nsview/cachedisplay(in:to:).md)
  Draws the specified area of the view, and its descendants, into a provided bitmap-representation object.
- [enum NSBorderType](nsbordertype.md)
  These constants specify the type of a view’s border.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/bitmapimagerepforcachingdisplay(in:))*