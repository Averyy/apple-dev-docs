# performDragOperation(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked after the released image has been removed from the screen, signaling the receiver to import the pasteboard data.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func performDragOperation(_ sender: any NSDraggingInfo) -> Bool
```

```objc
- (BOOL) performDragOperation:(id<NSDraggingInfo>) sender;
```

#### Return Value

If the destination accepts the data, it returns [`true`](../../Swift/true.md); otherwise it returns [`false`](../../Swift/false.md). The default is to return [`false`](../../Swift/false.md).

#### Discussion

For this method to be invoked, the previous [`prepareForDragOperation(_:)`](./preparefordragoperation%28_%29.md) message must have returned [`true`](../../Swift/true.md). The destination should implement this method to do the real work of importing the pasteboard data represented by the image.

If the sender object’s [`animatesToDestination`](../nsdragginginfo/animatestodestination.md) was set to [`true`](../../Swift/true.md) in [`prepareForDragOperation(_:)`](./preparefordragoperation%28_%29.md), then setup any animation to arrange space for the drag items to animate to. Also at this time, enumerate through the dragging items to set their destination frames and destination images.

## Parameters

- `sender`: The object sending the message; use it to get details about the dragging operation.

## See Also

### Managing a Dragging Session After an Image Is Released
- [func prepareForDragOperation(any NSDraggingInfo) -> Bool](./preparefordragoperation%28_%29.md)
  Invoked when the image is released, allowing the receiver to agree to or refuse drag operation.
- [func concludeDragOperation((any NSDraggingInfo)?)](./concludedragoperation%28_%29.md)
  Invoked when the dragging operation is complete, signaling the receiver to perform any necessary clean-up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingdestination/performdragoperation(_:))*