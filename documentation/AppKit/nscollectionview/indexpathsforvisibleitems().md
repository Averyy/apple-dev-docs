# indexPathsForVisibleItems()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index paths of the currently active items.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func indexPathsForVisibleItems() -> Set<IndexPath>
```

```objc
- (NSSet<NSIndexPath *> *) indexPathsForVisibleItems;
```

#### Return Value

The set of [`NSIndexPath`](../../Foundation/nsindexpath.md) objects corresponding to the currently visible items.

#### Discussion

The index paths returned by this method belong to items that are active and currently being managed by the collection view. As a result, the returned set may include index paths for items that are outside of the collection view’s actual visible rectangle. For example, it may contain index paths for items that were recently visible but have since been scrolled out of view. To test whether an item is visible, check to see if its frame rectangle intersects the [`visibleRect`](../nsview/visiblerect.md) of the collection view.

## See Also

### Locating Items and Views
- [func visibleItems() -> [NSCollectionViewItem]](./visibleitems%28%29.md)
  Returns an array of the actively managed items in the collection view.
- [func visibleSupplementaryViews(ofKind: NSCollectionView.SupplementaryElementKind) -> [any NSView & NSCollectionViewElement]](./visiblesupplementaryviews%28ofkind%29.md)
  Returns an array of the actively managed supplementary views in the collection view.
- [func indexPathsForVisibleSupplementaryElements(ofKind: NSCollectionView.SupplementaryElementKind) -> Set<IndexPath>](./indexpathsforvisiblesupplementaryelements%28ofkind%29.md)
  Returns the index paths of the currently active supplementary views.
- [func indexPath(for: NSCollectionViewItem) -> IndexPath?](./indexpath%28for%29.md)
  Returns the index path of the specified item.
- [func indexPathForItem(at: NSPoint) -> IndexPath?](./indexpathforitem%28at%29.md)
  Returns the index path of the item at the specified point.
- [func item(at: IndexPath) -> NSCollectionViewItem?](./item%28at%29-2vx2h.md)
  Returns the item associated with the specified index path.
- [func supplementaryView(forElementKind: NSCollectionView.SupplementaryElementKind, at: IndexPath) -> (any NSView & NSCollectionViewElement)?](./supplementaryview%28forelementkind,at%29.md)
  Returns the supplementary view associated with the specified index path.
- [func scrollToItems(at: Set<IndexPath>, scrollPosition: NSCollectionView.ScrollPosition)](./scrolltoitems%28at,scrollposition%29.md)
  Scrolls the collection view contents until the specified items are visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/indexpathsforvisibleitems())*