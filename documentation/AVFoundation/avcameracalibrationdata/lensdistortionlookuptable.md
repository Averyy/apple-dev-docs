# lensDistortionLookupTable

**Framework**: AVFoundation  
**Kind**: property

A map of floating-point values describing radial distortions imparted by the camera lens, for use in rectifying camera images.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var lensDistortionLookupTable: Data? { get }
```

#### Discussion

Images captured by a camera are geometrically warped by small imperfections in the lens. To project from the 2D image plane back into the 3D world, the images must be distortion corrected, or made rectilinear. Lens distortion is modeled using a one-dimensional lookup table of 32-bit float values evenly distributed along a radius from the center of the distortion to a corner, with each value representing a magnification of the radius. This model assumes symmetrical lens distortion.

When dealing with [`AVDepthData`](avdepthdata.md) objects, the disparity/depth map representations are geometrically distorted to align with images produced by the camera.

## See Also

- [var inverseLensDistortionLookupTable: Data?](avcameracalibrationdata/inverselensdistortionlookuptable.md)
  A map of floating-point values describing radial distortions for use in reapplying camera geometry to a rectified image.
- [var lensDistortionCenter: CGPoint](avcameracalibrationdata/lensdistortioncenter.md)
  The offset of the distortion center of the camera lens from the top-left corner of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcameracalibrationdata/lensdistortionlookuptable)*