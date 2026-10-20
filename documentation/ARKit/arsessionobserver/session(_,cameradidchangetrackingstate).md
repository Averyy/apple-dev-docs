# session(_:cameraDidChangeTrackingState:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Informs the delegate of changes to the quality of ARKit’s device position tracking.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
optional func session(_ session: ARSession, cameraDidChangeTrackingState camera: ARCamera)
```

```objc
- (void) session:(ARSession *) session cameraDidChangeTrackingState:(ARCamera *) camera;
```

#### Discussion

ARKit tracks the position and orientation of the device relative to a virtual scene through a combination of motion sensing and image processing. As such, factors that affect signal quality from the device’s motion sensing hardware or that interfere with scene detection in the camera image can result in poor estimates of the device position relative to the virtual scene.

## Parameters

- `session`: The session providing information.
- `camera`: The camera whose tracking parameters have changed. (Equivalent to [`currentFrame`](../arsession/currentframe.md).[`camera`](../arframe/camera.md).)

## See Also

### Responding to Tracking Quality Changes
- [func session(ARSession, didChange: ARGeoTrackingStatus)](./session%28_,didchange%29.md)
  Listen and react to geo-tracking state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsessionobserver/session(_:cameradidchangetrackingstate:))*