# sceneDepth

**Framework**: ARKit  
**Kind**: property

An option that provides the distance from the device to real-world objects viewed through the camera.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static var sceneDepth: ARConfiguration.FrameSemantics { get }
```

#### Discussion

Enable this option on a world-tracking configuration ([`ARWorldTrackingConfiguration`](arworldtrackingconfiguration.md)) to instruct ARKit to provide your app with the distance between the user’s device and the real-world objects in the camera feed. ARKit samples this distance using the LiDAR scanner and provides the results through the [`sceneDepth`](arframe/scenedepth.md) property on the session’s [`currentFrame`](arsession/currentframe.md).

ARKit creates this object from LiDAR readings at same time as the current frame. The data in [`sceneDepth`](arframe/scenedepth.md) reflects the distance from the device to real-world objects pictured in the frame’s [`capturedImage`](arframe/capturedimage.md). Alternatively, ARKit provides a [`smoothedSceneDepth`](arconfiguration/framesemantics-swift.struct/smoothedscenedepth.md) property that minimizes the difference in LiDAR readings across frames.

ARKit supports scene depth only on LiDAR-capable devices, so call [`supportsFrameSemantics(_:)`](arconfiguration/supportsframesemantics(_:).md) to ensure device support before attempting to enable scene depth.

## See Also

- [static var smoothedSceneDepth: ARConfiguration.FrameSemantics](arconfiguration/framesemantics-swift.struct/smoothedscenedepth.md)
  An option that provides the distance from the device to real-world objects, averaged across several frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/framesemantics-swift.struct/scenedepth)*