# lightEstimate

**Framework**: ARKit  
**Kind**: property

An estimate of lighting conditions based on the camera image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var lightEstimate: ARLightEstimate? { get }
```

#### Discussion

If you render your own overlay graphics for the AR scene, you can use this information in shading algorithms to help make those graphics match the real-world lighting conditions of the scene captured by the camera. (The [`ARSCNView`](arscnview.md) class automatically uses this information to configure SceneKit lighting.)

This property’s value is `nil` if the [`isLightEstimationEnabled`](arconfiguration/islightestimationenabled.md) property of the session configuration that captured this frame is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [func displayTransform(for: UIInterfaceOrientation, viewportSize: CGSize) -> CGAffineTransform](arframe/displaytransform(for:viewportsize:).md)
  Returns an affine transform for converting between normalized image coordinates and a coordinate space appropriate for rendering the camera image onscreen.
- [var rawFeaturePoints: ARPointCloud?](arframe/rawfeaturepoints.md)
  The current intermediate results of the scene analysis ARKit uses to perform world tracking.
- [var capturedDepthData: AVDepthData?](arframe/captureddepthdata.md)
  Depth data captured in front-camera experiences.
- [var capturedDepthDataTimestamp: TimeInterval](arframe/captureddepthdatatimestamp.md)
  The time at which depth data for the frame (if any) was captured.
- [var sceneDepth: ARDepthData?](arframe/scenedepth.md)
  Data on the distance between a device’s rear camera and real-world objects in an AR experience.
- [var smoothedSceneDepth: ARDepthData?](arframe/smoothedscenedepth.md)
  An average of distance measurements between a device’s rear camera and real-world objects that creates smoother visuals in an AR experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/lightestimate)*