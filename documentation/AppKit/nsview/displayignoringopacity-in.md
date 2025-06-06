# displayIgnoringOpacity(_:in:)

**Framework**: AppKit  
**Kind**: method

Causes the view and its descendants to be redrawn to the specified graphics context.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func displayIgnoringOpacity(_ rect: NSRect, in context: NSGraphicsContext)
```

#### Discussion

Acts as [`display()`](nsview/display().md), but confines drawing to `aRect`. This method initiates drawing with the view, even if the view is not opaque. Appropriate scaling factors for the view are obtained from `context`.

If the `context` parameter represents the context for the window containing the view, then all of the necessary transformations are applied. This includes the application of the view’s bounds and frame transforms along with any transforms it inherited from its ancestors. In this situation, the view is also marked as no longer needing an update for the specified rectangle.

If `context` specifies any other graphics context, then only the view’s bounds transform is applied. This means that drawing is not constrained to the view’s visible rectangle. It also means that any dirty rectangles are not cleared, since they are not being redrawn to the window.

## Parameters

- `rect`: A rectangle defining the region of the view to be redrawn. It should be specified in the coordinate system of the view.
- `context`: The graphics context in which drawing will occur. See the discussion below for more about this parameter.

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
- [func displayIfNeeded()](nsview/displayifneeded.md)
  Displays the view and all its subviews if any part of the view has been marked as needing display.
- [func displayIfNeeded(NSRect)](nsview/displayifneeded(_:).md)
  Acts as [`displayIfNeeded()`](nsview/displayifneeded().md), confining drawing to a specified region of the view.
- [func displayIfNeededIgnoringOpacity()](nsview/displayifneededignoringopacity.md)
  Acts as [`displayIfNeeded()`](nsview/displayifneeded().md), except that this method doesn’t back up to the first opaque ancestor—it simply causes the view and its descendants to execute their drawing code.
- [func displayIfNeededIgnoringOpacity(NSRect)](nsview/displayifneededignoringopacity(_:).md)
  Acts as [`displayIfNeeded()`](nsview/displayifneeded().md), but confining drawing to `aRect` and not backing up to the first opaque ancestor—it simply causes the view and its descendants to execute their drawing code.
- [func translateRectsNeedingDisplay(in: NSRect, by: NSSize)](nsview/translaterectsneedingdisplay(in:by:).md)
  Translates the display rectangles by the specified delta.
- [var isOpaque: Bool](nsview/isopaque.md)
  A Boolean value indicating whether the view fills its frame rectangle with opaque content.
- [func viewWillDraw()](nsview/viewwilldraw.md)
  Informs the view that it’s required to draw content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/displayignoringopacity(_:in:))*