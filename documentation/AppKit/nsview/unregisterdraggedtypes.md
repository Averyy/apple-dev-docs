# unregisterDraggedTypes()

**Framework**: AppKit  
**Kind**: method

Unregisters the view as a possible destination in a dragging session.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func unregisterDraggedTypes()
```

## See Also

- [func registerForDraggedTypes([NSPasteboard.PasteboardType])](nsview/registerfordraggedtypes(_:).md)
  Registers the pasteboard types that the view will accept as the destination of an image-dragging session.
- [var registeredDraggedTypes: [NSPasteboard.PasteboardType]](nsview/registereddraggedtypes.md)
  The array of pasteboard drag types that the view can accept.
- [func beginDraggingSession(with: [NSDraggingItem], event: NSEvent, source: any NSDraggingSource) -> NSDraggingSession](nsview/begindraggingsession(with:event:source:).md)
  Initiates a dragging session with a group of dragging items.
- [func shouldDelayWindowOrdering(for: NSEvent) -> Bool](nsview/shoulddelaywindowordering(for:).md)
  Allows the user to drag objects from the view without activating the app or moving the window of the view forward, possibly obscuring the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/unregisterdraggedtypes())*