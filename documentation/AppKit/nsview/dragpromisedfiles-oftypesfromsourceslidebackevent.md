# dragPromisedFiles(ofTypes:from:source:slideBack:event:)

**Framework**: AppKit  
**Kind**: method

Initiates a dragging operation from the view, allowing the user to drag one or more promised files (or directories) into any application that has window or view objects that accept promised file data.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func dragPromisedFiles(ofTypes typeArray: [String], from rect: NSRect, source sourceObject: Any, slideBack flag: Bool, event: NSEvent) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the drag operation is initiated successfully, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

This method must be invoked only within an implementation of the [`mouseDown(with:)`](nsresponder/mousedown(with:).md) method. As part of its implementation, this method invokes [`dragImage:at:offset:event:pasteboard:source:slideBack:`](nsview/dragimage:at:offset:event:pasteboard:source:slideback:.md).

Promised files are files that do not exist, yet, but that the drag source, `sourceObject`, promises to create at a file system location specified by the drag destination when the drag is successfully dropped.

See [`Drag and Drop Programming Topics`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DragandDrop/DragandDrop.html#//apple_ref/doc/uid/10000069i) for more information on dragging operations.

## Parameters

- `typeArray`: An array of file types being promised. The array elements can consist of file extensions and HFS types encoded with the   function. If promising a directory of files, only include the top directory in the array.
- `rect`: A rectangle that describes the position of the icon in the view’s coordinate system.
- `sourceObject`: An object that serves as the controller of the dragging operation. It must conform to the   protocol, and is typically the view itself or its   object.
- `flag`: A Boolean that indicates whether the icon being dragged should slide back to its position in the view if the file isn’t accepted. The icon slides back to   if   is  , the promised files are not accepted by the dragging destination, and the user has not disabled icon animation; otherwise it simply disappears.
- `event`: The mouse-down event object from which to initiate the drag operation. In particular, its mouse location is used for the offset of the icon being dragged.

## See Also

- [func unregisterDraggedTypes()](nsview/unregisterdraggedtypes.md)
  Unregisters the view as a possible destination in a dragging session.
- [func registerForDraggedTypes([NSPasteboard.PasteboardType])](nsview/registerfordraggedtypes(_:).md)
  Registers the pasteboard types that the view will accept as the destination of an image-dragging session.
- [func shouldDelayWindowOrdering(for: NSEvent) -> Bool](nsview/shoulddelaywindowordering(for:).md)
  Allows the user to drag objects from the view without activating the app or moving the window of the view forward, possibly obscuring the destination.
- [func beginDraggingSession(with: [NSDraggingItem], event: NSEvent, source: any NSDraggingSource) -> NSDraggingSession](nsview/begindraggingsession(with:event:source:).md)
  Initiates a dragging session with a group of dragging items.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/dragpromisedfiles(oftypes:from:source:slideback:event:))*