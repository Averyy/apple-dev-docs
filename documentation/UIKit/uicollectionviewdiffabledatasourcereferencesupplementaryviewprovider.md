# UICollectionViewDiffableDataSourceReferenceSupplementaryViewProvider

**Framework**: UIKit  
**Kind**: typealias

A closure that configures and returns a collection view’s supplementary view, such as a header or footer, from a diffable data source.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias UICollectionViewDiffableDataSourceReferenceSupplementaryViewProvider = (UICollectionView, String, IndexPath) -> UICollectionReusableView?
```

#### Return Value

A non-`nil` configured supplementary view object. The supplementary view provider must return a valid view object to the collection view.

## Parameters

- `collectionView`: The collection view to configure this supplementary view for.
- `kind`: The kind of supplementary view to provide. The layout object that supports the supplementary view defines the value of this string.
- `indexPath`: The index path that specifies the location of the supplementary view in the collection view.

## See Also

- [var supplementaryViewProvider: UICollectionViewDiffableDataSourceReferenceSupplementaryViewProvider?](uicollectionviewdiffabledatasourcereference/supplementaryviewprovider.md)
  The closure that configures and returns the collection view’s supplementary views, such as headers and footers, from the diffable data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasourcereferencesupplementaryviewprovider)*