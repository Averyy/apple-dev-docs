# collectionView(_:didDeselectItemsAt:)

**Framework**: AppKit  
**Kind**: method

Notifies the delegate object that one or more items were deselected.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, didDeselectItemsAt indexPaths: Set<IndexPath>)
```

#### Discussion

After the user successfully deselects one or more items, the collection view calls this method to let you know that the items are no longer selected. Use this method to respond to the selection change and to make any necessary adjustments to your content or the collection view.

This method is not called when you set the selection programmatically using the methods of the [`NSCollectionView`](nscollectionview.md) class.

## Parameters

- `collectionView`: The collection view notifying you of the selection change.
- `indexPaths`: The set of   objects corresponding to the items that were deselected.

## See Also

- [func collectionView(NSCollectionView, shouldSelectItemsAt: Set<IndexPath>) -> Set<IndexPath>](nscollectionviewdelegate/collectionview(_:shouldselectitemsat:).md)
  Asks the delegate to approve the pending selection of items.
- [func collectionView(NSCollectionView, didSelectItemsAt: Set<IndexPath>)](nscollectionviewdelegate/collectionview(_:didselectitemsat:).md)
  Notifies the delegate object that one or more items were selected.
- [func collectionView(NSCollectionView, shouldDeselectItemsAt: Set<IndexPath>) -> Set<IndexPath>](nscollectionviewdelegate/collectionview(_:shoulddeselectitemsat:).md)
  Asks the delegate object to approve the pending deselection of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:diddeselectitemsat:))*