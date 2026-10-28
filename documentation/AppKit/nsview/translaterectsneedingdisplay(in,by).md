# translateRectsNeedingDisplay(in:by:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Translates the display rectangles by the specified delta.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func translateRectsNeedingDisplay(in clipRect: NSRect, by delta: NSSize)
```

```objc
- (void) translateRectsNeedingDisplayInRect:(NSRect) clipRect by:(NSSize) delta;
```

## Discussion

This method performs the shifting of dirty rectangles that an equivalent [`scroll(_:by:)`](./scroll%28_,by%29.md) operation would cause, without performing the actual scroll operation.  It is only useful in very rare cases where a view implements its own low-level scrolling mechanics.

This method:

1. Collects the receiving view’s dirty rectangles.
2. Clears all dirty rectangles in the intersection of `clipRect` and the view’s bounds.
3. Shifts the retrieved rectangles by the `delta` offset.
4. Clips the result to the intersection of `clipRect` and the view’s bounds
5. Marks the resultant rectangles as needing display.

The developer must ensure that `clipRect` and `delta` are pixel-aligned in order to guarantee correct drawing.

## Parameters

- `clipRect`: A rectangle defining the region of the view, typically the view’s bounds.
- `delta`: A NSSize structure that specifies an offset from aRect’s origin.

## See Also

### Invalidating the View’s Content
- [func setNeedsDisplay(NSRect)](./setneedsdisplay%28_%29.md)
  Marks the region of the view within the specified rectangle as needing display, increasing the view’s existing invalid region to include it.
- [var needsDisplay: Bool](./needsdisplay.md)
  A Boolean value that determines whether the view needs to be redrawn before being displayed.
- [func display()](./display%28%29.md)
  Displays the view and all its subviews if possible, invoking each of the `NSView` methods [`lockFocus()`](./lockfocus%28%29.md), [`draw(_:)`](./draw%28_%29.md), and [`unlockFocus()`](./unlockfocus%28%29.md) as necessary.
- [func display(NSRect)](./display%28_%29.md)
  Acts as [`display()`](./display%28%29.md), but confining drawing to a rectangular region of the view.
- [func displayIgnoringOpacity(NSRect)](./displayignoringopacity%28_%29.md)
  Displays the view but confines drawing to a specified region and does not back up to the first opaque ancestor—it simply causes the view and its descendants to execute their drawing code.
- [func displayIgnoringOpacity(NSRect, in: NSGraphicsContext)](./displayignoringopacity%28_,in%29.md)
  Causes the view and its descendants to be redrawn to the specified graphics context.
- [func displayIfNeeded()](./displayifneeded%28%29.md)
  Displays the view and all its subviews if any part of the view has been marked as needing display.
- [func displayIfNeeded(NSRect)](./displayifneeded%28_%29.md)
  Acts as [`displayIfNeeded()`](./displayifneeded%28%29.md), confining drawing to a specified region of the view.
- [func displayIfNeededIgnoringOpacity()](./displayifneededignoringopacity%28%29.md)
  Acts as [`displayIfNeeded()`](./displayifneeded%28%29.md), except that this method doesn’t back up to the first opaque ancestor—it simply causes the view and its descendants to execute their drawing code.
- [func displayIfNeededIgnoringOpacity(NSRect)](./displayifneededignoringopacity%28_%29.md)
  Acts as [`displayIfNeeded()`](./displayifneeded%28%29.md), but confining drawing to `aRect` and not backing up to the first opaque ancestor—it simply causes the view and its descendants to execute their drawing code.
- [var isOpaque: Bool](./isopaque.md)
  A Boolean value indicating whether the view fills its frame rectangle with opaque content.
- [func viewWillDraw()](./viewwilldraw%28%29.md)
  Informs the view that it’s required to draw content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/translaterectsneedingdisplay(in:by:))*