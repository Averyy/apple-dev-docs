# UIDropOperation.cancel

**Framework**: UIKit  
**Kind**: case  
**Role**: Case

A drop operation type specifying that no data should be transferred, thereby canceling the drag.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case cancel
```

```c
UIDropOperationCancel
```

## Mentions

- [Making a view into a drop destination](../making-a-view-into-a-drop-destination.md)

## Discussion

If the user attempts a drop activity, the drag operation is canceled and the [`dropInteraction(_:performDrop:)`](../uidropinteractiondelegate/dropinteraction%28_,performdrop%29.md) delegate method isn’t called.

## See Also

### Drop operation types
- [UIDropOperation.forbidden](./forbidden.md)
  A drop operation type specifying that, although a move or copy operation is typically legitimate in this scenario, the drop activity isn’t allowed.
- [UIDropOperation.copy](./copy.md)
  A drop operation type specifying that the data represented by the drag items should be copied to the destination view.
- [UIDropOperation.move](./move.md)
  A drop operation type specifying that the data represented by the drag items should be moved, not copied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropoperation/cancel)*