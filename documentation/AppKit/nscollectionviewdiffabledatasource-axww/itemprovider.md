# NSCollectionViewDiffableDataSource.ItemProvider

**Framework**: AppKit  
**Kind**: typealias  
**Role**: Type Alias

A closure that configures and returns an item for a collection view from its diffable data source.

**Availability**:
- macOS 10.15.1+

## Declaration

```swift
typealias ItemProvider = (NSCollectionView, IndexPath, ItemIdentifierType) -> NSCollectionViewItem?
```

#### Return Value

A non-`nil` configured item object. The item provider must return a valid item object to the collection view.

## Parameters

- `collectionView`: The collection view to configure this item for.
- `indexPath`: The index path that specifies the location of the item in the collection view.
- `itemIdentifier`: The identifier of the data item for this item.

## See Also

### Creating a Diffable Data Source
- [init(collectionView: NSCollectionView, itemProvider: NSCollectionViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.ItemProvider)](./init%28collectionview,itemprovider%29.md)
  Creates a diffable data source with the specified item provider, and connects it to the specified collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdiffabledatasource-axww/itemprovider)*