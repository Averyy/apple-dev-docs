# collectionView(_:moveItemAt:to:)

**Framework**: UIKit  
**Kind**: method

Tells your data source object to move the specified item to its new location.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, moveItemAt sourceIndexPath: IndexPath, to destinationIndexPath: IndexPath)
```

#### Discussion

You must implement this method to support the reordering of items within the collection view. If you don’t implement this method, the collection view ignores any attempts to reorder items.

When interactions with an item end, the collection view calls this method if the position of the item changed. Use this method to update your data structures with the new index path information.

## Parameters

- `collectionView`: The collection view notifying you of the move.
- `sourceIndexPath`: The item’s original index path.
- `destinationIndexPath`: The new index path of the item.

## See Also

- [func collectionView(UICollectionView, canMoveItemAt: IndexPath) -> Bool](uicollectionviewdatasource/collectionview(_:canmoveitemat:).md)
  Asks your data source object whether the specified item can move to another location in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/collectionview(_:moveitemat:to:))*