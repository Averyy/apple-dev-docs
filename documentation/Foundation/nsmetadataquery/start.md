# start()

**Framework**: Foundation  
**Kind**: method

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

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) when successful; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

A query may fail to start if it does not specify a [`predicate`](nsmetadataquery/predicate.md), or if the query has already been started.

#### Discussion

A query can’t be started if the receiver is already running a query or no predicate has been specified.

This method must be called from the receiver’s [`operationQueue`](nsmetadataquery/operationqueue.md) or on the main thread. For example:

## See Also

- [var isStarted: Bool](nsmetadataquery/isstarted.md)
  A Boolean value that indicates whether the query has started. (read-only)
- [var isGathering: Bool](nsmetadataquery/isgathering.md)
  A Boolean value that indicates whether the receiver is in the initial gathering phase of the query. (read-only)
- [var isStopped: Bool](nsmetadataquery/isstopped.md)
  A Boolean value that indicates whether the query has stopped.
- [func stop()](nsmetadataquery/stop.md)
  Stops the receiver’s current query from gathering any further results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataquery/start())*