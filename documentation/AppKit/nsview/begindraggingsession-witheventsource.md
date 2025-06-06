# beginDraggingSession(with:event:source:)

**Framework**: AppKit  
**Kind**: method

Initiates a dragging session with a group of dragging items.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func beginDraggingSession(with items: [NSDraggingItem], event: NSEvent, source: any NSDraggingSource) -> NSDraggingSession
```

#### Return Value

The dragging session for the drag.

#### Discussion

A basic drag starts by calling `beginDraggingSessionWithItems:event:source:`.

The caller can take the returned [`NSDraggingSession`](nsdraggingsession.md) and continue to modify its properties. When the drag actually starts, the source is sent a [`draggingSession(_:willBeginAt:)`](nsdraggingsource/draggingsession(_:willbeginat:).md) message followed by multiple [`draggingSession(_:movedTo:)`](nsdraggingsource/draggingsession(_:movedto:).md) messages as the user drags.

Once the drag is ended or cancelled, the source receives a [`draggingSession(_:endedAt:operation:)`](nsdraggingsource/draggingsession(_:endedat:operation:).md) method and the drag is complete.

## Parameters

- `items`: The dragging items. The frame property of each   must be in the view’s coordinate system.
- `event`: The mouse-down event object from which to initiate the drag operation. In particular, its mouse location is used for the offset of the icon being dragged.
- `source`: An object that serves as the controller of the dragging operation. It must conform to the   protocol and is typically the view itself or its   object.

## See Also

- [func registerForDraggedTypes([NSPasteboard.PasteboardType])](nsview/registerfordraggedtypes(_:).md)
  Registers the pasteboard types that the view will accept as the destination of an image-dragging session.
- [func unregisterDraggedTypes()](nsview/unregisterdraggedtypes.md)
  Unregisters the view as a possible destination in a dragging session.
- [var registeredDraggedTypes: [NSPasteboard.PasteboardType]](nsview/registereddraggedtypes.md)
  The array of pasteboard drag types that the view can accept.
- [func shouldDelayWindowOrdering(for: NSEvent) -> Bool](nsview/shoulddelaywindowordering(for:).md)
  Allows the user to drag objects from the view without activating the app or moving the window of the view forward, possibly obscuring the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/begindraggingsession(with:event:source:))*