# isPrefetchingEnabled

**Framework**: Uikit  
**Kind**: property

A Boolean value that indicates whether cell and data prefetching are enabled.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isPrefetchingEnabled: Bool { get set }
```

#### Discussion

When [`true`](https://developer.apple.com/documentation/swift/true), the collection view requests cells in advance of when they will be displayed, spreading the rendering over multiple layout passes. When [`false`](https://developer.apple.com/documentation/swift/false), the cells are requested as they are needed for display, often with multiple cells being requested in the same render loop. Setting this property to [`false`](https://developer.apple.com/documentation/swift/false) also disables data prefetching. The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true).

> **Note**:  When prefetching is enabled the [`collectionView(_:cellForItemAt:)`](uicollectionviewdatasource/collectionview(_:cellforitemat:).md) method on the collection view delegate is called in advance of when the cell is required. To avoid inconsistencies in the visual appearance, use the [`collectionView(_:willDisplay:forItemAt:)`](uicollectionviewdelegate/collectionview(_:willdisplay:foritemat:).md) delegate method to update the cell to reflect visual state such as selection.

## See Also

- [var prefetchDataSource: (any UICollectionViewDataSourcePrefetching)?](uicollectionview/prefetchdatasource.md)
  The object that acts as the prefetching data source for the collection view, receiving notifications of upcoming cell data requirements.
- [protocol UICollectionViewDataSourcePrefetching](uicollectionviewdatasourceprefetching.md)
  A protocol that provides advance warning of the data requirements for a collection view, allowing the triggering of asynchronous data load operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/isprefetchingenabled)*