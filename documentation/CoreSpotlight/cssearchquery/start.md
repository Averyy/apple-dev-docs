# start()

**Framework**: Core Spotlight  
**Kind**: method

Starts searching the index for items that match the current query string and parameters.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
func start()
```

## Mentions

- [Searching for information in your app](searching-for-information-in-your-app.md)

#### Discussion

This method uses the configured search parameters and query string to begin a search of the index. It then delivers the results of that search to the closures in the [`foundItemsHandler`](cssearchquery/founditemshandler.md) and [`completionHandler`](cssearchquery/completionhandler.md) properties of the query object.

> **Note**: Don’t call this method if you fetch the query results using the [`results`](cssearchquery/results-swift.property.md) property. Accessing that property automatically starts the query.

## See Also

- [func cancel()](cssearchquery/cancel.md)
  Cancels the current query operation.
- [var isCancelled: Bool](cssearchquery/iscancelled.md)
  A Boolean value that indicates whether the current query is no longer running.
- [var foundItemCount: Int](cssearchquery/founditemcount.md)
  The number of matching items found for the given query string.
- [var foundItemsHandler: (([CSSearchableItem]) -> Void)?](cssearchquery/founditemshandler.md)
  The block to execute when the query delivers a new batch of matching items.
- [var completionHandler: (((any Error)?) -> Void)?](cssearchquery/completionhandler.md)
  The block to execute when the query finishes delivering all results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchquery/start())*