# indexPathForItem(at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Gets the index path of the item at the specified point in the collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func indexPathForItem(at point: CGPoint) -> IndexPath?
```

```objc
- (NSIndexPath *) indexPathForItemAtPoint:(CGPoint) point;
```

#### Return Value

The index path of the item at the specified point or `nil` if no item was found at the specified point.

#### Discussion

This method relies on the layout information provided by the associated layout object to determine which item contains the point.

## Parameters

- `point`: A point in the collection view’s coordinate system.

## See Also

### Locating items and views in the collection view
- [var indexPathsForVisibleItems: [IndexPath]](./indexpathsforvisibleitems.md)
  An array of the visible items in the collection view.
- [func indexPath(for: UICollectionViewCell) -> IndexPath?](./indexpath%28for%29.md)
  Gets the index path of the specified cell.
- [func cellForItem(at: IndexPath) -> UICollectionViewCell?](./cellforitem%28at%29.md)
  Gets the cell object at the index path you specify.
- [func indexPathsForVisibleSupplementaryElements(ofKind: String) -> [IndexPath]](./indexpathsforvisiblesupplementaryelements%28ofkind%29.md)
  Gets the index paths of all visible supplementary views of the specified type.
- [func supplementaryView(forElementKind: String, at: IndexPath) -> UICollectionReusableView?](./supplementaryview%28forelementkind,at%29.md)
  Gets the supplementary view at the specified index path.
- [func visibleSupplementaryViews(ofKind: String) -> [UICollectionReusableView]](./visiblesupplementaryviews%28ofkind%29.md)
  Gets an array of the visible supplementary views of the specified kind.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/indexpathforitem(at:))*