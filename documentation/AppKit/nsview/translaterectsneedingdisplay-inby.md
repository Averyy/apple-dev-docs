# translateRectsNeedingDisplay(in:by:)

**Framework**: AppKit  
**Kind**: method

Translates the display rectangles by the specified delta.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func translateRectsNeedingDisplay(in clipRect: NSRect, by delta: NSSize)
```

#### Discussion

This method performs the shifting of dirty rectangles that an equivalent [`scroll(_:by:)`](nsview/scroll(_:by:).md) operation would cause, without performing the actual scroll operation.  It is only useful in very rare cases where a view implements its own low-level scrolling mechanics.

This method:

1. Collects the receiving view’s dirty rectangles.
2. Clears all dirty rectangles in the intersection of `clipRect` and the view’s bounds.
3. Shifts the retrieved rectangles by the `delta` offset.
4. Clips the result to the intersection of `clipRect` and the view’s bounds
5. Marks the resultant rectangles as needing display.

The developer must ensure that `clipRect` and `delta` are pixel-aligned in order to guarantee correct drawing. See [`Transforming View Coordinates To and From Base Space`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaViewsGuide/WorkingWithAViewHierarchy/WorkingWithAViewHierarchy.html#//apple_ref/doc/uid/TP40002978-CH4-SW25) for a description of how to pixel-align view coordinates.

## Parameters

- `clipRect`: A rectangle defining the region of the view, typically the view’s bounds.
- `delta`: A NSSize structure that specifies an offset from aRect’s origin.

## See Also

- [func setNeedsDisplay(NSRect)](nsview/setneedsdisplay(_:).md)
  Marks the region of the view within the specified rectangle as needing display, increasing the view’s existing invalid region to include it.
- [var needsDisplay: Bool](nsview/needsdisplay.md)
  A Boolean value that determines whether the view needs to be redrawn before being displayed.
- [func display()](nsview/display.md)
  Displays the view and all its subviews if possible, invoking each of the `NSView` methods [`lockFocus()`](nsview/lockfocus().md), [`draw(_:)`](nsview/draw(_:).md), and [`unlockFocus()`](nsview/unlockfocus().md) as necessary.
- [func display(NSRect)](nsview/display(_:).md)
  Acts as [`display()`](nsview/display().md), but confining drawing to a rectangular region of the view.
- [func displayIgnoringOpacity(NSRect)](nsview/displayignoringopacity(_:).md)
  Displays the view but confines drawing to a specified region and does not back up to the first opaque ancestor—it simply causes the view and its descendants to execute their drawing code.
- [func displayIgnoringOpacity(NSRect, in: NSGraphicsContext)](nsview/displayignoringopacity(_:in:).md)
  Causes the view and its descendants to be redrawn to the specified graphics context.
- [func displayIfNeeded()](nsview/displayifneeded.md)
  Displays the view and all its subviews if any part of the view has been marked as needing display.
- [func displayIfNeeded(NSRect)](nsview/displayifneeded(_:).md)
  Acts as [`displayIfNeeded()`](nsview/displayifneeded().md), confining drawing to a specified region of the view.
- [func displayIfNeededIgnoringOpacity()](nsview/displayifneededignoringopacity.md)
  Acts as [`displayIfNeeded()`](nsview/displayifneeded().md), except that this method doesn’t back up to the first opaque ancestor—it simply causes the view and its descendants to execute their drawing code.
- [func displayIfNeededIgnoringOpacity(NSRect)](nsview/displayifneededignoringopacity(_:).md)
  Acts as [`displayIfNeeded()`](nsview/displayifneeded().md), but confining drawing to `aRect` and not backing up to the first opaque ancestor—it simply causes the view and its descendants to execute their drawing code.
- [var isOpaque: Bool](nsview/isopaque.md)
  A Boolean value indicating whether the view fills its frame rectangle with opaque content.
- [func viewWillDraw()](nsview/viewwilldraw.md)
  Informs the view that it’s required to draw content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/translaterectsneedingdisplay(in:by:))*