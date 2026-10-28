# foundItemCount

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

The number of matching items found for the given query string.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+

## Declaration

```swift
var foundItemCount: Int { get }
```

```objc
@property (readonly) NSUInteger foundItemCount;
```

## Discussion

As Spotlight finds matches to the query string, it updates the value of this property and delivers the new results to the handler in the [`foundItemsHandler`](./founditemshandler.md) property. This value reflects the total number of matching items, including the number of items the query delivered to your handler block previously.

## See Also

### Executing the query with handler blocks
- [func start()](./start%28%29.md)
  Starts searching the index for items that match the current query string and parameters.
- [func cancel()](./cancel%28%29.md)
  Cancels the current query operation.
- [var isCancelled: Bool](./iscancelled.md)
  A Boolean value that indicates whether the current query is no longer running.
- [var foundItemsHandler: (([CSSearchableItem]) -> Void)?](./founditemshandler.md)
  The block to execute when the query delivers a new batch of matching items.
- [var completionHandler: (((any Error)?) -> Void)?](./completionhandler.md)
  The block to execute when the query finishes delivering all results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchquery/founditemcount)*