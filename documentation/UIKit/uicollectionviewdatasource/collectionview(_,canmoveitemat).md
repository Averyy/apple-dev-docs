# collectionView(_:canMoveItemAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks your data source object whether the specified item can move to another location in the collection view.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func collectionView(_ collectionView: UICollectionView, canMoveItemAt indexPath: IndexPath) -> Bool
```

```objc
- (BOOL) collectionView:(UICollectionView *) collectionView canMoveItemAtIndexPath:(NSIndexPath *) indexPath;
```

## Return Value

[`true`](../../Swift/true.md) if the item is allowed to move, or [`false`](../../Swift/false.md) if it isn’t.

## Discussion

Use this method to selectively allow or disallow the movement of items within a collection view. If you don’t implement this method, but you do implement the [`collectionView(_:moveItemAt:to:)`](./collectionview%28_,moveitemat,to%29.md) method, the collection view allows all items to be reordered.

## Parameters

- `collectionView`: The collection view requesting this information.
- `indexPath`: The index path of the item that the collection view is trying to move.

## See Also

### Reordering items
- [func collectionView(UICollectionView, moveItemAt: IndexPath, to: IndexPath)](./collectionview%28_,moveitemat,to%29.md)
  Tells your data source object to move the specified item to its new location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdatasource/collectionview(_:canmoveitemat:))*