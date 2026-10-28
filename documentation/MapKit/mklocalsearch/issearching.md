# isSearching

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the search is in progress.

**Availability**:
- iOS 6.1+
- iPadOS 6.1+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var isSearching: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isSearching) BOOL searching;
```

## Discussion

The search object sets the value of this property to [`true`](../../Swift/true.md) when you initiate a search. It remains in that state until the search object delivers search results (or an appropriate error), at which time the search object sets the value of the property to [`false`](../../Swift/false.md).

## See Also

### Performing the search
- [func start(completionHandler: (MKLocalSearch.Response?, (any Error)?) -> Void)](./start%28completionhandler%29.md)
  Starts the search and delivers the results to the specified completion handler.
- [MKLocalSearch.CompletionHandler](./completionhandler.md)
  A completion handler block for a search operation.
- [func cancel()](./cancel%28%29.md)
  Cancels an in-progress search operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearch/issearching)*