# draggingEntered(_:)

**Framework**: AppKit  
**Kind**: method

Invoked when the dragged image enters destination bounds or frame; delegate returns dragging operation to perform.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func draggingEntered(_ sender: any NSDraggingInfo) -> NSDragOperation
```

#### Return Value

One (and only one) of the dragging operation constants described  in [`NSDragOperation`](nsdragoperation.md) in the [`NSDraggingInfo`](nsdragginginfo.md) reference. The default return value (if this method is not implemented by the destination) is the value returned by the previous [`draggingEntered(_:)`](nsdraggingdestination/draggingentered(_:).md) message.

#### Discussion

Invoked when a dragged image enters the destination but only if the destination has registered for the pasteboard data type involved in the drag operation. Specifically, this method is invoked when the mouse pointer enters the destination’s bounds rectangle (if it is a view object) or its frame rectangle (if it is a window object).

This method must return a value that indicates which dragging operation the destination will perform when the image is released. In deciding which dragging operation to return, the method should evaluate the overlap between both the dragging operations allowed by the source (obtained from `sender` with the [`draggingSourceOperationMask`](nsdragginginfo/draggingsourceoperationmask.md) method) and the dragging operations and pasteboard data types the destination itself supports.

If none of the operations is appropriate, this method should return `NSDragOperationNone` (this is the default response if the method is not implemented by the destination). A destination will still receive [`draggingUpdated(_:)`](nsdraggingdestination/draggingupdated(_:).md) and [`draggingExited(_:)`](nsdraggingdestination/draggingexited(_:).md) even if `NSDragOperationNone` is returned by this method.

## Parameters

- `sender`: The object sending the message; use it to get details about the dragging operation.

## See Also

- [Drag and Drop Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DragandDrop/DragandDrop.html#//apple_ref/doc/uid/10000069i)
- [func prepareForDragOperation(any NSDraggingInfo) -> Bool](nsdraggingdestination/preparefordragoperation(_:).md)
  Invoked when the image is released, allowing the receiver to agree to or refuse drag operation.
- [func wantsPeriodicDraggingUpdates() -> Bool](nsdraggingdestination/wantsperiodicdraggingupdates.md)
  Asks the destination object whether it wants to receive periodic [`draggingUpdated(_:)`](nsdraggingdestination/draggingupdated(_:).md) messages.
- [func draggingUpdated(any NSDraggingInfo) -> NSDragOperation](nsdraggingdestination/draggingupdated(_:).md)
  Invoked periodically as the image is held within the destination area, allowing modification of the dragging operation or mouse-pointer position.
- [func draggingExited((any NSDraggingInfo)?)](nsdraggingdestination/draggingexited(_:).md)
  Invoked when the dragged image exits the destination’s bounds rectangle (in the case of a view object) or its frame rectangle (in the case of a window object).
- [func draggingEnded(any NSDraggingInfo)](nsdraggingdestination/draggingended(_:).md)
  Called when a drag operation ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingdestination/draggingentered(_:))*