# indexPathsForVisibleItems

**Framework**: UIKit  
**Kind**: property

An array of the visible items in the collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var indexPathsForVisibleItems: [IndexPath] { get }
```

#### Discussion

The value of this property is an unsorted array of [`NSIndexPath`](https://developer.apple.com/documentation/Foundation/NSIndexPath) objects, each of which corresponds to a visible cell in the collection view. This array doesn’t include any supplementary views that are currently visible. If there are no visible items, the value of this property is an empty array.

## See Also

- [var visibleCells: [UICollectionViewCell]](uicollectionview/visiblecells.md)
  An array of visible cells currently displayed by the collection view.
- [func indexPathForItem(at: CGPoint) -> IndexPath?](uicollectionview/indexpathforitem(at:).md)
  Gets the index path of the item at the specified point in the collection view.
- [func indexPath(for: UICollectionViewCell) -> IndexPath?](uicollectionview/indexpath(for:).md)
  Gets the index path of the specified cell.
- [func cellForItem(at: IndexPath) -> UICollectionViewCell?](uicollectionview/cellforitem(at:).md)
  Gets the cell object at the index path you specify.
- [func indexPathsForVisibleSupplementaryElements(ofKind: String) -> [IndexPath]](uicollectionview/indexpathsforvisiblesupplementaryelements(ofkind:).md)
  Gets the index paths of all visible supplementary views of the specified type.
- [func supplementaryView(forElementKind: String, at: IndexPath) -> UICollectionReusableView?](uicollectionview/supplementaryview(forelementkind:at:).md)
  Gets the supplementary view at the specified index path.
- [func visibleSupplementaryViews(ofKind: String) -> [UICollectionReusableView]](uicollectionview/visiblesupplementaryviews(ofkind:).md)
  Gets an array of the visible supplementary views of the specified kind.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/indexpathsforvisibleitems)*