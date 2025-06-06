# visibleCells

**Framework**: UIKit  
**Kind**: property

An array of visible cells currently displayed by the collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var visibleCells: [UICollectionViewCell] { get }
```

#### Return Value

An array of [`UICollectionViewCell`](uicollectionviewcell.md) objects. If no cells are visible, this method returns an empty array.

#### Discussion

This method returns the complete list of visible cells displayed by the collection view.

## See Also

- [var indexPathsForVisibleItems: [IndexPath]](uicollectionview/indexpathsforvisibleitems.md)
  An array of the visible items in the collection view.
- [var numberOfSections: Int](uicollectionview/numberofsections.md)
  The number of sections displayed by the collection view.
- [func numberOfItems(inSection: Int) -> Int](uicollectionview/numberofitems(insection:).md)
  Fetches the count of items in the specified section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/visiblecells)*