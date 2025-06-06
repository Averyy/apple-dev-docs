# completionHandler

**Framework**: Core Spotlight  
**Kind**: property

The block to execute when the query finishes delivering all results.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
var completionHandler: (((any Error)?) -> Void)? { get set }
```

## Mentions

- [Searching for information in your app](searching-for-information-in-your-app.md)

#### Discussion

Specify a value for this property only if you start your query with the [`start()`](cssearchquery/start().md) method. When the query finishes, the query object executes the provided closure once to let you know the search is complete. Use your handler to perform any related cleanup. The block you assign to this property returns no parameters and takes the following parameter:

If you start the query by accessing the [`results`](cssearchquery/results-swift.property.md) property of [`CSSearchQuery`](cssearchquery.md) or the [`responses`](csuserquery/responses-swift.property.md) property of [`CSUserQuery`](csuserquery.md), the query object doesn’t execute the block in this property.

## See Also

- [func start()](cssearchquery/start.md)
  Starts searching the index for items that match the current query string and parameters.
- [func cancel()](cssearchquery/cancel.md)
  Cancels the current query operation.
- [var isCancelled: Bool](cssearchquery/iscancelled.md)
  A Boolean value that indicates whether the current query is no longer running.
- [var foundItemCount: Int](cssearchquery/founditemcount.md)
  The number of matching items found for the given query string.
- [var foundItemsHandler: (([CSSearchableItem]) -> Void)?](cssearchquery/founditemshandler.md)
  The block to execute when the query delivers a new batch of matching items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchquery/completionhandler)*