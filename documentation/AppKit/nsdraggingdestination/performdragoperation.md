# performDragOperation(_:)

**Framework**: AppKit  
**Kind**: method

Invoked after the released image has been removed from the screen, signaling the receiver to import the pasteboard data.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func performDragOperation(_ sender: any NSDraggingInfo) -> Bool
```

#### Return Value

If the destination accepts the data, it returns [`true`](https://developer.apple.com/documentation/Swift/true); otherwise it returns [`false`](https://developer.apple.com/documentation/Swift/false). The default is to return [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

For this method to be invoked, the previous [`prepareForDragOperation(_:)`](nsdraggingdestination/preparefordragoperation(_:).md) message must have returned [`true`](https://developer.apple.com/documentation/Swift/true). The destination should implement this method to do the real work of importing the pasteboard data represented by the image.

If the sender object’s [`animatesToDestination`](nsdragginginfo/animatestodestination.md) was set to [`true`](https://developer.apple.com/documentation/Swift/true) in [`prepareForDragOperation(_:)`](nsdraggingdestination/preparefordragoperation(_:).md), then setup any animation to arrange space for the drag items to animate to. Also at this time, enumerate through the dragging items to set their destination frames and destination images.

## Parameters

- `sender`: The object sending the message; use it to get details about the dragging operation.

## See Also

- [func prepareForDragOperation(any NSDraggingInfo) -> Bool](nsdraggingdestination/preparefordragoperation(_:).md)
  Invoked when the image is released, allowing the receiver to agree to or refuse drag operation.
- [func concludeDragOperation((any NSDraggingInfo)?)](nsdraggingdestination/concludedragoperation(_:).md)
  Invoked when the dragging operation is complete, signaling the receiver to perform any necessary clean-up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingdestination/performdragoperation(_:))*