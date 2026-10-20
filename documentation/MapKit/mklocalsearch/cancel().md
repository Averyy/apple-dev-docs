# cancel()

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) cancel;
```

#### Discussion

If no search operation is in progress, this method does nothing.

## See Also

### Performing the search
- [func start(completionHandler: (MKLocalSearch.Response?, (any Error)?) -> Void)](./start%28completionhandler%29.md)
  Starts the search and delivers the results to the specified completion handler.
- [MKLocalSearch.CompletionHandler](./completionhandler.md)
  A completion handler block for a search operation.
- [var isSearching: Bool](./issearching.md)
  A Boolean value that indicates whether the search is in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearch/cancel())*