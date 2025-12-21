# concludeDragOperation(_:)

**Framework**: AppKit  
**Kind**: method

Invoked when the dragging operation is complete, signaling the receiver to perform any necessary clean-up.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func concludeDragOperation(_ sender: (any NSDraggingInfo)?)
```

#### Discussion

For this method to be invoked, the previous [`performDragOperation(_:)`](nsdraggingdestination/performdragoperation(_:).md) must have returned [`true`](https://developer.apple.com/documentation/Swift/true).

The destination implements this method to perform any tidying up that it needs to do, such as updating its visual representation now that it has incorporated the dragged data. This message is the last message sent from `sender` to the destination during a dragging session.

If the `sender` object’s [`animatesToDestination`](nsdragginginfo/animatestodestination.md) property was set to [`true`](https://developer.apple.com/documentation/Swift/true) in [`prepareForDragOperation(_:)`](nsdraggingdestination/preparefordragoperation(_:).md), then the drag image is still visible. At this point you should draw the final visual representation in the view. When this method returns, the drag image is removed form the screen. If your final visual representation matches the visual representation in the drag, this is a seamless transition.

## Parameters

- `sender`: The object sending the message; use it to get details about the dragging operation.

## See Also

- [func prepareForDragOperation(any NSDraggingInfo) -> Bool](nsdraggingdestination/preparefordragoperation(_:).md)
  Invoked when the image is released, allowing the receiver to agree to or refuse drag operation.
- [func performDragOperation(any NSDraggingInfo) -> Bool](nsdraggingdestination/performdragoperation(_:).md)
  Invoked after the released image has been removed from the screen, signaling the receiver to import the pasteboard data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingdestination/concludedragoperation(_:))*