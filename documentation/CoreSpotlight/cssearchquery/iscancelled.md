# isCancelled

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the current query is no longer running.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+

## Declaration

```swift
var isCancelled: Bool { get }
```

```objc
@property (readonly, getter=isCancelled) BOOL cancelled;
```

## Discussion

The value of this property is `true` if you canceled it, and `false` if it’s still running or able to run.

## See Also

### Executing the query with handler blocks
- [func start()](./start%28%29.md)
  Starts searching the index for items that match the current query string and parameters.
- [func cancel()](./cancel%28%29.md)
  Cancels the current query operation.
- [var foundItemCount: Int](./founditemcount.md)
  The number of matching items found for the given query string.
- [var foundItemsHandler: (([CSSearchableItem]) -> Void)?](./founditemshandler.md)
  The block to execute when the query delivers a new batch of matching items.
- [var completionHandler: (((any Error)?) -> Void)?](./completionhandler.md)
  The block to execute when the query finishes delivering all results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchquery/iscancelled)*