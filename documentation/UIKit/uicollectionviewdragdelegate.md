# UICollectionViewDragDelegate

**Framework**: UIKit  
**Kind**: protocol

The interface for initiating drags from a collection view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UICollectionViewDragDelegate : NSObjectProtocol
```

## Mentions

- [Supporting Drag and Drop in Collection Views](supporting-drag-and-drop-in-collection-views.md)

#### Overview

Implement this protocol in the object that you use to initiate drags from your collection view. The only required method of this protocol is the [`collectionView(_:itemsForBeginning:at:)`](uicollectionviewdragdelegate/collectionview(_:itemsforbeginning:at:).md) method, but you can implement other methods as needed to customize the drag behavior of your collection view.

Assign your custom delegate object to the [`dragDelegate`](uicollectionview/dragdelegate.md) property of your collection view.

## Topics

### Providing the items to drag
- [func collectionView(UICollectionView, itemsForBeginning: any UIDragSession, at: IndexPath) -> [UIDragItem]](uicollectionviewdragdelegate/collectionview(_:itemsforbeginning:at:).md)
  Provides the initial set of items (if any) to drag.
- [func collectionView(UICollectionView, itemsForAddingTo: any UIDragSession, at: IndexPath, point: CGPoint) -> [UIDragItem]](uicollectionviewdragdelegate/collectionview(_:itemsforaddingto:at:point:).md)
  Adds the specified items to an existing drag session.
### Tracking the drag session
- [func collectionView(UICollectionView, dragSessionWillBegin: any UIDragSession)](uicollectionviewdragdelegate/collectionview(_:dragsessionwillbegin:).md)
  Notifies you that a drag session is about to begin for the collection view.
- [func collectionView(UICollectionView, dragSessionDidEnd: any UIDragSession)](uicollectionviewdragdelegate/collectionview(_:dragsessiondidend:).md)
  Notifies you that a drag session ended for the collection view.
### Providing a custom preview
- [func collectionView(UICollectionView, dragPreviewParametersForItemAt: IndexPath) -> UIDragPreviewParameters?](uicollectionviewdragdelegate/collectionview(_:dragpreviewparametersforitemat:).md)
  Returns custom information about how to display the item at the specified location during the drag.
### Controlling the drag session
- [func collectionView(UICollectionView, dragSessionAllowsMoveOperation: any UIDragSession) -> Bool](uicollectionviewdragdelegate/collectionview(_:dragsessionallowsmoveoperation:).md)
  Returns a Boolean value that determines whether a move operation is allowed for a drag session.
- [func collectionView(UICollectionView, dragSessionIsRestrictedToDraggingApplication: any UIDragSession) -> Bool](uicollectionviewdragdelegate/collectionview(_:dragsessionisrestrictedtodraggingapplication:).md)
  Returns a Boolean value that determines whether the source app and destination app must be the same for a drag session.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Supporting Drag and Drop in Collection Views](supporting-drag-and-drop-in-collection-views.md)
  Initiate drags and handle drops from a collection view.
- [protocol UICollectionViewDropDelegate](uicollectionviewdropdelegate.md)
  The interface for handling drops in a collection view.
- [protocol UICollectionViewDropCoordinator](uicollectionviewdropcoordinator.md)
  An interface for coordinating your custom drop-related actions with the collection view.
- [class UICollectionViewDropPlaceholder](uicollectionviewdropplaceholder.md)
  A placeholder for an item dropped on a collection view.
- [class UICollectionViewDropProposal](uicollectionviewdropproposal.md)
  Your proposed solution for handling a drop in a collection view.
- [protocol UICollectionViewDropItem](uicollectionviewdropitem.md)
  The data associated with an item being dropped into the collection view.
- [protocol UICollectionViewDropPlaceholderContext](uicollectionviewdropplaceholdercontext.md)
  An object that contains information about a placeholder in the collection view.
- [protocol UIDataSourceTranslating](uidatasourcetranslating.md)
  An advanced interface for managing a data source object.
- [class UICollectionViewPlaceholder](uicollectionviewplaceholder.md)
  A placeholder for an item dragged or dropped on a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdragdelegate)*