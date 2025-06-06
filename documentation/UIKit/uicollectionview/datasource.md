# dataSource

**Framework**: UIKit  
**Kind**: property

The object that provides the data for the collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
weak var dataSource: (any UICollectionViewDataSource)? { get set }
```

#### Discussion

The data source must adopt the [`UICollectionViewDataSource`](uicollectionviewdatasource.md) protocol. The collection view maintains a weak reference to the data source object.

## See Also

- [class UICollectionViewDiffableDataSource](uicollectionviewdiffabledatasource-9tqpa.md)
  The object you use to manage data and provide cells for a collection view.
- [protocol UICollectionViewDataSource](uicollectionviewdatasource.md)
  The methods adopted by the object you use to manage data and provide cells for a collection view.
- [Building high-performance lists and collection views](building-high-performance-lists-and-collection-views.md)
  Improve the performance of lists and collections in your app with prefetching and image preparation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/datasource)*