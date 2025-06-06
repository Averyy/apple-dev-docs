# supplementaryView(forElementKind:at:)

**Framework**: AppKit  
**Kind**: method

Returns the supplementary view associated with the specified index path.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func supplementaryView(forElementKind elementKind: NSCollectionView.SupplementaryElementKind, at indexPath: IndexPath) -> (any NSView & NSCollectionViewElement)?
```

#### Return Value

The view for the specified index path or `nil` if no view is available.

#### Discussion

For efficiency, the collection view does not create supplementary views until they are needed. Typically, views are created only when they need to be displayed onscreen. If the collection view does not currently have a supplementary view for the specified index path, because that view would be positioned offscreen, this method returns `nil`.

## Parameters

- `elementKind`: The kind of the supplementary views you want returned. The layout object defines the kinds of supplementary views it supports. This parameter must not be  .
- `indexPath`: The index path whose supplementary view you want.

## See Also

- [func visibleItems() -> [NSCollectionViewItem]](nscollectionview/visibleitems.md)
  Returns an array of the actively managed items in the collection view.
- [func indexPathsForVisibleItems() -> Set<IndexPath>](nscollectionview/indexpathsforvisibleitems.md)
  Returns the index paths of the currently active items.
- [func visibleSupplementaryViews(ofKind: NSCollectionView.SupplementaryElementKind) -> [any NSView & NSCollectionViewElement]](nscollectionview/visiblesupplementaryviews(ofkind:).md)
  Returns an array of the actively managed supplementary views in the collection view.
- [func indexPathsForVisibleSupplementaryElements(ofKind: NSCollectionView.SupplementaryElementKind) -> Set<IndexPath>](nscollectionview/indexpathsforvisiblesupplementaryelements(ofkind:).md)
  Returns the index paths of the currently active supplementary views.
- [func indexPath(for: NSCollectionViewItem) -> IndexPath?](nscollectionview/indexpath(for:).md)
  Returns the index path of the specified item.
- [func indexPathForItem(at: NSPoint) -> IndexPath?](nscollectionview/indexpathforitem(at:).md)
  Returns the index path of the item at the specified point.
- [func item(at: IndexPath) -> NSCollectionViewItem?](nscollectionview/item(at:)-2vx2h.md)
  Returns the item associated with the specified index path.
- [func scrollToItems(at: Set<IndexPath>, scrollPosition: NSCollectionView.ScrollPosition)](nscollectionview/scrolltoitems(at:scrollposition:).md)
  Scrolls the collection view contents until the specified items are visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/supplementaryview(forelementkind:at:))*