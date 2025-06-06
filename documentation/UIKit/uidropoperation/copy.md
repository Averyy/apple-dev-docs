# UIDropOperation.copy

**Framework**: UIKit  
**Kind**: case

A drop operation type specifying that the data represented by the drag items should be copied to the destination view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case copy
```

#### Discussion

This operation is used most often. When the user performs a drop activity, the [`dropInteraction(_:performDrop:)`](uidropinteractiondelegate/dropinteraction(_:performdrop:).md) delegate method is called. Your implementation of this delegate method should copy the data from the drag items to the destination view.

## See Also

- [UIDropOperation.cancel](uidropoperation/cancel.md)
  A drop operation type specifying that no data should be transferred, thereby canceling the drag.
- [UIDropOperation.forbidden](uidropoperation/forbidden.md)
  A drop operation type specifying that, although a move or copy operation is typically legitimate in this scenario, the drop activity isn’t allowed.
- [UIDropOperation.move](uidropoperation/move.md)
  A drop operation type specifying that the data represented by the drag items should be moved, not copied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropoperation/copy)*