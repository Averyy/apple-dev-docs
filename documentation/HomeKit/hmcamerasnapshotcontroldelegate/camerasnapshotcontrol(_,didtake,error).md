# cameraSnapshotControl(_:didTake:error:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the camera has taken a new snapshot.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
optional func cameraSnapshotControl(_ cameraSnapshotControl: HMCameraSnapshotControl, didTake snapshot: HMCameraSnapshot?, error: (any Error)?)
```

```objc
- (void) cameraSnapshotControl:(HMCameraSnapshotControl *) cameraSnapshotControl didTakeSnapshot:(HMCameraSnapshot *) snapshot error:(NSError *) error;
```

## Parameters

- `cameraSnapshotControl`: The camera snapshot control responsible for the new snapshot.
- `snapshot`: The snapshot taken by the camera. `nil` if there was a problem.
- `error`: An error that is populated if there was a problem taking the snapshot; `nil` otherwise.

## See Also

### Observing snapshot activity
- [func cameraSnapshotControlDidUpdateMostRecentSnapshot(HMCameraSnapshotControl)](./camerasnapshotcontroldidupdatemostrecentsnapshot%28_%29.md)
  Tells the delegate that the most recent snapshot has been updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerasnapshotcontroldelegate/camerasnapshotcontrol(_:didtake:error:))*