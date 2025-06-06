# UICollectionViewDropPlaceholderContext

**Framework**: UIKit  
**Kind**: protocol

An object that contains information about a placeholder in the collection view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UICollectionViewDropPlaceholderContext : UIDragAnimating
```

#### Overview

You do not create instances of this class yourself. For each placeholder cell that you insert into the collection view, the drop coordinator provides you with an instance of this class. You use this context object later to remove the placeholder cell, either by committing the actual data to your data source object or by deleting the placeholder cell.

## Topics

### Updating the Placeholder Cell
- [func commitInsertion(dataSourceUpdates: (IndexPath) -> Void) -> Bool](uicollectionviewdropplaceholdercontext/commitinsertion(datasourceupdates:).md)
  Exchanges the placeholder cell for a cell with the final content.
- [func setNeedsCellUpdate()](uicollectionviewdropplaceholdercontext/setneedscellupdate.md)
  Updates the contents of the placeholder cell.
### Removing the Placeholder Cell
- [func deletePlaceholder() -> Bool](uicollectionviewdropplaceholdercontext/deleteplaceholder.md)
  Removes an unneeded placeholder cell altogether from the collection view.
### Getting the Drag Item
- [var dragItem: UIDragItem](uicollectionviewdropplaceholdercontext/dragitem.md)
  The drag item being represented by the placeholder cell.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIDragAnimating](uidraganimating.md)

## See Also

- [Supporting Drag and Drop in Collection Views](supporting-drag-and-drop-in-collection-views.md)
  Initiate drags and handle drops from a collection view.
- [protocol UICollectionViewDragDelegate](uicollectionviewdragdelegate.md)
  The interface for initiating drags from a collection view.
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
- [protocol UIDataSourceTranslating](uidatasourcetranslating.md)
  An advanced interface for managing a data source object.
- [class UICollectionViewPlaceholder](uicollectionviewplaceholder.md)
  A placeholder for an item dragged or dropped on a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropplaceholdercontext)*