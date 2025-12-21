# allocateGState()

**Framework**: AppKit  
**Kind**: method

Causes the view to maintain a private graphics state object, which encapsulates all parameters of the graphics environment.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func allocateGState()
```

#### Discussion

If you do not invoke [`allocateGState()`](nsview/allocategstate().md), a graphics state object is constructed from scratch each time the NSView is focused.

The view builds the graphics state parameters using [`setUpGState()`](nsview/setupgstate().md), then automatically establishes this graphics state each time the focus is locked on it. A graphics state may improve performance for view objects that are focused often and need to set many parameters, but use of standard rendering operators is normally efficient enough.

Because graphics states occupy a fair amount of memory, they can actually degrade performance. Be sure to test application performance with and without the private graphics state before committing to its use.

## See Also

- [func lockFocus()](nsview/lockfocus.md)
  Locks the focus on the view, so subsequent commands take effect in the view’s window and coordinate system.
- [func lockFocusIfCanDraw() -> Bool](nsview/lockfocusifcandraw.md)
  Locks the focus to the view atomically if the `canDraw` method returns `true` and returns the value of `canDraw`.
- [func lockFocusIfCanDraw(in: NSGraphicsContext) -> Bool](nsview/lockfocusifcandraw(in:).md)
  Locks the focus to the view atomically if drawing can occur in the specified graphics context.
- [func unlockFocus()](nsview/unlockfocus.md)
  Unlocks focus from the current view.
- [func scroll(NSRect, by: NSSize)](nsview/scroll(_:by:).md)
  Copies the visible portion of the view’s rendered image within a region and lays that portion down again at a specified offset .
- [func shouldDrawColor() -> Bool](nsview/shoulddrawcolor.md)
  Returns a Boolean value indicating whether the view is being drawn to an environment that supports color.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/allocategstate())*