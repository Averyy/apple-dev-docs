# UICollectionViewDropCoordinator

**Framework**: UIKit  
**Kind**: protocol

An interface for coordinating your custom drop-related actions with the collection view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UICollectionViewDropCoordinator : NSObjectProtocol
```

## Mentions

- [Supporting Drag and Drop in Collection Views](supporting-drag-and-drop-in-collection-views.md)

#### Overview

You don’t create instances of this class yourself. When a drop occurs in the collection view, UIKit creates an instance of this class and passes it to your [`collectionView(_:performDropWith:)`](uicollectionviewdropdelegate/collectionview(_:performdropwith:).md) method. Use the object to let the collection view know how you want to animate the dropped items into position.

## Topics

### Getting the Dragged Items
- [var items: [any UICollectionViewDropItem]](uicollectionviewdropcoordinator/items.md)
  The items being dragged.
### Getting the Drop Location
- [var destinationIndexPath: IndexPath?](uicollectionviewdropcoordinator/destinationindexpath.md)
  The index path at which to insert the item in the collection view.
### Animating Items to Their Destination
- [func drop(UIDragItem, toItemAt: IndexPath) -> any UIDragAnimating](uicollectionviewdropcoordinator/drop(_:toitemat:).md)
  Animates the item to the specified index path in the collection view.
- [func drop(UIDragItem, intoItemAt: IndexPath, rect: CGRect) -> any UIDragAnimating](uicollectionviewdropcoordinator/drop(_:intoitemat:rect:).md)
  Animates the item to the specified rectangle in the collection view.
- [func drop(UIDragItem, to: UIDragPreviewTarget) -> any UIDragAnimating](uicollectionviewdropcoordinator/drop(_:to:)-7w5rn.md)
  Animates the item to an arbitrary location in your view hierarchy.
- [func drop(UIDragItem, to: UICollectionViewDropPlaceholder) -> any UICollectionViewDropPlaceholderContext](uicollectionviewdropcoordinator/drop(_:to:)-l5tg.md)
  Animates the item to the specified location and inserts a placeholder cell at that location.
### Getting the Session Information
- [var session: any UIDropSession](uicollectionviewdropcoordinator/session.md)
  The drop session containing information about the transaction.
- [var proposal: UICollectionViewDropProposal](uicollectionviewdropcoordinator/proposal.md)
  The current proposal for how to incorporate the dropped items.

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropcoordinator)*