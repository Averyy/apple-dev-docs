# stop()

**Framework**: Foundation  
**Kind**: method

Stops the receiver’s current query from gathering any further results.

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
func stop()
```

#### Discussion

The receiver first completes gathering any unprocessed results. If a query is stopped before the gathering phase finishes, it does not post an `NSMetadataQueryDidStartGatheringNotification` notification.

You call this function to stop a query that is generating too many results to be useful but you still want to access the available results. If the receiver is sent a `startQuery` message after performing this method, the existing results are discarded.

## See Also

- [var isStarted: Bool](nsmetadataquery/isstarted.md)
  A Boolean value that indicates whether the query has started. (read-only)
- [func start() -> Bool](nsmetadataquery/start.md)
  Attempts to start the query.
- [var isGathering: Bool](nsmetadataquery/isgathering.md)
  A Boolean value that indicates whether the receiver is in the initial gathering phase of the query. (read-only)
- [var isStopped: Bool](nsmetadataquery/isstopped.md)
  A Boolean value that indicates whether the query has stopped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataquery/stop())*