# visibleRect

**Framework**: AppKit  
**Kind**: property

The portion of the view that isn’t clipped by its superviews.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var visibleRect: NSRect { get }
```

#### Discussion

Visibility, as reflected by this property, doesn’t account for whether other view or window objects overlap the current view or whether the current view is installed in a window at all. This value of this property is `NSZeroRect` if the current view is effectively hidden.

During a printing operation the visible rectangle is further clipped to the page being imaged.

[`clipsToBounds`](nsview/clipstobounds.md) affects this property.

## See Also

- [var isHidden: Bool](nsview/ishidden.md)
  A Boolean value indicating whether the view is hidden.
- [var documentVisibleRect: NSRect](nsscrollview/documentvisiblerect.md)
  The portion of the document view, in its own coordinate system, visible through the scroll view’s content view.
- [var documentVisibleRect: NSRect](nsclipview/documentvisiblerect.md)
  The exposed rectangle of the clip view’s document view, in the document view’s own coordinate system.
- [var isVisible: Bool](nswindow/isvisible.md)
  A Boolean value that indicates whether the window is visible onscreen (even when it’s obscured by other windows).
- [func updateLayer()](nsview/updatelayer.md)
  Updates the view’s content by modifying its underlying layer.
- [func draw(NSRect)](nsview/draw(_:).md)
  Overridden by subclasses to draw the view’s image within the specified rectangle.
- [var clipsToBounds: Bool](nsview/clipstobounds.md)
  A Boolean value that indicates whether the view, and its subviews, confine their drawing areas to the bounds of the view.
- [var canDrawConcurrently: Bool](nsview/candrawconcurrently.md)
  A Boolean value indicating whether the view can draw its contents on a background thread.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/visiblerect)*