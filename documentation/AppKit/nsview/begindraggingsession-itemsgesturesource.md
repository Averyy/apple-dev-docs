# beginDraggingSession(items:gesture:source:)

**Framework**: AppKit  
**Kind**: method

Initiates a drag operation using a gesture recognizer.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func beginDraggingSession(items: [NSDraggingItem], gesture: NSGestureRecognizer, source: any NSDraggingSource) -> NSDraggingSession?
```

#### Return Value

The dragging session for the drag, or `nil` if the method can’t start the session.

#### Discussion

Like [`beginDraggingSession(with:event:source:)`](nsview/begindraggingsession(with:event:source:).md), this method starts an internal tracking loop. If the gesture is mouse-based, the system cancels the gesture at the end of the drag-and-drop operation. If the gesture is touch-based, the system cancels the gesture at the start of the drag-and-drop operation.

The system may animate drag images from their initial positions into a system-defined formation. The system clips the drag to the visible area of the view.

```swift
var dragSession: NSDraggingSession?

@objc func handleDragGesture(_ gestureRecognizer: NSGestureRecognizer) {
    if gestureRecognizer.state == .began {
        let items = [NSDraggingItem(pasteboardWriter: myPasteboardItem)]
        
        // Returns nil if the drag fails to start.
        dragSession = self.beginDraggingSession(items: items, gesture: gestureRecognizer, source: self)
    }
}
```

## Parameters

- `items`: The dragging items. The frame property of each [`NSDraggingItem`](nsdraggingitem.md) must be in the view’s coordinate system.
- `gesture`: The gesture recognizer initiating the drag session.
- `source`: An object that controls the dragging operation and conforms to the [`NSDraggingSource`](nsdraggingsource.md) protocol.

## See Also

- [func beginDraggingSession(with: [NSDraggingItem], event: NSEvent, source: any NSDraggingSource) -> NSDraggingSession](nsview/begindraggingsession(with:event:source:).md)
  Initiates a dragging session with a group of dragging items.
- [func registerForDraggedTypes([NSPasteboard.PasteboardType])](nsview/registerfordraggedtypes(_:).md)
  Registers the pasteboard types that the view will accept as the destination of an image-dragging session.
- [func unregisterDraggedTypes()](nsview/unregisterdraggedtypes.md)
  Unregisters the view as a possible destination in a dragging session.
- [var registeredDraggedTypes: [NSPasteboard.PasteboardType]](nsview/registereddraggedtypes.md)
  The array of pasteboard drag types that the view can accept.
- [func beginDraggingSession(with: [NSDraggingItem], event: NSEvent, source: any NSDraggingSource) -> NSDraggingSession](nsview/begindraggingsession(with:event:source:).md)
  Initiates a dragging session with a group of dragging items.
- [func shouldDelayWindowOrdering(for: NSEvent) -> Bool](nsview/shoulddelaywindowordering(for:).md)
  Allows the user to drag objects from the view without activating the app or moving the window of the view forward, possibly obscuring the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/begindraggingsession(items:gesture:source:))*