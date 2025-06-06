# registerForDraggedTypes(_:)

**Framework**: AppKit  
**Kind**: method

Registers a set of pasteboard types that the window accepts as the destination of an image-dragging session.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func registerForDraggedTypes(_ newTypes: [NSPasteboard.PasteboardType])
```

#### Discussion

Registering an `NSWindow` object for dragged types automatically makes it a candidate destination object for a dragging session. `NSWindow` has a default implementation for many of the methods in the [`NSDraggingDestination`](nsdraggingdestination.md) protocol. The default implementation forwards each message to the delegate if the delegate responds to the selector of the message. The messages forwarded this way are [`draggingEntered(_:)`](nsdraggingdestination/draggingentered(_:).md), [`draggingUpdated(_:)`](nsdraggingdestination/draggingupdated(_:).md), [`draggingExited(_:)`](nsdraggingdestination/draggingexited(_:).md), [`prepareForDragOperation(_:)`](nsdraggingdestination/preparefordragoperation(_:).md), [`performDragOperation(_:)`](nsdraggingdestination/performdragoperation(_:).md), and [`concludeDragOperation(_:)`](nsdraggingdestination/concludedragoperation(_:).md).

## Parameters

- `newTypes`: An array of the pasteboard types the window accepts as the destination of an image-dragging session.

## See Also

- [func drag(NSImage, at: NSPoint, offset: NSSize, event: NSEvent, pasteboard: NSPasteboard, source: Any, slideBack: Bool)](nswindow/drag(_:at:offset:event:pasteboard:source:slideback:).md)
  Begins a dragging session.
- [func unregisterDraggedTypes()](nswindow/unregisterdraggedtypes.md)
  Unregisters the window as a possible destination for dragging operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/registerfordraggedtypes(_:))*