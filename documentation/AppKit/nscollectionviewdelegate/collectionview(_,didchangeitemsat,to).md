# collectionView(_:didChangeItemsAt:to:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate that the highlight state of the specified items changed.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: NSCollectionView, didChangeItemsAt indexPaths: Set<IndexPath>, to highlightState: NSCollectionViewItem.HighlightState)
```

```objc
- (void) collectionView:(NSCollectionView *) collectionView didChangeItemsAtIndexPaths:(NSSet<NSIndexPath *> *) indexPaths toHighlightState:(NSCollectionViewItemHighlightState) highlightState;
```

## Discussion

After the highlight state of one or more items changes successfully, the collection view calls this method to report the change. Use this method to respond to the change and to make any necessary adjustments to your content or the collection view.

## Parameters

- `collectionView`: The collection view notifying you of the highlight change.
- `indexPaths`: The set of [`NSIndexPath`](../../Foundation/nsindexpath.md) objects corresponding to the items whose highlight state changed.
- `highlightState`: The new highlight state of the items.

## See Also

### Managing Item Highlighting
- [func collectionView(NSCollectionView, shouldChangeItemsAt: Set<IndexPath>, to: NSCollectionViewItem.HighlightState) -> Set<IndexPath>](./collectionview%28_,shouldchangeitemsat,to%29.md)
  Asks the delegate to approve the pending highlighting of the specified items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdelegate/collectionview(_:didchangeitemsat:to:))*