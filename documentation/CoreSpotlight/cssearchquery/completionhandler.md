# completionHandler

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

The block to execute when the query finishes delivering all results.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+

## Declaration

```swift
var completionHandler: (((any Error)?) -> Void)? { get set }
```

```objc
@property (copy, nullable) void (^completionHandler)(NSError *error);
```

## Mentions

- [Searching for information in your app](../searching-for-information-in-your-app.md)

#### Discussion

Specify a value for this property only if you start your query with the [`start()`](./start%28%29.md) method. When the query finishes, the query object executes the provided closure once to let you know the search is complete. Use your handler to perform any related cleanup. The block you assign to this property returns no parameters and takes the following parameter:

- **error**: An error object with details about a problem that occurred, or `nil` if the query completed successfully.

If you start the query by accessing the [`results`](./results-swift.property.md) property of [`CSSearchQuery`](../cssearchquery.md) or the [`responses`](../csuserquery/responses-swift.property.md) property of [`CSUserQuery`](../csuserquery.md), the query object doesn’t execute the block in this property.

## See Also

### Executing the query with handler blocks
- [func start()](./start%28%29.md)
  Starts searching the index for items that match the current query string and parameters.
- [func cancel()](./cancel%28%29.md)
  Cancels the current query operation.
- [var isCancelled: Bool](./iscancelled.md)
  A Boolean value that indicates whether the current query is no longer running.
- [var foundItemCount: Int](./founditemcount.md)
  The number of matching items found for the given query string.
- [var foundItemsHandler: (([CSSearchableItem]) -> Void)?](./founditemshandler.md)
  The block to execute when the query delivers a new batch of matching items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchquery/completionhandler)*