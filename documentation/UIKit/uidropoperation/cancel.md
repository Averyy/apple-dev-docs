# UIDropOperation.cancel

**Framework**: UIKit  
**Kind**: case

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

## Mentions

- [Making a view into a drop destination](making-a-view-into-a-drop-destination.md)

#### Discussion

If the user attempts a drop activity, the drag operation is canceled and the [`dropInteraction(_:performDrop:)`](uidropinteractiondelegate/dropinteraction(_:performdrop:).md) delegate method isn’t called.

## See Also

- [UIDropOperation.forbidden](uidropoperation/forbidden.md)
  A drop operation type specifying that, although a move or copy operation is typically legitimate in this scenario, the drop activity isn’t allowed.
- [UIDropOperation.copy](uidropoperation/copy.md)
  A drop operation type specifying that the data represented by the drag items should be copied to the destination view.
- [UIDropOperation.move](uidropoperation/move.md)
  A drop operation type specifying that the data represented by the drag items should be moved, not copied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropoperation/cancel)*