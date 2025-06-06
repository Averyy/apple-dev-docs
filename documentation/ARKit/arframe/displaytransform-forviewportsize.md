# displayTransform(for:viewportSize:)

**Framework**: ARKit  
**Kind**: method

Returns an affine transform for converting between normalized image coordinates and a coordinate space appropriate for rendering the camera image onscreen.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func displayTransform(for orientation: UIInterfaceOrientation, viewportSize: CGSize) -> CGAffineTransform
```

## Mentions

- [Displaying an AR Experience with Metal](displaying-an-ar-experience-with-metal.md)

#### Return Value

A transform matrix that converts from normalized image coordinates in the captured image to normalized image coordinates that account for the specified parameters.

#### Discussion

Normalized image coordinates range from `(0,0)` in the upper left corner of the image to `(1,1)` in the lower right corner.

This method creates an affine transform representing the rotation and aspect-fit crop operations necessary to adapt the camera image to the specified orientation and to the aspect ratio of the specified viewport. The affine transform does not scale to the viewport’s pixel size.

The [`capturedImage`](arframe/capturedimage.md) pixel buffer is the original image captured by the device camera, and thus not adjusted for device orientation or view aspect ratio.

## Parameters

- `orientation`: The orientation intended for presenting the view.
- `viewportSize`: The size, in points, of the view intended for rendering the camera image.

## See Also

- [var lightEstimate: ARLightEstimate?](arframe/lightestimate.md)
  An estimate of lighting conditions based on the camera image.
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

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/displaytransform(for:viewportsize:))*