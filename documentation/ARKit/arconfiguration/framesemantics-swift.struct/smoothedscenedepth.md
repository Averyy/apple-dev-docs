# smoothedSceneDepth

**Framework**: ARKit  
**Kind**: property

An option that provides the distance from the device to real-world objects, averaged across several frames.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
static var smoothedSceneDepth: ARConfiguration.FrameSemantics { get }
```

#### Discussion

Enable this option on a world-tracking configuration ([`ARWorldTrackingConfiguration`](arworldtrackingconfiguration.md)) to instruct ARKit to provide your app with the distance between the user’s device and the real-world objects pictured in the frame’s [`capturedImage`](arframe/capturedimage.md). ARKit samples this distance using the LiDAR scanner and provides the results through the [`smoothedSceneDepth`](arframe/smoothedscenedepth.md) property on the session’s [`currentFrame`](arsession/currentframe.md).

To minimize the difference in LiDAR readings across frames, ARKit processes the data as an average. The averaged readings reduce flickering to create a smoother motion effect when depicting objects with depth, as demonstrated in [`Creating a fog effect using scene depth`](creating-a-fog-effect-using-scene-depth.md). Alternatively, to access a discrete LiDAR reading at the instant the framework creates the current frame, use [`sceneDepth`](arframe/scenedepth.md).

ARKit supports scene depth only on LiDAR-capable devices, so call [`supportsFrameSemantics(_:)`](arconfiguration/supportsframesemantics(_:).md) to ensure device support before attempting to enable scene depth.

## See Also

- [static var sceneDepth: ARConfiguration.FrameSemantics](arconfiguration/framesemantics-swift.struct/scenedepth.md)
  An option that provides the distance from the device to real-world objects viewed through the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/framesemantics-swift.struct/smoothedscenedepth)*