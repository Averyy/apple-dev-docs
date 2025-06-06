# supplementaryViewProvider

**Framework**: UIKit  
**Kind**: property

The closure that configures and returns the collection view’s supplementary views, such as headers and footers, from the diffable data source.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- tvOS 13.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency var supplementaryViewProvider: UICollectionViewDiffableDataSource<SectionIdentifierType, ItemIdentifierType>.SupplementaryViewProvider? { get set }
```

## See Also

- [UICollectionViewDiffableDataSource.SupplementaryViewProvider](uicollectionviewdiffabledatasource-9tqpa/supplementaryviewprovider-swift.typealias.md)
  A closure that configures and returns a collection view’s supplementary view, such as a header or footer, from a diffable data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdiffabledatasource-9tqpa/supplementaryviewprovider-swift.property)*