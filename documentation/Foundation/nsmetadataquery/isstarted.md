# isStarted

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, getter=isStarted) BOOL started;
```

## Discussion

This property contains [`true`](../../Swift/true.md) when the receiver has executed the `startQuery` method; otherwise, [`false`](../../Swift/false.md).

## See Also

### Running queries
- [func start() -> Bool](./start%28%29.md)
  Attempts to start the query.
- [var isGathering: Bool](./isgathering.md)
  A Boolean value that indicates whether the receiver is in the initial gathering phase of the query. (read-only)
- [var isStopped: Bool](./isstopped.md)
  A Boolean value that indicates whether the query has stopped.
- [func stop()](./stop%28%29.md)
  Stops the receiver’s current query from gathering any further results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmetadataquery/isstarted)*