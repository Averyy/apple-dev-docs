# start()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Attempts to start the query.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func start() -> Bool
```

```objc
- (BOOL) startQuery;
```

#### Return Value

[`true`](../../Swift/true.md) when successful; otherwise, [`false`](../../Swift/false.md).

A query may fail to start if it does not specify a [`predicate`](./predicate.md), or if the query has already been started.

#### Discussion

A query can’t be started if the receiver is already running a query or no predicate has been specified.

This method must be called from the receiver’s [`operationQueue`](./operationqueue.md) or on the main thread. For example:

**Swift**:

```swift
let query: NSMetadataQuery = // Initialize and set up a query
    query.operationQueue?.addOperationWithBlock {
        query.startQuery()
}
```

**Objective-C**:

```objc
NSMetadataQuery *query = // Initialize and set up a query
[query.operationQueue addOperationWithBlock:^{
    [query startQuery];
}];
```

## See Also

### Running queries
- [var isStarted: Bool](./isstarted.md)
  A Boolean value that indicates whether the query has started. (read-only)
- [var isGathering: Bool](./isgathering.md)
  A Boolean value that indicates whether the receiver is in the initial gathering phase of the query. (read-only)
- [var isStopped: Bool](./isstopped.md)
  A Boolean value that indicates whether the query has stopped.
- [func stop()](./stop%28%29.md)
  Stops the receiver’s current query from gathering any further results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataquery/start())*