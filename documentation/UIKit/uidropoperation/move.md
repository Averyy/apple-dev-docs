# UIDropOperation.move

**Framework**: UIKit  
**Kind**: case

A drop operation type specifying that the data represented by the drag items should be moved, not copied.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case move
```

#### Discussion

You may use this operation only if the drop session’s [`allowsMoveOperation`](uidragdropsession/allowsmoveoperation.md) property is [`true`](https://developer.apple.com/documentation/swift/true); otherwise, it’s treated as a [`UIDropOperation.cancel`](uidropoperation/cancel.md) operation. A move operation is allowed only within same app. Data shared with another app must be copied.

The system gives no special meaning to this operation. The [`UIDragInteractionDelegate`](uidraginteractiondelegate.md) object and the [`UIDropInteractionDelegate`](uidropinteractiondelegate.md) object must cooperate to produce the correct move results. For instance, the drop interaction delegate might insert the data in a new location while the drag interaction delegate removes the data from the old location.

## See Also

- [UIDropOperation.cancel](uidropoperation/cancel.md)
  A drop operation type specifying that no data should be transferred, thereby canceling the drag.
- [UIDropOperation.forbidden](uidropoperation/forbidden.md)
  A drop operation type specifying that, although a move or copy operation is typically legitimate in this scenario, the drop activity isn’t allowed.
- [UIDropOperation.copy](uidropoperation/copy.md)
  A drop operation type specifying that the data represented by the drag items should be copied to the destination view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropoperation/move)*