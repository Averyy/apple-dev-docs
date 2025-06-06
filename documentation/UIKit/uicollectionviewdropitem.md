# UICollectionViewDropItem

**Framework**: UIKit  
**Kind**: protocol

The data associated with an item being dropped into the collection view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UICollectionViewDropItem : NSObjectProtocol
```

#### Overview

When handling a drop, you get instances of this class from the [`items`](uicollectionviewdropcoordinator/items.md) property of the [`UICollectionViewDropCoordinator`](uicollectionviewdropcoordinator.md) object. Use them to retrieve the data for the items being dragged and to plan any animations related to dropping the items. You do not create instances of this class yourself.

## Topics

### Getting the Drag Item
- [var dragItem: UIDragItem](uicollectionviewdropitem/dragitem.md)
  The item that was dragged.
### Getting the Item Information
- [var previewSize: CGSize](uicollectionviewdropitem/previewsize.md)
  The size of the drag item’s preview.
- [var sourceIndexPath: IndexPath?](uicollectionviewdropitem/sourceindexpath.md)
  The index path of the item in the collection view, if any.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

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
- [protocol UICollectionViewDropPlaceholderContext](uicollectionviewdropplaceholdercontext.md)
  An object that contains information about a placeholder in the collection view.
- [protocol UIDataSourceTranslating](uidatasourcetranslating.md)
  An advanced interface for managing a data source object.
- [class UICollectionViewPlaceholder](uicollectionviewplaceholder.md)
  A placeholder for an item dragged or dropped on a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropitem)*