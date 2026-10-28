# MKMapSnapshotter

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

A utility class for capturing a map and its content into an image.

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
class MKMapSnapshotter
```

```objc
@interface MKMapSnapshotter : NSObject
```

## Overview

Use an [`MKMapSnapshotter`](./mkmapsnapshotter.md) object when you want to capture the system-provided map content, including the map tiles and imagery. The snapshotter object captures the best image possible by loading all of the available map tiles before capturing the image.

Configure a snapshotter object using an [`MKMapSnapshotter.Options`](./mkmapsnapshotter/options.md) object. The snapshot options specify the appearance of the map, including which portion of the map the snapshotter captures.

> **Note**:  Snapshotter objects don’t capture the visual representations of any overlays or annotations that your app creates. If you want those items to appear in the final snapshot, you must draw them on the resulting snapshot image. For more information about drawing custom content on map snapshots, see [`MKMapSnapshotter.Snapshot`](./mkmapsnapshotter/snapshot.md).

## Topics

### Creating a snapshotter object
- [init(options: MKMapSnapshotter.Options)](./mkmapsnapshotter/init%28options%29.md)
  Creates and returns a snapshotter object based on the specified options.
- [MKMapSnapshotter.Options](./mkmapsnapshotter/options.md)
  The options the snapshotter initializer uses to create a snapshotter to capture map-based imagery.
### Generating a snapshot
- [func start(completionHandler: (MKMapSnapshotter.Snapshot?, (any Error)?) -> Void)](./mkmapsnapshotter/start%28completionhandler%29.md)
  Submits the request to create a snapshot and delivers the results to the specified block.
- [func start(with: dispatch_queue_t, completionHandler: (MKMapSnapshotter.Snapshot?, (any Error)?) -> Void)](./mkmapsnapshotter/start%28with,completionhandler%29.md)
  Submits the request to create a snapshot and executes the resulting block on the specified queue.
- [MKMapSnapshotter.CompletionHandler](./mkmapsnapshotter/completionhandler.md)
  A block that processes the results of a snapshot request.
- [func cancel()](./mkmapsnapshotter/cancel%28%29.md)
  Cancels the request to create a snapshot.
- [var isLoading: Bool](./mkmapsnapshotter/isloading.md)
  A Boolean value that indicates whether the snapshotter is generating an image.
### Snapshot output
- [MKMapSnapshotter.Snapshot](./mkmapsnapshotter/snapshot.md)
  An image that a snapshotter object generates.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Static map snapshots
- [MKMapSnapshotter.Snapshot](./mkmapsnapshotter/snapshot.md)
  An image that a snapshotter object generates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapsnapshotter)*