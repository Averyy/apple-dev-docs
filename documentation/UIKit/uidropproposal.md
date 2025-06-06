# UIDropProposal

**Framework**: UIKit  
**Kind**: class

A configuration for the behavior of a drop interaction, required if a view accepts drop activities.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIDropProposal
```

## Mentions

- [Making a view into a drop destination](making-a-view-into-a-drop-destination.md)

#### Overview

If a view’s drop interaction delegate accepts dropped drag items, it must return a drop proposal in its implementation of the [`dropInteraction(_:sessionDidUpdate:)`](uidropinteractiondelegate/dropinteraction(_:sessiondidupdate:).md) method.

## Topics

### Initializing a drop proposal
- [init(operation: UIDropOperation)](uidropproposal/init(operation:).md)
  Initializes a new drop proposal with a drop operation type.
- [var operation: UIDropOperation](uidropproposal/operation.md)
  The drop operation that the drop interaction proposes to perform.
### Configuring a drop proposal
- [var isPrecise: Bool](uidropproposal/isprecise.md)
  A Boolean value that proposes that the drop interaction define the drop location precisely, such as at a specific point within existing text.
- [var prefersFullSizePreview: Bool](uidropproposal/prefersfullsizepreview.md)
  A Boolean value that indicates that the drag item preview should be shown at its full, original size.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UICollectionViewDropProposal](uicollectionviewdropproposal.md)
- [UITableViewDropProposal](uitableviewdropproposal.md)
- [UITextDropProposal](uitextdropproposal.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol UIDropSession](uidropsession.md)
  The interface for querying a drop session about its state and associated drag items.
- [enum UIDropOperation](uidropoperation.md)
  Operation types that determine how a drag and drop activity resolves when the user drops a drag item.
- [enum UIDropSessionProgressIndicatorStyle](uidropsessionprogressindicatorstyle.md)
  The drop-progress indicator styles for the drop session, used while data is moving from the source to the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropproposal)*