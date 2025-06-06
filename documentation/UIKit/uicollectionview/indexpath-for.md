# indexPath(for:)

**Framework**: UIKit  
**Kind**: method

Gets the index path of the specified cell.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func indexPath(for cell: UICollectionViewCell) -> IndexPath?
```

#### Return Value

The index path of the cell or `nil` if the specified cell is not in the collection view.

## Parameters

- `cell`: The cell object whose index path you want.

## See Also

- [func indexPathForItem(at: CGPoint) -> IndexPath?](uicollectionview/indexpathforitem(at:).md)
  Gets the index path of the item at the specified point in the collection view.
- [var indexPathsForVisibleItems: [IndexPath]](uicollectionview/indexpathsforvisibleitems.md)
  An array of the visible items in the collection view.
- [func cellForItem(at: IndexPath) -> UICollectionViewCell?](uicollectionview/cellforitem(at:).md)
  Gets the cell object at the index path you specify.
- [func indexPathsForVisibleSupplementaryElements(ofKind: String) -> [IndexPath]](uicollectionview/indexpathsforvisiblesupplementaryelements(ofkind:).md)
  Gets the index paths of all visible supplementary views of the specified type.
- [func supplementaryView(forElementKind: String, at: IndexPath) -> UICollectionReusableView?](uicollectionview/supplementaryview(forelementkind:at:).md)
  Gets the supplementary view at the specified index path.
- [func visibleSupplementaryViews(ofKind: String) -> [UICollectionReusableView]](uicollectionview/visiblesupplementaryviews(ofkind:).md)
  Gets an array of the visible supplementary views of the specified kind.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/indexpath(for:))*