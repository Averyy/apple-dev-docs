# MKMapSnapshotter.CompletionHandler

**Framework**: MapKit  
**Kind**: typealias

A block that processes the results of a snapshot request.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias CompletionHandler = (MKMapSnapshotter.Snapshot?, (any Error)?) -> Void
```

## Parameters

- `snapshot`: The image data that the snapshotter generates, or   if an error occurs.
- `error`: The error that occurs, or   if the framework generates the snapshot successfully.

## See Also

- [func start(completionHandler: (MKMapSnapshotter.Snapshot?, (any Error)?) -> Void)](mkmapsnapshotter/start(completionhandler:).md)
  Submits the request to create a snapshot and delivers the results to the specified block.
- [func start(with: dispatch_queue_t, completionHandler: MKMapSnapshotter.CompletionHandler)](mkmapsnapshotter/start(with:completionhandler:).md)
  Submits the request to create a snapshot and executes the resulting block on the specified queue.
- [func cancel()](mkmapsnapshotter/cancel.md)
  Cancels the request to create a snapshot.
- [var isLoading: Bool](mkmapsnapshotter/isloading.md)
  A Boolean value that indicates whether the snapshotter is generating an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/completionhandler)*