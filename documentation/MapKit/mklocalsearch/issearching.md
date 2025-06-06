# isSearching

**Framework**: MapKit  
**Kind**: property

A Boolean value that indicates whether the search is in progress.

**Availability**:
- iOS 6.1+
- iPadOS 6.1+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var isSearching: Bool { get }
```

#### Discussion

The search object sets the value of this property to [`true`](https://developer.apple.com/documentation/swift/true) when you initiate a search. It remains in that state until the search object delivers search results (or an appropriate error), at which time the search object sets the value of the property to [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func start(completionHandler: (MKLocalSearch.Response?, (any Error)?) -> Void)](mklocalsearch/start(completionhandler:).md)
  Starts the search and delivers the results to the specified completion handler.
- [MKLocalSearch.CompletionHandler](mklocalsearch/completionhandler.md)
  A completion handler block for a search operation.
- [func cancel()](mklocalsearch/cancel.md)
  Cancels an in-progress search operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearch/issearching)*