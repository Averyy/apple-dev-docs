# prepareForDragOperation(_:)

**Framework**: AppKit  
**Kind**: method

Invoked when the image is released, allowing the receiver to agree to or refuse drag operation.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func prepareForDragOperation(_ sender: any NSDraggingInfo) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver agrees to perform the drag operation and [`false`](https://developer.apple.com/documentation/Swift/false) if not.

#### Discussion

This method is invoked only if the most recent [`draggingEntered(_:)`](nsdraggingdestination/draggingentered(_:).md) or [`draggingUpdated(_:)`](nsdraggingdestination/draggingupdated(_:).md) message returned an acceptable drag-operation value.

If you want the drag items to animate from their current location on screen to their final location in your view, set the sender object’s [`animatesToDestination`](nsdragginginfo/animatestodestination.md) property to [`true`](https://developer.apple.com/documentation/Swift/true) in your implementation of this method.

## Parameters

- `sender`: The object sending the message; use it to get details about the dragging operation.

## See Also

- [func performDragOperation(any NSDraggingInfo) -> Bool](nsdraggingdestination/performdragoperation(_:).md)
  Invoked after the released image has been removed from the screen, signaling the receiver to import the pasteboard data.
- [func concludeDragOperation((any NSDraggingInfo)?)](nsdraggingdestination/concludedragoperation(_:).md)
  Invoked when the dragging operation is complete, signaling the receiver to perform any necessary clean-up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingdestination/preparefordragoperation(_:))*