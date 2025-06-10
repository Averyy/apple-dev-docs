# cancel()

**Framework**: MapKit  
**Kind**: method

Cancels an in-progress search operation.

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
func cancel()
```

#### Discussion

If no search operation is in progress, this method does nothing.

## See Also

- [func start(completionHandler: (MKLocalSearch.Response?, (any Error)?) -> Void)](mklocalsearch/start(completionhandler:).md)
  Starts the search and delivers the results to the specified completion handler.
- [MKLocalSearch.CompletionHandler](mklocalsearch/completionhandler.md)
  A completion handler block for a search operation.
- [var isSearching: Bool](mklocalsearch/issearching.md)
  A Boolean value that indicates whether the search is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearch/cancel())*