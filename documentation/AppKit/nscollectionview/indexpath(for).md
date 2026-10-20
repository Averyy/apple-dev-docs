# indexPath(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index path of the specified item.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func indexPath(for item: NSCollectionViewItem) -> IndexPath?
```

```objc
- (NSIndexPath *) indexPathForItem:(NSCollectionViewItem *) item;
```

#### Return Value

The item’s index path or `nil` if the item is not in the collection view.

## Parameters

- `item`: The item whose index path you want to know.

## See Also

### Locating Items and Views
- [func visibleItems() -> [NSCollectionViewItem]](./visibleitems%28%29.md)
  Returns an array of the actively managed items in the collection view.
- [func indexPathsForVisibleItems() -> Set<IndexPath>](./indexpathsforvisibleitems%28%29.md)
  Returns the index paths of the currently active items.
- [func visibleSupplementaryViews(ofKind: NSCollectionView.SupplementaryElementKind) -> [any NSView & NSCollectionViewElement]](./visiblesupplementaryviews%28ofkind%29.md)
  Returns an array of the actively managed supplementary views in the collection view.
- [func indexPathsForVisibleSupplementaryElements(ofKind: NSCollectionView.SupplementaryElementKind) -> Set<IndexPath>](./indexpathsforvisiblesupplementaryelements%28ofkind%29.md)
  Returns the index paths of the currently active supplementary views.
- [func indexPathForItem(at: NSPoint) -> IndexPath?](./indexpathforitem%28at%29.md)
  Returns the index path of the item at the specified point.
- [func item(at: IndexPath) -> NSCollectionViewItem?](./item%28at%29-2vx2h.md)
  Returns the item associated with the specified index path.
- [func supplementaryView(forElementKind: NSCollectionView.SupplementaryElementKind, at: IndexPath) -> (any NSView & NSCollectionViewElement)?](./supplementaryview%28forelementkind,at%29.md)
  Returns the supplementary view associated with the specified index path.
- [func scrollToItems(at: Set<IndexPath>, scrollPosition: NSCollectionView.ScrollPosition)](./scrolltoitems%28at,scrollposition%29.md)
  Scrolls the collection view contents until the specified items are visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/indexpath(for:))*