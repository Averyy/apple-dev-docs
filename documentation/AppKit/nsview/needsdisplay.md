# needsDisplay

**Framework**: AppKit  
**Kind**: property

A Boolean value that determines whether the view needs to be redrawn before being displayed.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var needsDisplay: Bool { get set }
```

#### Discussion

The `displayIfNeeded` methods check the value of this property to avoid unnecessary drawing, and all display methods set the value back to [`false`](https://developer.apple.com/documentation/Swift/false) when the view is up to date.

Whenever the data or state affecting the view’s appearance changes, set this property to [`true`](https://developer.apple.com/documentation/Swift/true). This marks the view as needing to update its display. On the next pass through the app’s event loop, the view is automatically redisplayed.

## See Also

- [func setNeedsDisplay(NSRect)](nsview/setneedsdisplay(_:).md)
  Marks the region of the view within the specified rectangle as needing display, increasing the view’s existing invalid region to include it.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/needsdisplay)*