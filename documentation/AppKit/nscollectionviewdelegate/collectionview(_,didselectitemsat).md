# collectionView(_:didSelectItemsAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate object that one or more items were selected.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, didSelectItemsAt indexPaths: Set<IndexPath>)
```

```objc
- (void) collectionView:(NSCollectionView *) collectionView didSelectItemsAtIndexPaths:(NSSet<NSIndexPath *> *) indexPaths;
```

## Discussion

After the user successfully selects one or more items, the collection view calls this method to let you know that the selection has been made. Use this method to respond to the selection change and to make any necessary adjustments to your content or the collection view.

This method is not called when you set the selection programmatically using the methods of the [`NSCollectionView`](../nscollectionview.md) class.

## Parameters

- `collectionView`: The collection view notifying you of the selection change.
- `indexPaths`: The set of [`NSIndexPath`](../../Foundation/nsindexpath.md) objects corresponding to the items that are now selected.

## See Also

### Managing the Selection
- [func collectionView(NSCollectionView, shouldSelectItemsAt: Set<IndexPath>) -> Set<IndexPath>](./collectionview%28_,shouldselectitemsat%29.md)
  Asks the delegate to approve the pending selection of items.
- [func collectionView(NSCollectionView, shouldDeselectItemsAt: Set<IndexPath>) -> Set<IndexPath>](./collectionview%28_,shoulddeselectitemsat%29.md)
  Asks the delegate object to approve the pending deselection of items.
- [func collectionView(NSCollectionView, didDeselectItemsAt: Set<IndexPath>)](./collectionview%28_,diddeselectitemsat%29.md)
  Notifies the delegate object that one or more items were deselected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:didselectitemsat:))*