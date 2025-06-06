# scroll(_:by:)

**Framework**: AppKit  
**Kind**: method

Copies the visible portion of the view’s rendered image within a region and lays that portion down again at a specified offset .

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func scroll(_ rect: NSRect, by delta: NSSize)
```

#### Discussion

This method is useful during scrolling or translation of the coordinate system to efficiently move as much of the view’s rendered image as possible without requiring it to be redrawn, following these steps:

1. Invoke [`scroll(_:by:)`](nsview/scroll(_:by:).md) to copy the rendered image.
2. Move the view object’s origin or scroll it within its superview.
3. Calculate the newly exposed rectangles and either set the [`needsDisplay`](nsview/needsdisplay.md) property to [`true`](https://developer.apple.com/documentation/swift/true) or call [`setNeedsDisplay(_:)`](nsview/setneedsdisplay(_:).md) to draw them.

You should rarely need to use this method, however. The [`scroll(_:)`](nsview/scroll(_:).md), [`scrollToVisible(_:)`](nsview/scrolltovisible(_:).md), and [`autoscroll(with:)`](nsview/autoscroll(with:).md) methods automatically perform optimized scrolling.

## Parameters

- `rect`: A rectangle defining a region of the view.
- `delta`: A   structure that specifies an offset from  ’s origin.

## See Also

- [func setBoundsOrigin(NSPoint)](nsview/setboundsorigin(_:).md)
  Sets the origin of the view’s bounds rectangle to a specified point.
- [func translateOrigin(to: NSPoint)](nsview/translateorigin(to:).md)
  Translates the view’s coordinate system so that its origin moves to a new location.
- [func lockFocus()](nsview/lockfocus.md)
  Locks the focus on the view, so subsequent commands take effect in the view’s window and coordinate system.
- [func lockFocusIfCanDraw() -> Bool](nsview/lockfocusifcandraw.md)
  Locks the focus to the view atomically if the `canDraw` method returns [`true`](https://developer.apple.com/documentation/swift/true) and returns the value of `canDraw`.
- [func lockFocusIfCanDraw(in: NSGraphicsContext) -> Bool](nsview/lockfocusifcandraw(in:).md)
  Locks the focus to the view atomically if drawing can occur in the specified graphics context.
- [func unlockFocus()](nsview/unlockfocus.md)
  Unlocks focus from the current view.
- [func shouldDrawColor() -> Bool](nsview/shoulddrawcolor.md)
  Returns a Boolean value indicating whether the view is being drawn to an environment that supports color.
- [func allocateGState()](nsview/allocategstate.md)
  Causes the view to maintain a private graphics state object, which encapsulates all parameters of the graphics environment.
- [func gState() -> Int](nsview/gstate.md)
  Returns the identifier for the view’s graphics state object, or 0 if the view doesn’t have a graphics state object.
- [func setUpGState()](nsview/setupgstate.md)
  Overridden by subclasses to (re)initialize the view’s graphics state object.
- [func renewGState()](nsview/renewgstate.md)
  Invalidates the view’s graphics state object, if it has one.
- [func releaseGState()](nsview/releasegstate.md)
  Frees the view’s graphics state object, if it has one.
- [func dragFile(String, from: NSRect, slideBack: Bool, event: NSEvent) -> Bool](nsview/dragfile(_:from:slideback:event:).md)
  Initiates a dragging operation from the view, allowing the user to drag a file icon to any application that has window or view objects that accept files.
- [func dragPromisedFiles(ofTypes: [String], from: NSRect, source: Any, slideBack: Bool, event: NSEvent) -> Bool](nsview/dragpromisedfiles(oftypes:from:source:slideback:event:).md)
  Initiates a dragging operation from the view, allowing the user to drag one or more promised files (or directories) into any application that has window or view objects that accept promised file data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/scroll(_:by:))*