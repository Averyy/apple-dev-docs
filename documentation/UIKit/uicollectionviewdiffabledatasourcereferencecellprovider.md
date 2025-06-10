# UICollectionViewDiffableDataSourceReferenceCellProvider

**Framework**: UIKit  
**Kind**: typealias

A closure that configures and returns a cell for a collection view from its diffable data source.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias UICollectionViewDiffableDataSourceReferenceCellProvider = (UICollectionView, IndexPath, Any) -> UICollectionViewCell?
```

#### Return Value

A non-`nil` configured cell object. The cell provider must return a valid cell object to the collection view.

## Parameters

- `collectionView`: The collection view to configure this cell for.
- `indexPath`: The index path that specifies the location of the cell in the collection view.
- `identifier`: The identifier of the item for this cell.

## See Also

- [init(collectionView: UICollectionView, cellProvider: UICollectionViewDiffableDataSourceReferenceCellProvider)](uicollectionviewdiffabledatasourcereference/init(collectionview:cellprovider:).md)
  Creates a diffable data source with the specified cell provider, and connects it to the specified collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereferencecellprovider)*