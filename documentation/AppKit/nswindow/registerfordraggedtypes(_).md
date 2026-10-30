# registerForDraggedTypes(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Registers a set of pasteboard types that the window accepts as the destination of an image-dragging session.

**Availability**:
- macOS

## Declaration

```swift
func registerForDraggedTypes(_ newTypes: [NSPasteboard.PasteboardType])
```

```objc
- (void) registerForDraggedTypes:(NSArray<NSString *> *) newTypes;
```

## Discussion

Registering an `NSWindow` object for dragged types automatically makes it a candidate destination object for a dragging session. `NSWindow` has a default implementation for many of the methods in the [`NSDraggingDestination`](../nsdraggingdestination.md) protocol. The default implementation forwards each message to the delegate if the delegate responds to the selector of the message. The messages forwarded this way are [`draggingEntered(_:)`](../nsdraggingdestination/draggingentered%28_%29.md), [`draggingUpdated(_:)`](../nsdraggingdestination/draggingupdated%28_%29.md), [`draggingExited(_:)`](../nsdraggingdestination/draggingexited%28_%29.md), [`prepareForDragOperation(_:)`](../nsdraggingdestination/preparefordragoperation%28_%29.md), [`performDragOperation(_:)`](../nsdraggingdestination/performdragoperation%28_%29.md), and [`concludeDragOperation(_:)`](../nsdraggingdestination/concludedragoperation%28_%29.md).

## Parameters

- `newTypes`: An array of the pasteboard types the window accepts as the destination of an image-dragging session.

## See Also

### Dragging Items
- [func beginDraggingSession(items: [NSDraggingItem], event: NSEvent, source: any NSDraggingSource) -> NSDraggingSession](./begindraggingsession%28items,event,source%29.md)
- [func unregisterDraggedTypes()](./unregisterdraggedtypes%28%29.md)
  Unregisters the window as a possible destination for dragging operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/registerfordraggedtypes(_:))*