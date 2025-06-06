# init(collectionView:cellProvider:)

**Framework**: UIKit  
**Kind**: init

Creates a diffable data source with the specified cell provider, and connects it to the specified collection view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency init(collectionView: UICollectionView, cellProvider: @escaping UICollectionViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.CellProvider)
```

#### Discussion

To connect a diffable data source to a collection view, you create the diffable data source using this initializer, passing in the collection view you want to associate with that data source. You also pass in a cell provider, where you configure each of your cells to determine how to display your data in the UI.

```swift
dataSource = UICollectionViewDiffableDataSource<Int, UUID>(collectionView: collectionView) {
    (collectionView: UICollectionView, indexPath: IndexPath, itemIdentifier: UUID) -> UICollectionViewCell? in
    // configure and return cell
}
```

## Parameters

- `collectionView`: The initialized collection view object to connect to the diffable data source.
- `cellProvider`: A closure that creates and returns each of the cells for the collection view from the data the diffable data source provides.

## See Also

- [UICollectionViewDiffableDataSource.CellProvider](uicollectionviewdiffabledatasource-9tqpa/cellprovider.md)
  A closure that configures and returns a cell for a collection view from its diffable data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/init(collectionview:cellprovider:))*