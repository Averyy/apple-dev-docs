# item(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the item associated with the specified index path.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func item(at indexPath: IndexPath) -> NSCollectionViewItem?
```

```objc
- (NSCollectionViewItem *) itemAtIndexPath:(NSIndexPath *) indexPath;
```

#### Return Value

The item for the specified index path or `nil` if no item is available.

#### Discussion

For efficiency, the collection view does not create items until they are needed, and usually it creates them only when they need to be displayed onscreen. If the collection view does not currently have an item for the specified index path, because that item would be positioned offscreen, this method returns `nil`.

## Parameters

- `indexPath`: The index path whose item you want.

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
- [func indexPathForItem(at: NSPoint) -> IndexPath?](./indexpathforitem%28at%29.md)
  Returns the index path of the item at the specified point.
- [func supplementaryView(forElementKind: NSCollectionView.SupplementaryElementKind, at: IndexPath) -> (any NSView & NSCollectionViewElement)?](./supplementaryview%28forelementkind,at%29.md)
  Returns the supplementary view associated with the specified index path.
- [func scrollToItems(at: Set<IndexPath>, scrollPosition: NSCollectionView.ScrollPosition)](./scrolltoitems%28at,scrollposition%29.md)
  Scrolls the collection view contents until the specified items are visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/item(at:)-2vx2h)*