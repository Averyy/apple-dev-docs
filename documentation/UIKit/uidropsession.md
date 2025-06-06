# UIDropSession

**Framework**: UIKit  
**Kind**: protocol

The interface for querying a drop session about its state and associated drag items.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIDropSession : ProgressReporting, UIDragDropSession
```

## Mentions

- [Making a view into a drop destination](making-a-view-into-a-drop-destination.md)

## Topics

### Getting the drag session
- [var localDragSession: (any UIDragSession)?](uidropsession/localdragsession.md)
  The drag session that corresponds to this drop session, for in-app drag activities.
### Loading objects
- [func loadObjects(ofClass: any NSItemProviderReading.Type, completion: ([any NSItemProviderReading]) -> Void) -> Progress](uidropsession/loadobjects(ofclass:completion:).md)
  Creates and loads a new instance of the specified class for each drag item in the session.
### Showing a progress indicator
- [var progressIndicatorStyle: UIDropSessionProgressIndicatorStyle](uidropsession/progressindicatorstyle.md)
  The drop-progress indicator style associated with the drop session.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [ProgressReporting](../Foundation/ProgressReporting.md)
- [UIDragDropSession](uidragdropsession.md)

## See Also

- [class UIDropProposal](uidropproposal.md)
  A configuration for the behavior of a drop interaction, required if a view accepts drop activities.
- [enum UIDropOperation](uidropoperation.md)
  Operation types that determine how a drag and drop activity resolves when the user drops a drag item.
- [enum UIDropSessionProgressIndicatorStyle](uidropsessionprogressindicatorstyle.md)
  The drop-progress indicator styles for the drop session, used while data is moving from the source to the destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropsession)*