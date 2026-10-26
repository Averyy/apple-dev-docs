# dragPromisedFiles(ofTypes:from:source:slideBack:event:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Initiates a dragging operation from the view, allowing the user to drag one or more promised files (or directories) into any application that has window or view objects that accept promised file data.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use [`beginDraggingSession(with:event:source:)`](./begindraggingsession%28with,event,source%29.md) instead.

## Declaration

```swift
func dragPromisedFiles(ofTypes typeArray: [String], from rect: NSRect, source sourceObject: Any, slideBack flag: Bool, event: NSEvent) -> Bool
```

```objc
- (BOOL) dragPromisedFilesOfTypes:(NSArray<NSString *> *) typeArray fromRect:(NSRect) rect source:(id) sourceObject slideBack:(BOOL) flag event:(NSEvent *) event;
```

#### Return Value

[`true`](../../Swift/true.md) if the drag operation is initiated successfully, [`false`](../../Swift/false.md) otherwise.

#### Discussion

This method must be invoked only within an implementation of the [`mouseDown(with:)`](../nsresponder/mousedown%28with%29.md) method. As part of its implementation, this method invokes [`dragImage:at:offset:event:pasteboard:source:slideBack:`](./dragimage_at_offset_event_pasteboard_source_slideback_.md).

Promised files are files that do not exist, yet, but that the drag source, `sourceObject`, promises to create at a file system location specified by the drag destination when the drag is successfully dropped.

See [Drag and Drop](../drag-and-drop.md) for more information on dragging operations.

## Parameters

- `typeArray`: An array of file types being promised. The array elements can consist of file extensions and HFS types encoded with the [`NSFileTypeForHFSTypeCode(_:)`](../../Foundation/nsfiletypeforhfstypecode%28_%29.md) function. If promising a directory of files, only include the top directory in the array.
- `rect`: A rectangle that describes the position of the icon in the view’s coordinate system.
- `sourceObject`: An object that serves as the controller of the dragging operation. It must conform to the [`NSDraggingSource`](../nsdraggingsource.md) protocol, and is typically the view itself or its [`NSWindow`](../nswindow.md) object.
- `flag`: A Boolean that indicates whether the icon being dragged should slide back to its position in the view if the file isn’t accepted. The icon slides back to `aRect` if `slideBack` is [`true`](../../Swift/true.md), the promised files are not accepted by the dragging destination, and the user has not disabled icon animation; otherwise it simply disappears.
- `event`: The mouse-down event object from which to initiate the drag operation. In particular, its mouse location is used for the offset of the icon being dragged.

## See Also

### Related Documentation
- [func unregisterDraggedTypes()](./unregisterdraggedtypes%28%29.md)
  Unregisters the view as a possible destination in a dragging session.
- [func registerForDraggedTypes([NSPasteboard.PasteboardType])](./registerfordraggedtypes%28_%29.md)
  Registers the pasteboard types that the view will accept as the destination of an image-dragging session.
- [func shouldDelayWindowOrdering(for: NSEvent) -> Bool](./shoulddelaywindowordering%28for%29.md)
  Allows the user to drag objects from the view without activating the app or moving the window of the view forward, possibly obscuring the destination.
- [func beginDraggingSession(with: [NSDraggingItem], event: NSEvent, source: any NSDraggingSource) -> NSDraggingSession](./begindraggingsession%28with,event,source%29.md)
  Initiates a dragging session with a group of dragging items.
- [- dragImage:at:offset:event:pasteboard:source:slideBack:](./dragimage_at_offset_event_pasteboard_source_slideback_.md)
  Initiates a dragging operation from the view, allowing the user to drag arbitrary data with a specified icon into any application that has window or view objects that accept dragged data.
### Deprecated methods
- [func lockFocus()](./lockfocus%28%29.md)
  Locks the focus on the view, so subsequent commands take effect in the view’s window and coordinate system.
- [func lockFocusIfCanDraw() -> Bool](./lockfocusifcandraw%28%29.md)
  Locks the focus to the view atomically if the `canDraw` method returns `true` and returns the value of `canDraw`.
- [func lockFocusIfCanDraw(in: NSGraphicsContext) -> Bool](./lockfocusifcandraw%28in%29.md)
  Locks the focus to the view atomically if drawing can occur in the specified graphics context.
- [func unlockFocus()](./unlockfocus%28%29.md)
  Unlocks focus from the current view.
- [func scroll(NSRect, by: NSSize)](./scroll%28_,by%29.md)
  Copies the visible portion of the view’s rendered image within a region and lays that portion down again at a specified offset .
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
- [- convertPointToBase:](./convertpointtobase_.md)
  Converts the point from the view’s coordinate system to the base coordinate system.
- [- convertPointFromBase:](./convertpointfrombase_.md)
  Converts the point from the base coordinate system to the view’s coordinate system.
- [- convertSizeToBase:](./convertsizetobase_.md)
  Converts the size from the view’s coordinate system to the base coordinate system.
- [- convertSizeFromBase:](./convertsizefrombase_.md)
  Converts the size from the base coordinate system to the view’s coordinate system.
- [- convertRectToBase:](./convertrecttobase_.md)
  Converts the rectangle from the view’s coordinate system to the base coordinate system.
- [- convertRectFromBase:](./convertrectfrombase_.md)
  Converts the rectangle from the base coordinate system to the view’s coordinate system.
- [- performMnemonic:](./performmnemonic_.md)
  Implemented by subclasses to respond to mnemonics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/dragpromisedfiles(oftypes:from:source:slideback:event:))*