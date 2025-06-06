# visibleSupplementaryViews(ofKind:)

**Framework**: UIKit  
**Kind**: method

Gets an array of the visible supplementary views of the specified kind.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func visibleSupplementaryViews(ofKind elementKind: String) -> [UICollectionReusableView]
```

#### Return Value

An array of the visible supplementary views. If no supplementary views are visible, the returned array is empty.

## Parameters

- `elementKind`: The kind of supplementary view to locate. This value is defined by the layout object. This parameter must not be  .

## See Also

- [func indexPathForItem(at: CGPoint) -> IndexPath?](uicollectionview/indexpathforitem(at:).md)
  Gets the index path of the item at the specified point in the collection view.
- [var indexPathsForVisibleItems: [IndexPath]](uicollectionview/indexpathsforvisibleitems.md)
  An array of the visible items in the collection view.
- [func indexPath(for: UICollectionViewCell) -> IndexPath?](uicollectionview/indexpath(for:).md)
  Gets the index path of the specified cell.
- [func cellForItem(at: IndexPath) -> UICollectionViewCell?](uicollectionview/cellforitem(at:).md)
  Gets the cell object at the index path you specify.
- [func indexPathsForVisibleSupplementaryElements(ofKind: String) -> [IndexPath]](uicollectionview/indexpathsforvisiblesupplementaryelements(ofkind:).md)
  Gets the index paths of all visible supplementary views of the specified type.
- [func supplementaryView(forElementKind: String, at: IndexPath) -> UICollectionReusableView?](uicollectionview/supplementaryview(forelementkind:at:).md)
  Gets the supplementary view at the specified index path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/visiblesupplementaryviews(ofkind:))*