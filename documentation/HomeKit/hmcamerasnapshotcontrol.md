# HMCameraSnapshotControl

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HMCameraSnapshotControl : HMCameraControl
```

## Topics

### Taking snapshots
- [func takeSnapshot()](./hmcamerasnapshotcontrol/takesnapshot%28%29.md)
  Takes an image snapshot.
- [var mostRecentSnapshot: HMCameraSnapshot?](./hmcamerasnapshotcontrol/mostrecentsnapshot.md)
  The camera’s most recent snapshot.
- [class HMCameraSnapshot](./hmcamerasnapshot.md)
  An object that represents a snapshot taken from a camera.
### Observing snapshot activity
- [var delegate: (any HMCameraSnapshotControlDelegate)?](./hmcamerasnapshotcontrol/delegate.md)
  Delegate that receives updates as the camera takes snapshots.
- [protocol HMCameraSnapshotControlDelegate](./hmcamerasnapshotcontroldelegate.md)
  A set of methods used to observe the camera’s snapshot activity.
### Initializers
- [init()](./hmcamerasnapshotcontrol/init%28%29.md)

## Relationships

### Inherits From
- [HMCameraControl](./hmcameracontrol.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Capturing snapshots
- [var snapshotControl: HMCameraSnapshotControl?](./hmcameraprofile/snapshotcontrol.md)
  Controls the camera’s snapshot function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerasnapshotcontrol)*