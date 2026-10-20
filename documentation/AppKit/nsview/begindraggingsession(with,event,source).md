# beginDraggingSession(with:event:source:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Initiates a dragging session with a group of dragging items.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func beginDraggingSession(with items: [NSDraggingItem], event: NSEvent, source: any NSDraggingSource) -> NSDraggingSession
```

```objc
- (NSDraggingSession *) beginDraggingSessionWithItems:(NSArray<NSDraggingItem *> *) items event:(NSEvent *) event source:(id<NSDraggingSource>) source;
```

#### Return Value

The dragging session for the drag, , or `nil` if the method can’t start the session.

#### Discussion

A basic drag starts by calling `beginDraggingSessionWithItems:event:source:`.

The caller can take the returned [`NSDraggingSession`](../nsdraggingsession.md) and continue to modify its properties. When the drag actually starts, the source is sent a [`draggingSession(_:willBeginAt:)`](../nsdraggingsource/draggingsession%28_,willbeginat%29.md) message followed by multiple [`draggingSession(_:movedTo:)`](../nsdraggingsource/draggingsession%28_,movedto%29.md) messages as the user drags.

Once the drag is ended or cancelled, the source receives a [`draggingSession(_:endedAt:operation:)`](../nsdraggingsource/draggingsession%28_,endedat,operation%29.md) method and the drag is complete.

## Parameters

- `items`: The dragging items. The frame property of each `NSDraggingItem` must be in the view’s coordinate system.
- `event`: The mouse-down event object from which to initiate the drag operation. In particular, its mouse location is used for the offset of the icon being dragged.
- `source`: An object that serves as the controller of the dragging operation. It must conform to the [`NSDraggingSource`](../nsdraggingsource.md) protocol and is typically the view itself or its [`NSWindow`](../nswindow.md) object.

## See Also

### Dragging Operations
- [func registerForDraggedTypes([NSPasteboard.PasteboardType])](./registerfordraggedtypes%28_%29.md)
  Registers the pasteboard types that the view will accept as the destination of an image-dragging session.
- [func unregisterDraggedTypes()](./unregisterdraggedtypes%28%29.md)
  Unregisters the view as a possible destination in a dragging session.
- [var registeredDraggedTypes: [NSPasteboard.PasteboardType]](./registereddraggedtypes.md)
  The array of pasteboard drag types that the view can accept.
- [func beginDraggingSession(items: [NSDraggingItem], gesture: NSGestureRecognizer, source: any NSDraggingSource) -> NSDraggingSession?](./begindraggingsession%28items,gesture,source%29.md)
  Initiates a drag operation using a gesture recognizer.
- [func shouldDelayWindowOrdering(for: NSEvent) -> Bool](./shoulddelaywindowordering%28for%29.md)
  Allows the user to drag objects from the view without activating the app or moving the window of the view forward, possibly obscuring the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/begindraggingsession(with:event:source:))*