# indexPathsForVisibleSupplementaryElements(ofKind:)

**Framework**: AppKit  
**Kind**: method

Returns the index paths of the currently active supplementary views.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func indexPathsForVisibleSupplementaryElements(ofKind elementKind: NSCollectionView.SupplementaryElementKind) -> Set<IndexPath>
```

#### Return Value

The set of [`NSIndexPath`](https://developer.apple.com/documentation/Foundation/NSIndexPath) objects. The returned array may be empty.

#### Discussion

The index paths returned by this method correspond to supplementary views that are active and currently being managed by the collection view. The set may include index paths for views that are outside of the collection view’s actual visible rectangle. For example, it might contain index paths for views that were recently visible but have since been scrolled out of the visible rectangle. To test whether a view is actually visible, check to see if its frame rectangle intersects the [`visibleRect`](nsview/visiblerect.md) of the collection view.

## Parameters

- `elementKind`: The kind of the supplementary views you want returned. The layout object defines the kinds of supplementary views it supports. This parameter must not be  .

## See Also

- [func visibleItems() -> [NSCollectionViewItem]](nscollectionview/visibleitems.md)
  Returns an array of the actively managed items in the collection view.
- [func indexPathsForVisibleItems() -> Set<IndexPath>](nscollectionview/indexpathsforvisibleitems.md)
  Returns the index paths of the currently active items.
- [func visibleSupplementaryViews(ofKind: NSCollectionView.SupplementaryElementKind) -> [any NSView & NSCollectionViewElement]](nscollectionview/visiblesupplementaryviews(ofkind:).md)
  Returns an array of the actively managed supplementary views in the collection view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/indexpathsforvisiblesupplementaryelements(ofkind:))*