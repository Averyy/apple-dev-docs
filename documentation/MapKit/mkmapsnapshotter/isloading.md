# isLoading

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the snapshotter is generating an image.

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
var isLoading: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isLoading) BOOL loading;
```

## See Also

### Generating a snapshot
- [func start(completionHandler: (MKMapSnapshotter.Snapshot?, (any Error)?) -> Void)](./start%28completionhandler%29.md)
  Submits the request to create a snapshot and delivers the results to the specified block.
- [func start(with: dispatch_queue_t, completionHandler: (MKMapSnapshotter.Snapshot?, (any Error)?) -> Void)](./start%28with,completionhandler%29.md)
  Submits the request to create a snapshot and executes the resulting block on the specified queue.
- [MKMapSnapshotter.CompletionHandler](./completionhandler.md)
  A block that processes the results of a snapshot request.
- [func cancel()](./cancel%28%29.md)
  Cancels the request to create a snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter/isloading)*