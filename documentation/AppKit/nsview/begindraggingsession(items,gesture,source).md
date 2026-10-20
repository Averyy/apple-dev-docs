# beginDraggingSession(items:gesture:source:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Initiates a drag operation using a gesture recognizer.

**Availability**:
- macOS 27.0+

## Declaration

```swift
func beginDraggingSession(items: [NSDraggingItem], gesture: NSGestureRecognizer, source: any NSDraggingSource) -> NSDraggingSession?
```

```objc
- (NSDraggingSession *) beginDraggingSessionWithItems:(NSArray<NSDraggingItem *> *) items gesture:(NSGestureRecognizer *) gesture source:(id<NSDraggingSource>) source;
```

#### Return Value

The dragging session for the drag, or `nil` if the method can’t start the session.

#### Discussion

Like [`beginDraggingSession(with:event:source:)`](./begindraggingsession%28with,event,source%29.md), this method starts an internal tracking loop. If the gesture is mouse-based, the system cancels the gesture at the end of the drag-and-drop operation. If the gesture is touch-based, the system cancels the gesture at the start of the drag-and-drop operation.

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

- `items`: The dragging items. The frame property of each [`NSDraggingItem`](../nsdraggingitem.md) must be in the view’s coordinate system.
- `gesture`: The gesture recognizer initiating the drag session.
- `source`: An object that controls the dragging operation and conforms to the [`NSDraggingSource`](../nsdraggingsource.md) protocol.

## See Also

### Related Documentation
- [func beginDraggingSession(with: [NSDraggingItem], event: NSEvent, source: any NSDraggingSource) -> NSDraggingSession](./begindraggingsession%28with,event,source%29.md)
  Initiates a dragging session with a group of dragging items.
### Dragging Operations
- [func registerForDraggedTypes([NSPasteboard.PasteboardType])](./registerfordraggedtypes%28_%29.md)
  Registers the pasteboard types that the view will accept as the destination of an image-dragging session.
- [func unregisterDraggedTypes()](./unregisterdraggedtypes%28%29.md)
  Unregisters the view as a possible destination in a dragging session.
- [var registeredDraggedTypes: [NSPasteboard.PasteboardType]](./registereddraggedtypes.md)
  The array of pasteboard drag types that the view can accept.
- [func beginDraggingSession(with: [NSDraggingItem], event: NSEvent, source: any NSDraggingSource) -> NSDraggingSession](./begindraggingsession%28with,event,source%29.md)
  Initiates a dragging session with a group of dragging items.
- [func shouldDelayWindowOrdering(for: NSEvent) -> Bool](./shoulddelaywindowordering%28for%29.md)
  Allows the user to drag objects from the view without activating the app or moving the window of the view forward, possibly obscuring the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/begindraggingsession(items:gesture:source:))*