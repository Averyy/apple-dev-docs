# sceneDepth

**Framework**: ARKit  
**Kind**: property

Data on the distance between a device’s rear camera and real-world objects in an AR experience.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var sceneDepth: ARDepthData? { get }
```

#### Discussion

This property describes the distance between a device’s camera and objects or areas in the real world, including ARKit’s confidence in the estimated distance.

This property is `nil` by default. Add the [`sceneDepth`](arconfiguration/framesemantics-swift.struct/scenedepth.md) frame semantic to your configuration’s [`frameSemantics`](arconfiguration/framesemantics-swift.property.md) to instruct the framework to populate this value with [`ARDepthData`](ardepthdata.md) captured by the LiDAR scanner.

Call [`supportsFrameSemantics(_:)`](arconfiguration/supportsframesemantics(_:).md) on your app’s configuration to support scene depth on select devices and configurations.

## See Also

- [var lightEstimate: ARLightEstimate?](arframe/lightestimate.md)
  An estimate of lighting conditions based on the camera image.
- [func displayTransform(for: UIInterfaceOrientation, viewportSize: CGSize) -> CGAffineTransform](arframe/displaytransform(for:viewportsize:).md)
  Returns an affine transform for converting between normalized image coordinates and a coordinate space appropriate for rendering the camera image onscreen.
- [var rawFeaturePoints: ARPointCloud?](arframe/rawfeaturepoints.md)
  The current intermediate results of the scene analysis ARKit uses to perform world tracking.
- [var capturedDepthData: AVDepthData?](arframe/captureddepthdata.md)
  Depth data captured in front-camera experiences.
- [var capturedDepthDataTimestamp: TimeInterval](arframe/captureddepthdatatimestamp.md)
  The time at which depth data for the frame (if any) was captured.
- [var smoothedSceneDepth: ARDepthData?](arframe/smoothedscenedepth.md)
  An average of distance measurements between a device’s rear camera and real-world objects that creates smoother visuals in an AR experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/scenedepth)*