# cancel()

**Framework**: MapKit  
**Kind**: method

Cancels the request to create a snapshot.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
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

If the snapshotter isn’t in the process of generating the snapshot, calling this method does nothing.

## See Also

- [func start(completionHandler: (MKMapSnapshotter.Snapshot?, (any Error)?) -> Void)](mkmapsnapshotter/start(completionhandler:).md)
  Submits the request to create a snapshot and delivers the results to the specified block.
- [func start(with: dispatch_queue_t, completionHandler: (MKMapSnapshotter.Snapshot?, (any Error)?) -> Void)](mkmapsnapshotter/start(with:completionhandler:).md)
  Submits the request to create a snapshot and executes the resulting block on the specified queue.
- [MKMapSnapshotter.CompletionHandler](mkmapsnapshotter/completionhandler.md)
  A block that processes the results of a snapshot request.
- [var isLoading: Bool](mkmapsnapshotter/isloading.md)
  A Boolean value that indicates whether the snapshotter is generating an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/cancel())*