# prefetchDataSource

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The object that acts as the prefetching data source for the collection view, receiving notifications of upcoming cell data requirements.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
weak var prefetchDataSource: (any UICollectionViewDataSourcePrefetching)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UICollectionViewDataSourcePrefetching> prefetchDataSource;
```

#### Discussion

Assign an object that conforms to the [`UICollectionViewDataSourcePrefetching`](../uicollectionviewdatasourceprefetching.md) protocol to facilitate prefetching of data for cells to be displayed in the near future. To disable data prefetching behavior, set this property to `nil`.

## See Also

### Prefetching collection view cells and data
- [var isPrefetchingEnabled: Bool](./isprefetchingenabled.md)
  A Boolean value that indicates whether cell and data prefetching are enabled.
- [protocol UICollectionViewDataSourcePrefetching](../uicollectionviewdatasourceprefetching.md)
  A protocol that provides advance warning of the data requirements for a collection view, allowing the triggering of asynchronous data load operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/prefetchdatasource)*