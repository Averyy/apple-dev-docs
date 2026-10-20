# unregisterDraggedTypes()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Unregisters the view as a possible destination in a dragging session.

**Availability**:
- macOS

## Declaration

```swift
func unregisterDraggedTypes()
```

```objc
- (void) unregisterDraggedTypes;
```

## See Also

### Dragging Operations
- [func registerForDraggedTypes([NSPasteboard.PasteboardType])](./registerfordraggedtypes%28_%29.md)
  Registers the pasteboard types that the view will accept as the destination of an image-dragging session.
- [var registeredDraggedTypes: [NSPasteboard.PasteboardType]](./registereddraggedtypes.md)
  The array of pasteboard drag types that the view can accept.
- [func beginDraggingSession(with: [NSDraggingItem], event: NSEvent, source: any NSDraggingSource) -> NSDraggingSession](./begindraggingsession%28with,event,source%29.md)
  Initiates a dragging session with a group of dragging items.
- [func beginDraggingSession(items: [NSDraggingItem], gesture: NSGestureRecognizer, source: any NSDraggingSource) -> NSDraggingSession?](./begindraggingsession%28items,gesture,source%29.md)
  Initiates a drag operation using a gesture recognizer.
- [func shouldDelayWindowOrdering(for: NSEvent) -> Bool](./shoulddelaywindowordering%28for%29.md)
  Allows the user to drag objects from the view without activating the app or moving the window of the view forward, possibly obscuring the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/unregisterdraggedtypes())*