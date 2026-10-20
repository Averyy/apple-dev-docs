# indexPath(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Gets the index path of the specified cell.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func indexPath(for cell: UICollectionViewCell) -> IndexPath?
```

```objc
- (NSIndexPath *) indexPathForCell:(UICollectionViewCell *) cell;
```

#### Return Value

The index path of the cell or `nil` if the specified cell is not in the collection view.

## Parameters

- `cell`: The cell object whose index path you want.

## See Also

### Locating items and views in the collection view
- [func indexPathForItem(at: CGPoint) -> IndexPath?](./indexpathforitem%28at%29.md)
  Gets the index path of the item at the specified point in the collection view.
- [var indexPathsForVisibleItems: [IndexPath]](./indexpathsforvisibleitems.md)
  An array of the visible items in the collection view.
- [func cellForItem(at: IndexPath) -> UICollectionViewCell?](./cellforitem%28at%29.md)
  Gets the cell object at the index path you specify.
- [func indexPathsForVisibleSupplementaryElements(ofKind: String) -> [IndexPath]](./indexpathsforvisiblesupplementaryelements%28ofkind%29.md)
  Gets the index paths of all visible supplementary views of the specified type.
- [func supplementaryView(forElementKind: String, at: IndexPath) -> UICollectionReusableView?](./supplementaryview%28forelementkind,at%29.md)
  Gets the supplementary view at the specified index path.
- [func visibleSupplementaryViews(ofKind: String) -> [UICollectionReusableView]](./visiblesupplementaryviews%28ofkind%29.md)
  Gets an array of the visible supplementary views of the specified kind.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/indexpath(for:))*