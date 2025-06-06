# shouldDrawColor()

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value indicating whether the view is being drawn to an environment that supports color.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func shouldDrawColor() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the view’s window supports color drawing or [`false`](https://developer.apple.com/documentation/swift/false) if it does not.

#### Discussion

A view object can base its drawing behavior on the return value of this method to improve its appearance in grayscale windows. This method might return [`false`](https://developer.apple.com/documentation/swift/false) when the view’s window does not store color information because the content is destined for a grayscale printer.

## See Also

- [func draw(NSRect)](nsview/draw(_:).md)
  Overridden by subclasses to draw the view’s image within the specified rectangle.
- [func canStoreColor() -> Bool](nswindow/canstorecolor.md)
  Indicates whether the window has a depth limit that allows it to store color values.
- [func lockFocus()](nsview/lockfocus.md)
  Locks the focus on the view, so subsequent commands take effect in the view’s window and coordinate system.
- [func lockFocusIfCanDraw() -> Bool](nsview/lockfocusifcandraw.md)
  Locks the focus to the view atomically if the `canDraw` method returns [`true`](https://developer.apple.com/documentation/swift/true) and returns the value of `canDraw`.
- [func lockFocusIfCanDraw(in: NSGraphicsContext) -> Bool](nsview/lockfocusifcandraw(in:).md)
  Locks the focus to the view atomically if drawing can occur in the specified graphics context.
- [func unlockFocus()](nsview/unlockfocus.md)
  Unlocks focus from the current view.
- [func scroll(NSRect, by: NSSize)](nsview/scroll(_:by:).md)
  Copies the visible portion of the view’s rendered image within a region and lays that portion down again at a specified offset .
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/shoulddrawcolor())*