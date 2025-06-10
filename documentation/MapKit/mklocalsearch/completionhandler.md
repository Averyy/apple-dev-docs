# MKLocalSearch.CompletionHandler

**Framework**: MapKit  
**Kind**: typealias

A completion handler block for a search operation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias CompletionHandler = (MKLocalSearch.Response?, (any Error)?) -> Void
```

#### Discussion

This block takes two parameters:

- The `response` parameter contains the search results. If an error occurs, this parameter is `nil` and the framework provides an appropriate error object in the `error` parameter.
- The `error` parameter is `nil` if the search is successful. If an error occurs during the operation, the framework sets this parameter to an appropriate error object.

This block has no return value.

## See Also

- [func start(completionHandler: (MKLocalSearch.Response?, (any Error)?) -> Void)](mklocalsearch/start(completionhandler:).md)
  Starts the search and delivers the results to the specified completion handler.
- [var isSearching: Bool](mklocalsearch/issearching.md)
  A Boolean value that indicates whether the search is in progress.
- [func cancel()](mklocalsearch/cancel.md)
  Cancels an in-progress search operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearch/completionhandler)*