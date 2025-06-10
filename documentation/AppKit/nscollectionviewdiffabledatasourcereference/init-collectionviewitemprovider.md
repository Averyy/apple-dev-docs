# init(collectionView:itemProvider:)

**Framework**: AppKit  
**Kind**: init

Creates a diffable data source with the specified item provider, and connects it to the specified collection view.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(collectionView: NSCollectionView, itemProvider: @escaping NSCollectionViewDiffableDataSourceReferenceItemProvider)
```

## Parameters

- `collectionView`: The initialized collection view object to connect to the diffable data source.
- `itemProvider`: A closure that creates and returns each of the items for the collection view from the data the diffable data source provides.

## See Also

- [typealias NSCollectionViewDiffableDataSourceReferenceItemProvider](nscollectionviewdiffabledatasourcereferenceitemprovider.md)
  A closure that configures and returns an item for a collection view from its diffable data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdiffabledatasourcereference/init(collectionview:itemprovider:))*