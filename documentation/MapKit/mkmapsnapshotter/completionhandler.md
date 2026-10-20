# MKMapSnapshotter.CompletionHandler

**Framework**: MapKit  
**Kind**: typealias  
**Role**: Type Alias

A block that processes the results of a snapshot request.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias CompletionHandler = (MKMapSnapshotter.Snapshot?, (any Error)?) -> Void
```

```c
typedef void (^)(MKMapSnapshot *, NSError *) MKMapSnapshotCompletionHandler;
```

## Parameters

- `snapshot`: The image data that the snapshotter generates, or `nil` if an error occurs.
- `error`: The error that occurs, or `nil` if the framework generates the snapshot successfully.

## See Also

### Generating a snapshot
- [func start(completionHandler: (MKMapSnapshotter.Snapshot?, (any Error)?) -> Void)](./start%28completionhandler%29.md)
  Submits the request to create a snapshot and delivers the results to the specified block.
- [func start(with: dispatch_queue_t, completionHandler: (MKMapSnapshotter.Snapshot?, (any Error)?) -> Void)](./start%28with,completionhandler%29.md)
  Submits the request to create a snapshot and executes the resulting block on the specified queue.
- [func cancel()](./cancel%28%29.md)
  Cancels the request to create a snapshot.
- [var isLoading: Bool](./isloading.md)
  A Boolean value that indicates whether the snapshotter is generating an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/completionhandler)*