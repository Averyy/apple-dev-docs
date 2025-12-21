# dragFile(_:from:slideBack:event:)

**Framework**: AppKit  
**Kind**: method

Initiates a dragging operation from the view, allowing the user to drag a file icon to any application that has window or view objects that accept files.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func dragFile(_ filename: String, from rect: NSRect, slideBack flag: Bool, event: NSEvent) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the view successfully initiates the dragging operation (which doesn’t necessarily mean the dragging operation concluded successfully). Otherwise, this method returns [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method must be invoked only within an implementation of the [`mouseDown(with:)`](nsresponder/mousedown(with:).md) method.

See the [`NSDraggingSource`](nsdraggingsource.md), [`NSDraggingInfo`](nsdragginginfo.md), and [`NSDraggingDestination`](nsdraggingdestination.md) protocol specifications for more information on dragging operations.

## Parameters

- `filename`: A string that specifies the absolute path for the file that is dragged.
- `rect`: A rectangle that describes the position of the icon in the view’s coordinate system.
- `flag`: A Boolean that indicates whether the icon being dragged should slide back to its position in the view if the file isn’t accepted. The icon slides back to   if   is  , the file is not accepted by the dragging destination, and the user has not disabled icon animation; otherwise it simply disappears.
- `event`: The mouse-down event object from which to initiate the drag operation. In particular, its mouse location is used for the offset of the icon being dragged.

## See Also

- [func shouldDelayWindowOrdering(for: NSEvent) -> Bool](nsview/shoulddelaywindowordering(for:).md)
  Allows the user to drag objects from the view without activating the app or moving the window of the view forward, possibly obscuring the destination.
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
- [func dragPromisedFiles(ofTypes: [String], from: NSRect, source: Any, slideBack: Bool, event: NSEvent) -> Bool](nsview/dragpromisedfiles(oftypes:from:source:slideback:event:).md)
  Initiates a dragging operation from the view, allowing the user to drag one or more promised files (or directories) into any application that has window or view objects that accept promised file data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/dragfile(_:from:slideback:event:))*