# MKLookAroundSnapshotter

**Framework**: MapKit  
**Kind**: class

A utility class that you use to create a static image from a LookAround scene.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MKLookAroundSnapshotter
```

## Topics

### Creating a snapshotter object
- [init(scene: MKLookAroundScene, options: MKLookAroundSnapshotter.Options)](mklookaroundsnapshotter/init(scene:options:).md)
  Create a new snapshotter object with the scene and options you specify.
### Starting and stopping a snapshot
- [func cancel()](mklookaroundsnapshotter/cancel.md)
  Cancels an in-progress snapshot request.
- [func getSnapshotWithCompletionHandler((MKLookAroundSnapshotter.Snapshot?, (any Error)?) -> Void)](mklookaroundsnapshotter/getsnapshotwithcompletionhandler(_:).md)
  Requests a new snapshot and calls the completion handler you provide.
### Monitoring the progress of a snaphot
- [var isLoading: Bool](mklookaroundsnapshotter/isloading.md)
  A Boolean value that indicates whether the snapshot request is loading.
### Customizing the snapshot
- [MKLookAroundSnapshotter.Options](mklookaroundsnapshotter/options.md)
  Values you use to customize LookAround snapshots.
### Accessing snapshot imagery
- [MKLookAroundSnapshotter.Snapshot](mklookaroundsnapshotter/snapshot.md)
  An object that contains a snapshot image.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MKLookAroundScene](mklookaroundscene.md)
  A utility class that encapsulates information the framework requires to retrieve and display a specific Look Around location’s imagery.
- [class MKLookAroundSceneRequest](mklookaroundscenerequest.md)
  A class you use to request a LookAround scene at the location you specify.
- [class MKLookAroundViewController](mklookaroundviewcontroller.md)
  A class that manages the presentation and display of a LookAround view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklookaroundsnapshotter)*