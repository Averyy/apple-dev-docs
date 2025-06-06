# cameraSnapshotControlDidUpdateMostRecentSnapshot(_:)

**Framework**: HomeKit  
**Kind**: method

Tells the delegate that the most recent snapshot has been updated.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
optional func cameraSnapshotControlDidUpdateMostRecentSnapshot(_ cameraSnapshotControl: HMCameraSnapshotControl)
```

## Parameters

- `cameraSnapshotControl`: The camera snapshot control responsible for the updated snapshot.

## See Also

- [func cameraSnapshotControl(HMCameraSnapshotControl, didTake: HMCameraSnapshot?, error: (any Error)?)](hmcamerasnapshotcontroldelegate/camerasnapshotcontrol(_:didtake:error:).md)
  Tells the delegate that the camera has taken a new snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerasnapshotcontroldelegate/camerasnapshotcontroldidupdatemostrecentsnapshot(_:))*