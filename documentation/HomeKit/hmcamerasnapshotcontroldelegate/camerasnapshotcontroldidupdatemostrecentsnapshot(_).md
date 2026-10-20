# cameraSnapshotControlDidUpdateMostRecentSnapshot(_:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) cameraSnapshotControlDidUpdateMostRecentSnapshot:(HMCameraSnapshotControl *) cameraSnapshotControl;
```

## Parameters

- `cameraSnapshotControl`: The camera snapshot control responsible for the updated snapshot.

## See Also

### Observing snapshot activity
- [func cameraSnapshotControl(HMCameraSnapshotControl, didTake: HMCameraSnapshot?, error: (any Error)?)](./camerasnapshotcontrol%28_,didtake,error%29.md)
  Tells the delegate that the camera has taken a new snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerasnapshotcontroldelegate/camerasnapshotcontroldidupdatemostrecentsnapshot(_:))*