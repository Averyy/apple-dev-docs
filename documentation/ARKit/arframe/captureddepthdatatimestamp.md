# capturedDepthDataTimestamp

**Framework**: ARKit  
**Kind**: property

The time at which depth data for the frame (if any) was captured.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var capturedDepthDataTimestamp: TimeInterval { get }
```

#### Discussion

Face-based AR (see [`ARFaceTrackingConfiguration`](arfacetrackingconfiguration.md)) uses the front-facing, depth-sensing camera on compatible devices. When running such a configuration, frames vended by the session contain a depth map captured by the depth camera in addition to the color pixel buffer (see capturedImage) captured by the color camera. This property’s value is always zero when running other AR configurations.

The depth-sensing camera provides data at a different frame rate than the color camera, so this property’s value may not exactly match the [`timestamp`](arframe/timestamp.md) property for the image captured by the color camera, and can also be zero if no depth data was captured at the same time as the current color image.

## See Also

- [var lightEstimate: ARLightEstimate?](arframe/lightestimate.md)
  An estimate of lighting conditions based on the camera image.
- [func displayTransform(for: UIInterfaceOrientation, viewportSize: CGSize) -> CGAffineTransform](arframe/displaytransform(for:viewportsize:).md)
  Returns an affine transform for converting between normalized image coordinates and a coordinate space appropriate for rendering the camera image onscreen.
- [var rawFeaturePoints: ARPointCloud?](arframe/rawfeaturepoints.md)
  The current intermediate results of the scene analysis ARKit uses to perform world tracking.
- [var capturedDepthData: AVDepthData?](arframe/captureddepthdata.md)
  Depth data captured in front-camera experiences.
- [var sceneDepth: ARDepthData?](arframe/scenedepth.md)
  Data on the distance between a device’s rear camera and real-world objects in an AR experience.
- [var smoothedSceneDepth: ARDepthData?](arframe/smoothedscenedepth.md)
  An average of distance measurements between a device’s rear camera and real-world objects that creates smoother visuals in an AR experience.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/captureddepthdatatimestamp)*