# isStarted

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the query has started. (read-only)

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
var isStarted: Bool { get }
```

#### Discussion

This property contains [`true`](https://developer.apple.com/documentation/Swift/true) when the receiver has executed the `startQuery` method; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func start() -> Bool](nsmetadataquery/start.md)
  Attempts to start the query.
- [var isGathering: Bool](nsmetadataquery/isgathering.md)
  A Boolean value that indicates whether the receiver is in the initial gathering phase of the query. (read-only)
- [var isStopped: Bool](nsmetadataquery/isstopped.md)
  A Boolean value that indicates whether the query has stopped.
- [func stop()](nsmetadataquery/stop.md)
  Stops the receiver’s current query from gathering any further results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataquery/isstarted)*