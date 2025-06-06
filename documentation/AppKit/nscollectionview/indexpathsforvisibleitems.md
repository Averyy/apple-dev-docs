# indexPathsForVisibleItems()

**Framework**: AppKit  
**Kind**: method

Returns the index paths of the currently active items.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func indexPathsForVisibleItems() -> Set<IndexPath>
```

#### Return Value

The set of [`NSIndexPath`](https://developer.apple.com/documentation/Foundation/NSIndexPath) objects corresponding to the currently visible items.

#### Discussion

The index paths returned by this method belong to items that are active and currently being managed by the collection view. As a result, the returned set may include index paths for items that are outside of the collection view’s actual visible rectangle. For example, it may contain index paths for items that were recently visible but have since been scrolled out of view. To test whether an item is visible, check to see if its frame rectangle intersects the [`visibleRect`](nsview/visiblerect.md) of the collection view.

## See Also

- [func visibleItems() -> [NSCollectionViewItem]](nscollectionview/visibleitems.md)
  Returns an array of the actively managed items in the collection view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/indexpathsforvisibleitems())*