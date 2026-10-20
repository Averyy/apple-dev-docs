# visibleSupplementaryViews(ofKind:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an array of the actively managed supplementary views in the collection view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func visibleSupplementaryViews(ofKind elementKind: NSCollectionView.SupplementaryElementKind) -> [any NSView & NSCollectionViewElement]
```

```objc
- (NSArray<NSView<NSCollectionViewElement> *> *) visibleSupplementaryViewsOfKind:(NSCollectionViewSupplementaryElementKind) elementKind;
```

#### Return Value

An array of view objects. The returned array may be empty.

#### Discussion

The views returned by this method represent the ones that are active and are currently being managed by the collection view. The array may contain supplementary views that are outside of the collection view’s actual visible rectangle. For example, it might contain views that were recently visible but have since been scrolled out of the visible rectangle. To test whether a view is actually visible, check to see if its frame rectangle intersects the [`visibleRect`](../nsview/visiblerect.md) of the collection view.

## Parameters

- `elementKind`: The kind of the supplementary views you want returned. The layout object defines the kinds of supplementary views it supports. This parameter must not be `nil`.

## See Also

### Locating Items and Views
- [func visibleItems() -> [NSCollectionViewItem]](./visibleitems%28%29.md)
  Returns an array of the actively managed items in the collection view.
- [func indexPathsForVisibleItems() -> Set<IndexPath>](./indexpathsforvisibleitems%28%29.md)
  Returns the index paths of the currently active items.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/visiblesupplementaryviews(ofkind:))*