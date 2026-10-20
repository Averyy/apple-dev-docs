# prepareForDragOperation(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when the image is released, allowing the receiver to agree to or refuse drag operation.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func prepareForDragOperation(_ sender: any NSDraggingInfo) -> Bool
```

```objc
- (BOOL) prepareForDragOperation:(id<NSDraggingInfo>) sender;
```

#### Return Value

[`true`](../../Swift/true.md) if the receiver agrees to perform the drag operation and [`false`](../../Swift/false.md) if not.

#### Discussion

This method is invoked only if the most recent [`draggingEntered(_:)`](./draggingentered%28_%29.md) or [`draggingUpdated(_:)`](./draggingupdated%28_%29.md) message returned an acceptable drag-operation value.

If you want the drag items to animate from their current location on screen to their final location in your view, set the sender object’s [`animatesToDestination`](../nsdragginginfo/animatestodestination.md) property to [`true`](../../Swift/true.md) in your implementation of this method.

## Parameters

- `sender`: The object sending the message; use it to get details about the dragging operation.

## See Also

### Managing a Dragging Session After an Image Is Released
- [func performDragOperation(any NSDraggingInfo) -> Bool](./performdragoperation%28_%29.md)
  Invoked after the released image has been removed from the screen, signaling the receiver to import the pasteboard data.
- [func concludeDragOperation((any NSDraggingInfo)?)](./concludedragoperation%28_%29.md)
  Invoked when the dragging operation is complete, signaling the receiver to perform any necessary clean-up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingdestination/preparefordragoperation(_:))*