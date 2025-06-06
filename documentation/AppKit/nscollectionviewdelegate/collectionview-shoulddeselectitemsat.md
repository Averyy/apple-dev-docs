# collectionView(_:shouldDeselectItemsAt:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate object to approve the pending deselection of items.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, shouldDeselectItemsAt indexPaths: Set<IndexPath>) -> Set<IndexPath>
```

#### Return Value

The set of [`NSIndexPath`](https://developer.apple.com/documentation/Foundation/NSIndexPath) objects corresponding to the items that you want to be deselected. If you do not want any items deselected, return an empty set.

#### Discussion

Use this method to approve or modify the items that the user tries to deselect. During interactive selection, the collection view calls this method whenever the user deselects items. Your implementation of the method can return the proposed set of index paths as-is or modify the set before returning it. You might modify the set to disallow the deselection of specific items.

This method is not called when you set the selection programmatically using the methods of the [`NSCollectionView`](nscollectionview.md) class. If you do not implement this method, the collection view deselects the items specified by the `indexPaths` parameter.

## Parameters

- `collectionView`: The collection view making the request.
- `indexPaths`: The set of   objects corresponding to the items deselected by the user.

## See Also

- [func collectionView(NSCollectionView, shouldSelectItemsAt: Set<IndexPath>) -> Set<IndexPath>](nscollectionviewdelegate/collectionview(_:shouldselectitemsat:).md)
  Asks the delegate to approve the pending selection of items.
- [func collectionView(NSCollectionView, didSelectItemsAt: Set<IndexPath>)](nscollectionviewdelegate/collectionview(_:didselectitemsat:).md)
  Notifies the delegate object that one or more items were selected.
- [func collectionView(NSCollectionView, didDeselectItemsAt: Set<IndexPath>)](nscollectionviewdelegate/collectionview(_:diddeselectitemsat:).md)
  Notifies the delegate object that one or more items were deselected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:shoulddeselectitemsat:))*