# UICollectionViewDropDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

The interface for handling drops in a collection view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UICollectionViewDropDelegate : NSObjectProtocol
```

```objc
@protocol UICollectionViewDropDelegate <NSObject>
```

## Mentions

- [Supporting Drag and Drop in Collection Views](./supporting-drag-and-drop-in-collection-views.md)

#### Overview

Implement this protocol in the object that you use to incorporate dropped data into your collection view. The only required method of this protocol is the [`collectionView(_:performDropWith:)`](./uicollectionviewdropdelegate/collectionview%28_,performdropwith%29.md) method, but you can implement other methods as needed to customize the drop behavior of your collection view.

Assign your custom delegate object to the [`dropDelegate`](./uicollectionview/dropdelegate.md) property of your collection view.

## Topics

### Declaring support for handling drops
- [func collectionView(UICollectionView, canHandle: any UIDropSession) -> Bool](./uicollectionviewdropdelegate/collectionview%28_,canhandle%29.md)
  Asks your delegate whether the collection view can accept a drop with the specified type of data.
### Incorporating the dropped data
- [func collectionView(UICollectionView, performDropWith: any UICollectionViewDropCoordinator)](./uicollectionviewdropdelegate/collectionview%28_,performdropwith%29.md)
  Tells your delegate to incorporate the drop data into the collection view.
### Tracking the drag movements
- [func collectionView(UICollectionView, dropSessionDidUpdate: any UIDropSession, withDestinationIndexPath: IndexPath?) -> UICollectionViewDropProposal](./uicollectionviewdropdelegate/collectionview%28_,dropsessiondidupdate,withdestinationindexpath%29.md)
  Tells your delegate that the position of the dragged data over the collection view changed.
- [func collectionView(UICollectionView, dropSessionDidEnter: any UIDropSession)](./uicollectionviewdropdelegate/collectionview%28_,dropsessiondidenter%29.md)
  Notifies you when dragged content enters the collection view’s bounds rectangle.
- [func collectionView(UICollectionView, dropSessionDidExit: any UIDropSession)](./uicollectionviewdropdelegate/collectionview%28_,dropsessiondidexit%29.md)
  Notifies you when dragged content exits the collection view’s bounds rectangle.
- [func collectionView(UICollectionView, dropSessionDidEnd: any UIDropSession)](./uicollectionviewdropdelegate/collectionview%28_,dropsessiondidend%29.md)
  Notifies you when the drag operation ends.
### Providing a custom preview
- [func collectionView(UICollectionView, dropPreviewParametersForItemAt: IndexPath) -> UIDragPreviewParameters?](./uicollectionviewdropdelegate/collectionview%28_,droppreviewparametersforitemat%29.md)
  Returns custom information about how to display the item at the specified location during the drop.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Drag and drop
- [Supporting Drag and Drop in Collection Views](./supporting-drag-and-drop-in-collection-views.md)
  Initiate drags and handle drops from a collection view.
- [protocol UICollectionViewDragDelegate](./uicollectionviewdragdelegate.md)
  The interface for initiating drags from a collection view.
- [protocol UICollectionViewDropCoordinator](./uicollectionviewdropcoordinator.md)
  An interface for coordinating your custom drop-related actions with the collection view.
- [class UICollectionViewDropPlaceholder](./uicollectionviewdropplaceholder.md)
  A placeholder for an item dropped on a collection view.
- [class UICollectionViewDropProposal](./uicollectionviewdropproposal.md)
  Your proposed solution for handling a drop in a collection view.
- [protocol UICollectionViewDropItem](./uicollectionviewdropitem.md)
  The data associated with an item being dropped into the collection view.
- [protocol UICollectionViewDropPlaceholderContext](./uicollectionviewdropplaceholdercontext.md)
  An object that contains information about a placeholder in the collection view.
- [protocol UIDataSourceTranslating](./uidatasourcetranslating.md)
  An advanced interface for managing a data source object.
- [class UICollectionViewPlaceholder](./uicollectionviewplaceholder.md)
  A placeholder for an item dragged or dropped on a collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropdelegate)*