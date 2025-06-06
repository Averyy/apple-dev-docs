# collectionView(_:cancelPrefetchingForItemsAt:)

**Framework**: UIKit  
**Kind**: method

Cancels a previously triggered data prefetch request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func collectionView(_ collectionView: UICollectionView, cancelPrefetchingForItemsAt indexPaths: [IndexPath])
```

#### Discussion

The collection view calls this method to cancel prefetch requests as cells scroll out of view. Your implementation of this method is responsible for canceling the operations initiated by a previous call to [`collectionView(_:prefetchItemsAt:)`](uicollectionviewdatasourceprefetching/collectionview(_:prefetchitemsat:).md). For further information about canceling an asynchronous data loading task, see [`Concurrency Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091).

## Parameters

- `collectionView`: The collection view issuing the cancellation of the prefetch request.
- `indexPaths`: The index paths that specify the locations of the items for which data is no longer required.

## See Also

- [Prefetching collection view data](prefetching-collection-view-data.md)
  Load data for collection view cells before they display.
- [func collectionView(UICollectionView, prefetchItemsAt: [IndexPath])](uicollectionviewdatasourceprefetching/collectionview(_:prefetchitemsat:).md)
  Tells your prefetch data source object to begin preparing data for the cells at the supplied index paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdatasourceprefetching/collectionview(_:cancelprefetchingforitemsat:))*