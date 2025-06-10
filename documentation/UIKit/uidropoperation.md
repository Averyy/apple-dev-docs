# UIDropOperation

**Framework**: UIKit  
**Kind**: enum

Operation types that determine how a drag and drop activity resolves when the user drops a drag item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum UIDropOperation
```

## Mentions

- [Making a view into a drop destination](making-a-view-into-a-drop-destination.md)

## Topics

### Drop operation types
- [UIDropOperation.cancel](uidropoperation/cancel.md)
  A drop operation type specifying that no data should be transferred, thereby canceling the drag.
- [UIDropOperation.forbidden](uidropoperation/forbidden.md)
  A drop operation type specifying that, although a move or copy operation is typically legitimate in this scenario, the drop activity isn’t allowed.
- [UIDropOperation.copy](uidropoperation/copy.md)
  A drop operation type specifying that the data represented by the drag items should be copied to the destination view.
- [UIDropOperation.move](uidropoperation/move.md)
  A drop operation type specifying that the data represented by the drag items should be moved, not copied.
### Initializers
- [init?(rawValue: UInt)](uidropoperation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol UIDropSession](uidropsession.md)
  The interface for querying a drop session about its state and associated drag items.
- [class UIDropProposal](uidropproposal.md)
  A configuration for the behavior of a drop interaction, required if a view accepts drop activities.
- [enum UIDropSessionProgressIndicatorStyle](uidropsessionprogressindicatorstyle.md)
  The drop-progress indicator styles for the drop session, used while data is moving from the source to the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropoperation)*