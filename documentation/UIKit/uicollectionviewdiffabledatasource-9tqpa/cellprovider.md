# UICollectionViewDiffableDataSource.CellProvider

**Framework**: UIKit  
**Kind**: typealias

A closure that configures and returns a cell for a collection view from its diffable data source.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
typealias CellProvider = (UICollectionView, IndexPath, ItemIdentifierType) -> UICollectionViewCell?
```

#### Return Value

A non-`nil` configured cell object. The cell provider must return a valid cell object to the collection view.

#### Discussion

You use this closure to configure and return cells when creating a diffable data source using [`init(collectionView:cellProvider:)`](uicollectionviewdiffabledatasource-9tqpa/init(collectionview:cellprovider:).md).

## Parameters

- `collectionView`: The collection view to configure this cell for.
- `indexPath`: The index path that specifies the location of the cell in the collection view.
- `itemIdentifier`: An object, with a type that implements the   protocol, the data source uses to uniquely identify the item for this cell.

## See Also

- [class UICollectionViewDiffableDataSourceReference](uicollectionviewdiffabledatasourcereference.md)
  The object you use to manage data and provide cells for a collection view.
- [Updating collection views using diffable data sources](updating-collection-views-using-diffable-data-sources.md)
  Streamline the display and update of data in a collection view using a diffable data source that contains identifiers.
- [Implementing modern collection views](implementing-modern-collection-views.md)
  Bring compositional layouts to your app and simplify updating your user interface with diffable data sources.
- [init(collectionView: UICollectionView, cellProvider: UICollectionViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.CellProvider)](uicollectionviewdiffabledatasource-9tqpa/init(collectionview:cellprovider:).md)
  Creates a diffable data source with the specified cell provider, and connects it to the specified collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/cellprovider)*