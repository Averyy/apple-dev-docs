# indexPathForItem(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index path of the item at the specified point.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func indexPathForItem(at point: NSPoint) -> IndexPath?
```

```objc
- (NSIndexPath *) indexPathForItemAtPoint:(NSPoint) point;
```

## Return Value

The item at the specified point or `nil` if no item was found at that point.

## Discussion

This method uses the available layout attributes to determine which item is at the specified point. If more than one item is at the point, this method returns only the top-most item. This method ignores the opacity of the item, so items that are fully transparent are still returned by this method. Hidden items are never returned.

## Parameters

- `point`: The point in the collection view’s bounds that you want to test.

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
- [func indexPath(for: NSCollectionViewItem) -> IndexPath?](./indexpath%28for%29.md)
  Returns the index path of the specified item.
- [func item(at: IndexPath) -> NSCollectionViewItem?](./item%28at%29-2vx2h.md)
  Returns the item associated with the specified index path.
- [func supplementaryView(forElementKind: NSCollectionView.SupplementaryElementKind, at: IndexPath) -> (any NSView & NSCollectionViewElement)?](./supplementaryview%28forelementkind,at%29.md)
  Returns the supplementary view associated with the specified index path.
- [func scrollToItems(at: Set<IndexPath>, scrollPosition: NSCollectionView.ScrollPosition)](./scrolltoitems%28at,scrollposition%29.md)
  Scrolls the collection view contents until the specified items are visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/indexpathforitem(at:))*