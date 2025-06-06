# cancel()

**Framework**: Core Spotlight  
**Kind**: method

Cancels the current query operation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
func cancel()
```

## Mentions

- [Searching for information in your app](searching-for-information-in-your-app.md)

#### Discussion

Cancel a query operation when you no longer need the results. You can use this method to cancel a query you started, by using either the [`start()`](cssearchquery/start().md) method or by accessing the [`results`](cssearchquery/results-swift.property.md) property. After you cancel a query operation, you can’t restart it. To perform a new query, create a new query object. For example, you might cancel one query and start a new one when the text in your app’s search control changes.

## See Also

- [func start()](cssearchquery/start.md)
  Starts searching the index for items that match the current query string and parameters.
- [var isCancelled: Bool](cssearchquery/iscancelled.md)
  A Boolean value that indicates whether the current query is no longer running.
- [var foundItemCount: Int](cssearchquery/founditemcount.md)
  The number of matching items found for the given query string.
- [var foundItemsHandler: (([CSSearchableItem]) -> Void)?](cssearchquery/founditemshandler.md)
  The block to execute when the query delivers a new batch of matching items.
- [var completionHandler: (((any Error)?) -> Void)?](cssearchquery/completionhandler.md)
  The block to execute when the query finishes delivering all results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchquery/cancel())*