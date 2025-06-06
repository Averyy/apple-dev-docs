# collectionView(_:shouldChangeItemsAt:to:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate to approve the pending highlighting of the specified items.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, shouldChangeItemsAt indexPaths: Set<IndexPath>, to highlightState: NSCollectionViewItem.HighlightState) -> Set<IndexPath>
```

#### Return Value

The set of [`NSIndexPath`](https://developer.apple.com/documentation/Foundation/NSIndexPath) objects corresponding to the items that you want to receive the specified highlight. If you do not want any items to receive the specified highlight state, return an empty set.

#### Discussion

Use this method to approve or modify the set of items targeted to receive the specified highlight state. During interactive selection or dragging, the collection view calls this method when actions occur that would affect the highlight state of items. Your implementation of the method can return the proposed set of index paths as-is or modify the set and disallow the highlighting of some or all of the items. Removing items from the set suppresses the corresponding actions, such as selecting the item or showing its eligibility as a drop target.

If you do not implement this method, the collection view updates the highlight state for the items specified by the `indexPaths` parameter.

## Parameters

- `collectionView`: The collection view making the request.
- `indexPaths`: The set of   objects corresponding to the items being highlighted.
- `highlightState`: The new highlight state for the items.

## See Also

- [func collectionView(NSCollectionView, didChangeItemsAt: Set<IndexPath>, to: NSCollectionViewItem.HighlightState)](nscollectionviewdelegate/collectionview(_:didchangeitemsat:to:).md)
  Notifies the delegate that the highlight state of the specified items changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:shouldchangeitemsat:to:))*