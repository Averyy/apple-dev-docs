# HMCameraSnapshotControl

**Framework**: HomeKit  
**Kind**: class

An object that can take an image snapshot from a camera.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class HMCameraSnapshotControl
```

## Topics

### Taking snapshots
- [func takeSnapshot()](hmcamerasnapshotcontrol/takesnapshot.md)
  Takes an image snapshot.
- [var mostRecentSnapshot: HMCameraSnapshot?](hmcamerasnapshotcontrol/mostrecentsnapshot.md)
  The camera’s most recent snapshot.
- [class HMCameraSnapshot](hmcamerasnapshot.md)
  An object that represents a snapshot taken from a camera.
### Observing snapshot activity
- [var delegate: (any HMCameraSnapshotControlDelegate)?](hmcamerasnapshotcontrol/delegate.md)
  Delegate that receives updates as the camera takes snapshots.
- [protocol HMCameraSnapshotControlDelegate](hmcamerasnapshotcontroldelegate.md)
  A set of methods used to observe the camera’s snapshot activity.
### Initializers
- [init()](hmcamerasnapshotcontrol/init.md)

## Relationships

### Inherits From
- [HMCameraControl](hmcameracontrol.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var snapshotControl: HMCameraSnapshotControl?](hmcameraprofile/snapshotcontrol.md)
  Controls the camera’s snapshot function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerasnapshotcontrol)*