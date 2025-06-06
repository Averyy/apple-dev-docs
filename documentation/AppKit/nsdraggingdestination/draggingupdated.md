# draggingUpdated(_:)

**Framework**: AppKit  
**Kind**: method

Invoked periodically as the image is held within the destination area, allowing modification of the dragging operation or mouse-pointer position.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func draggingUpdated(_ sender: any NSDraggingInfo) -> NSDragOperation
```

#### Return Value

One (and only one) of the dragging operation constants described  in [`NSDragOperation`](nsdragoperation.md) in the [`NSDraggingInfo`](nsdragginginfo.md) reference. The default return value (if this method is not implemented by the destination) is the value returned by the previous [`draggingEntered(_:)`](nsdraggingdestination/draggingentered(_:).md) message.

#### Discussion

For this to be invoked, the destination must have registered for the pasteboard data type involved in the drag operation. The messages continue until the image is either released or dragged out of the window or view.

This method provides the destination with an opportunity to modify the dragging operation depending on the position of the mouse pointer inside of the destination view or window object. For example, you may have several graphics or areas of text contained within the same view and wish to tailor the dragging operation, or to ignore the drag event completely, depending upon which object is underneath the mouse pointer at the time when the user releases the dragged image and the [`performDragOperation(_:)`](nsdraggingdestination/performdragoperation(_:).md) method is invoked.

You typically examine the contents of the pasteboard in the [`draggingEntered(_:)`](nsdraggingdestination/draggingentered(_:).md) method, where this examination is performed only once, rather than in the [`draggingUpdated(_:)`](nsdraggingdestination/draggingupdated(_:).md) method, which is invoked multiple times.

Only one destination at a time receives a sequence of [`draggingUpdated(_:)`](nsdraggingdestination/draggingupdated(_:).md) messages. If the mouse pointer is within the bounds of two overlapping views that are both valid destinations, the uppermost view receives these messages until the image is either released or dragged out.

## Parameters

- `sender`: The object sending the message; use it to get details about the dragging operation.

## See Also

- [func prepareForDragOperation(any NSDraggingInfo) -> Bool](nsdraggingdestination/preparefordragoperation(_:).md)
  Invoked when the image is released, allowing the receiver to agree to or refuse drag operation.
- [func draggingEntered(any NSDraggingInfo) -> NSDragOperation](nsdraggingdestination/draggingentered(_:).md)
  Invoked when the dragged image enters destination bounds or frame; delegate returns dragging operation to perform.
- [func wantsPeriodicDraggingUpdates() -> Bool](nsdraggingdestination/wantsperiodicdraggingupdates.md)
  Asks the destination object whether it wants to receive periodic [`draggingUpdated(_:)`](nsdraggingdestination/draggingupdated(_:).md) messages.
- [func draggingExited((any NSDraggingInfo)?)](nsdraggingdestination/draggingexited(_:).md)
  Invoked when the dragged image exits the destination’s bounds rectangle (in the case of a view object) or its frame rectangle (in the case of a window object).
- [func draggingEnded(any NSDraggingInfo)](nsdraggingdestination/draggingended(_:).md)
  Called when a drag operation ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingdestination/draggingupdated(_:))*