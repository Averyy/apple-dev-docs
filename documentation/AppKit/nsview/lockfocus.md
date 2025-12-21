# lockFocus()

**Framework**: AppKit  
**Kind**: method

Locks the focus on the view, so subsequent commands take effect in the view’s window and coordinate system.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func lockFocus()
```

#### Discussion

If you don’t use a `display` method to draw an `NSView` object, you must invoke [`lockFocus()`](nsview/lockfocus().md) before invoking methods that send commands to the window server, and must balance it with an [`unlockFocus()`](nsview/unlockfocus().md) message when finished.

Hiding or miniaturizing a one-shot window causes the backing store for that window to be released. (A one-shot window frees its window device when the window is hidden and another is created when it’s returned to the screen.) If you don’t use the standard display mechanism to draw, you should use [`lockFocusIfCanDraw()`](nsview/lockfocusifcandraw().md) rather than [`lockFocus()`](nsview/lockfocus().md) if there is a chance of drawing while the window is either miniaturized or hidden. This method throws an exception if the view is hidden or if drawing cannot happen for some other reason. To ensure that you can lock focus successfully, make sure the [`canDraw`](nsview/candraw.md) property is [`true`](https://developer.apple.com/documentation/Swift/true); you can also call [`lockFocusIfCanDraw()`](nsview/lockfocusifcandraw().md) instead and use the return value of that method to determine if focus was obtained successfully.

## See Also

- [func draw(NSRect)](nsview/draw(_:).md)
  Overridden by subclasses to draw the view’s image within the specified rectangle.
- [class var focusView: NSView?](nsview/focusview.md)
  The currently focused view object.
- [func display()](nsview/display.md)
  Displays the view and all its subviews if possible, invoking each of the `NSView` methods [`lockFocus()`](nsview/lockfocus().md), [`draw(_:)`](nsview/draw(_:).md), and [`unlockFocus()`](nsview/unlockfocus().md) as necessary.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/lockfocus())*