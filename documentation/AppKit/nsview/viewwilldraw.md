# viewWillDraw()

**Framework**: AppKit  
**Kind**: method

Informs the view that it’s required to draw content.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
func viewWillDraw()
```

#### Discussion

In response to receiving one of the `display` methods, the view recurses down the view hierarchy, sending this message to each of the views that may be involved in the display operation.

Subclasses can override this method to move or resize views, mark additional areas as requiring display, or take other actions that can best be deferred until they are required for drawing. During the recursion, setting the [`needsDisplay`](nsview/needsdisplay.md) property or sending the [`setNeedsDisplay(_:)`](nsview/setneedsdisplay(_:).md) message to views in the hierarchy that are about to be drawn is valid and supported, and affects the assessment of the total area to be rendered in that drawing pass.

The following is an example of a generic subclass implementation:

```objc
- (void)viewWillDraw {
    // Perform some operations before recursing for descendants.
 
    // Now recurse to handle all our descendants.
    // Overrides must call up to super like this.
    [super viewWillDraw];
 
    // Perform some operations that might depend on descendants
    //  already having had a chance to update.
}
```

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
- [func translateRectsNeedingDisplay(in: NSRect, by: NSSize)](nsview/translaterectsneedingdisplay(in:by:).md)
  Translates the display rectangles by the specified delta.
- [var isOpaque: Bool](nsview/isopaque.md)
  A Boolean value indicating whether the view fills its frame rectangle with opaque content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/viewwilldraw())*