# visibleItems()

**Framework**: AppKit  
**Kind**: method

Returns an array of the actively managed items in the collection view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func visibleItems() -> [NSCollectionViewItem]
```

#### Return Value

An array of [`NSCollectionViewItem`](nscollectionviewitem.md) objects. The returned array may be empty.

#### Discussion

The items returned by this method represent the ones that are active and currently being managed by the collection view. This array may contain items that are outside of the collection view’s actual visible rectangle. For example, it may contain items that were recently visible but have since been scrolled out of view. To test whether an item is actually visible, check to see if its frame rectangle intersects the [`visibleRect`](nsview/visiblerect.md) of the collection view.

## See Also

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
- [func supplementaryView(forElementKind: NSCollectionView.SupplementaryElementKind, at: IndexPath) -> (any NSView & NSCollectionViewElement)?](nscollectionview/supplementaryview(forelementkind:at:).md)
  Returns the supplementary view associated with the specified index path.
- [func scrollToItems(at: Set<IndexPath>, scrollPosition: NSCollectionView.ScrollPosition)](nscollectionview/scrolltoitems(at:scrollposition:).md)
  Scrolls the collection view contents until the specified items are visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/visibleitems())*