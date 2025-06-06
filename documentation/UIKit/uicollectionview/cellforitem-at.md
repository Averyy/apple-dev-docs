# cellForItem(at:)

**Framework**: UIKit  
**Kind**: method

Gets the cell object at the index path you specify.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func cellForItem(at indexPath: IndexPath) -> UICollectionViewCell?
```

#### Return Value

The cell object at the corresponding index path. In versions of iOS earlier than iOS 15, this method returns `nil` if the cell isn’t visible or if `indexPath` is out of range. In iOS 15 and later, this method returns a non-`nil` cell if the collection view retains a prepared cell at the specified index path, even if the cell isn’t currently visible.

#### Discussion

In iOS 15 and later, the collection view retains a prepared cell in the following situations:

- Cells that the collection view prefetches and retains in its cache of prepared cells, but that aren’t visible because the collection view hasn’t displayed them yet.
- Cells that the collection view finishes displaying and continues to retain in its cache of prepared cells because they remain near the visible region and might scroll back into view.
- The cell that contains the first responder.
- The cell that has focus.

## Parameters

- `indexPath`: The index path that specifies the section and item number of the cell.

## See Also

- [func indexPathForItem(at: CGPoint) -> IndexPath?](uicollectionview/indexpathforitem(at:).md)
  Gets the index path of the item at the specified point in the collection view.
- [var indexPathsForVisibleItems: [IndexPath]](uicollectionview/indexpathsforvisibleitems.md)
  An array of the visible items in the collection view.
- [func indexPath(for: UICollectionViewCell) -> IndexPath?](uicollectionview/indexpath(for:).md)
  Gets the index path of the specified cell.
- [func indexPathsForVisibleSupplementaryElements(ofKind: String) -> [IndexPath]](uicollectionview/indexpathsforvisiblesupplementaryelements(ofkind:).md)
  Gets the index paths of all visible supplementary views of the specified type.
- [func supplementaryView(forElementKind: String, at: IndexPath) -> UICollectionReusableView?](uicollectionview/supplementaryview(forelementkind:at:).md)
  Gets the supplementary view at the specified index path.
- [func visibleSupplementaryViews(ofKind: String) -> [UICollectionReusableView]](uicollectionview/visiblesupplementaryviews(ofkind:).md)
  Gets an array of the visible supplementary views of the specified kind.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/cellforitem(at:))*