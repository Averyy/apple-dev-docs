# isCancelled

**Framework**: Core Spotlight  
**Kind**: property

A Boolean value that indicates whether the current query is no longer running.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
var isCancelled: Bool { get }
```

#### Discussion

The value of this property is `true` if you canceled it, and `false` if it’s still running or able to run.

## See Also

- [func start()](cssearchquery/start.md)
  Starts searching the index for items that match the current query string and parameters.
- [func cancel()](cssearchquery/cancel.md)
  Cancels the current query operation.
- [var foundItemCount: Int](cssearchquery/founditemcount.md)
  The number of matching items found for the given query string.
- [var foundItemsHandler: (([CSSearchableItem]) -> Void)?](cssearchquery/founditemshandler.md)
  The block to execute when the query delivers a new batch of matching items.
- [var completionHandler: (((any Error)?) -> Void)?](cssearchquery/completionhandler.md)
  The block to execute when the query finishes delivering all results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchquery/iscancelled)*