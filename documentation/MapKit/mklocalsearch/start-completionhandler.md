# start(completionHandler:)

**Framework**: MapKit  
**Kind**: method

Starts the search and delivers the results to the specified completion handler.

**Availability**:
- iOS 6.1+
- iPadOS 6.1+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
func start() async throws -> MKLocalSearch.Response
```

#### Discussion

> **Note**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func start() async throws -> MKLocalSearch.Response
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func start() async throws -> MKLocalSearch.Response
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

You use this method to initiate a map-based search operation. The search runs until the framework delivers the results, at which point the framework calls the specified completion handler.

Call this method only once to start the search operation. Calling this method while the search is running doesn’t stop the original search operation from finishing. However, for each subsequent call, the search object executes your completion handler and passes an error object to it.

The provided completion handler executes on your app’s main thread. The local search object keeps a reference to the completion handler block until the search object delivers the results (or an error), at which point, it relinquishes that reference.

## Parameters

- `completionHandler`: The completion handler block that processes the results. This parameter can’t be  .

## See Also

- [MKLocalSearch.CompletionHandler](mklocalsearch/completionhandler.md)
  A completion handler block for a search operation.
- [var isSearching: Bool](mklocalsearch/issearching.md)
  A Boolean value that indicates whether the search is in progress.
- [func cancel()](mklocalsearch/cancel.md)
  Cancels an in-progress search operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklocalsearch/start(completionhandler:))*