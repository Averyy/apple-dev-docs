# scroll(_:by:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Copies the visible portion of the view’s rendered image within a region and lays that portion down again at a specified offset .

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use NSScrollView to achieve scrolling views.

## Declaration

```swift
func scroll(_ rect: NSRect, by delta: NSSize)
```

```objc
- (void) scrollRect:(NSRect) rect by:(NSSize) delta;
```

#### Discussion

This method is useful during scrolling or translation of the coordinate system to efficiently move as much of the view’s rendered image as possible without requiring it to be redrawn, following these steps:

1. Invoke [`scroll(_:by:)`](./scroll%28_,by%29.md) to copy the rendered image.
2. Move the view object’s origin or scroll it within its superview.
3. Calculate the newly exposed rectangles and either set the [`needsDisplay`](./needsdisplay.md) property to [`true`](../../Swift/true.md) or call [`setNeedsDisplay(_:)`](./setneedsdisplay%28_%29.md) to draw them.

You should rarely need to use this method, however. The [`scroll(_:)`](./scroll%28_%29.md), [`scrollToVisible(_:)`](./scrolltovisible%28_%29.md), and [`autoscroll(with:)`](./autoscroll%28with%29.md) methods automatically perform optimized scrolling.

## Parameters

- `rect`: A rectangle defining a region of the view.
- `delta`: A `NSSize` structure that specifies an offset from `aRect`’s origin.

## See Also

### Related Documentation
- [func setBoundsOrigin(NSPoint)](./setboundsorigin%28_%29.md)
  Sets the origin of the view’s bounds rectangle to a specified point.
- [func translateOrigin(to: NSPoint)](./translateorigin%28to%29.md)
  Translates the view’s coordinate system so that its origin moves to a new location.
### Deprecated methods
- [func lockFocus()](./lockfocus%28%29.md)
  Locks the focus on the view, so subsequent commands take effect in the view’s window and coordinate system.
- [func lockFocusIfCanDraw() -> Bool](./lockfocusifcandraw%28%29.md)
  Locks the focus to the view atomically if the `canDraw` method returns `true` and returns the value of `canDraw`.
- [func lockFocusIfCanDraw(in: NSGraphicsContext) -> Bool](./lockfocusifcandraw%28in%29.md)
  Locks the focus to the view atomically if drawing can occur in the specified graphics context.
- [func unlockFocus()](./unlockfocus%28%29.md)
  Unlocks focus from the current view.
- [func shouldDrawColor() -> Bool](./shoulddrawcolor%28%29.md)
  Returns a Boolean value indicating whether the view is being drawn to an environment that supports color.
- [func allocateGState()](./allocategstate%28%29.md)
  Causes the view to maintain a private graphics state object, which encapsulates all parameters of the graphics environment.
- [func gState() -> Int](./gstate%28%29.md)
  Returns the identifier for the view’s graphics state object, or 0 if the view doesn’t have a graphics state object.
- [func setUpGState()](./setupgstate%28%29.md)
  Overridden by subclasses to (re)initialize the view’s graphics state object.
- [func renewGState()](./renewgstate%28%29.md)
  Invalidates the view’s graphics state object, if it has one.
- [func releaseGState()](./releasegstate%28%29.md)
  Frees the view’s graphics state object, if it has one.
- [func dragFile(String, from: NSRect, slideBack: Bool, event: NSEvent) -> Bool](./dragfile%28_,from,slideback,event%29.md)
  Initiates a dragging operation from the view, allowing the user to drag a file icon to any application that has window or view objects that accept files.
- [func dragPromisedFiles(ofTypes: [String], from: NSRect, source: Any, slideBack: Bool, event: NSEvent) -> Bool](./dragpromisedfiles%28oftypes,from,source,slideback,event%29.md)
  Initiates a dragging operation from the view, allowing the user to drag one or more promised files (or directories) into any application that has window or view objects that accept promised file data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/scroll(_:by:))*