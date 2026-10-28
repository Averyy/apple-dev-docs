# viewWillDraw()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the view that it’s required to draw content.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func viewWillDraw()
```

```objc
- (void) viewWillDraw;
```

## Discussion

In response to receiving one of the `display` methods, the view recurses down the view hierarchy, sending this message to each of the views that may be involved in the display operation.

Subclasses can override this method to move or resize views, mark additional areas as requiring display, or take other actions that can best be deferred until they are required for drawing. During the recursion, setting the [`needsDisplay`](./needsdisplay.md) property or sending the [`setNeedsDisplay(_:)`](./setneedsdisplay%28_%29.md) message to views in the hierarchy that are about to be drawn is valid and supported, and affects the assessment of the total area to be rendered in that drawing pass.

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
- [func translateRectsNeedingDisplay(in: NSRect, by: NSSize)](./translaterectsneedingdisplay%28in,by%29.md)
  Translates the display rectangles by the specified delta.
- [var isOpaque: Bool](./isopaque.md)
  A Boolean value indicating whether the view fills its frame rectangle with opaque content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/viewwilldraw())*