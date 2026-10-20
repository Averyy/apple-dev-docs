# indexPathsForVisibleItems

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An array of the visible items in the collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var indexPathsForVisibleItems: [IndexPath] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSIndexPath *> * indexPathsForVisibleItems;
```

#### Discussion

The value of this property is an unsorted array of [`NSIndexPath`](../../Foundation/nsindexpath.md) objects, each of which corresponds to a visible cell in the collection view. This array doesn’t include any supplementary views that are currently visible. If there are no visible items, the value of this property is an empty array.

## See Also

### Related Documentation
- [var visibleCells: [UICollectionViewCell]](./visiblecells.md)
  An array of visible cells currently displayed by the collection view.
### Locating items and views in the collection view
- [func indexPathForItem(at: CGPoint) -> IndexPath?](./indexpathforitem%28at%29.md)
  Gets the index path of the item at the specified point in the collection view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/indexpathsforvisibleitems)*