# HMCameraSnapshotControlDelegate

**Framework**: HomeKit  
**Kind**: protocol

A set of methods used to observe the camera’s snapshot activity.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
protocol HMCameraSnapshotControlDelegate : NSObjectProtocol
```

## Topics

### Observing snapshot activity
- [func cameraSnapshotControl(HMCameraSnapshotControl, didTake: HMCameraSnapshot?, error: (any Error)?)](hmcamerasnapshotcontroldelegate/camerasnapshotcontrol(_:didtake:error:).md)
  Tells the delegate that the camera has taken a new snapshot.
- [func cameraSnapshotControlDidUpdateMostRecentSnapshot(HMCameraSnapshotControl)](hmcamerasnapshotcontroldelegate/camerasnapshotcontroldidupdatemostrecentsnapshot(_:).md)
  Tells the delegate that the most recent snapshot has been updated.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any HMCameraSnapshotControlDelegate)?](hmcamerasnapshotcontrol/delegate.md)
  Delegate that receives updates as the camera takes snapshots.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerasnapshotcontroldelegate)*