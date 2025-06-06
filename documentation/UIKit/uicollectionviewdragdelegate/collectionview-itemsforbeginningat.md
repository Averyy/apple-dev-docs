# collectionView(_:itemsForBeginning:at:)

**Framework**: UIKit  
**Kind**: method  
**Required**: Yes

Provides the initial set of items (if any) to drag.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func collectionView(_ collectionView: UICollectionView, itemsForBeginning session: any UIDragSession, at indexPath: IndexPath) -> [UIDragItem]
```

## Mentions

- [Supporting Drag and Drop in Collection Views](supporting-drag-and-drop-in-collection-views.md)

#### Return Value

An array of [`UIDragItem`](uidragitem.md) objects containing the details of the items to drag. Return an empty array to prevent the item from being dragged.

#### Discussion

You must implement this method to allow the dragging of items from your collection view. In your implementation, create one or more [`UIDragItem`](uidragitem.md) objects for the item at the specified `indexPath`. Normally, you return only one drag item, but if the specified item has children or can’t be dragged without one or more associated items, include those items as well.

The collection view calls this method one or more times when a new drag begins within its bounds. Specifically, if the user begins the drag from a selected item, the collection view calls this method once for each item that’s part of the selection. If the user begins the drag from an unselected item, the collection view calls the method only once for that item.

## Parameters

- `collectionView`: The collection view from which the drag operation originated.
- `session`: The current drag session object.
- `indexPath`: The index path of the item to drag.

## See Also

- [func collectionView(UICollectionView, itemsForAddingTo: any UIDragSession, at: IndexPath, point: CGPoint) -> [UIDragItem]](uicollectionviewdragdelegate/collectionview(_:itemsforaddingto:at:point:).md)
  Adds the specified items to an existing drag session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdragdelegate/collectionview(_:itemsforbeginning:at:))*