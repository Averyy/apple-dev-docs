# supplementaryViewProvider

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The closure that configures and returns the collection view’s supplementary views, such as headers and footers, from the diffable data source.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var supplementaryViewProvider: NSCollectionViewDiffableDataSourceReferenceSupplementaryViewProvider? { get set }
```

```objc
@property (copy, nullable) NSCollectionViewDiffableDataSourceSupplementaryViewProvider supplementaryViewProvider;
```

## See Also

### Creating Supplementary Views
- [typealias NSCollectionViewDiffableDataSourceReferenceSupplementaryViewProvider](../nscollectionviewdiffabledatasourcereferencesupplementaryviewprovider.md)
  A closure that configures and returns a collection view’s supplementary view, such as a header or footer, from a diffable data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewdiffabledatasourcereference/supplementaryviewprovider)*