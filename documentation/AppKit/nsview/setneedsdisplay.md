# setNeedsDisplay(_:)

**Framework**: AppKit  
**Kind**: method

Marks the region of the view within the specified rectangle as needing display, increasing the view’s existing invalid region to include it.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setNeedsDisplay(_ invalidRect: NSRect)
```

#### Discussion

A later `displayIfNeeded` method will then perform drawing only within the invalid region. View objects marked as needing display are automatically redisplayed on each pass through the application’s event loop. (View objects that need to redisplay before the event loop comes around can of course immediately be sent the appropriate `display` method.)

## Parameters

- `invalidRect`: The rectangular region of the view to mark as invalid; it should be specified in the coordinate system of the view.

## See Also

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
- [func translateRectsNeedingDisplay(in: NSRect, by: NSSize)](nsview/translaterectsneedingdisplay(in:by:).md)
  Translates the display rectangles by the specified delta.
- [var isOpaque: Bool](nsview/isopaque.md)
  A Boolean value indicating whether the view fills its frame rectangle with opaque content.
- [func viewWillDraw()](nsview/viewwilldraw.md)
  Informs the view that it’s required to draw content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/setneedsdisplay(_:))*