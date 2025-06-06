# isGeometricDistortionCorrectionSupported

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether this device supports geometric distortion correction.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isGeometricDistortionCorrectionSupported: Bool { get }
```

#### Discussion

Some devices benefit from geometric distortion correction (GDC), such as devices with a very wide field of view. GDC lessens the fisheye effect at the outer edge of the frame at the cost of losing a small amount of the horizontal field of view. When you enable GDC, the device upscales the corrected image to the original image size.

## See Also

- [var isGeometricDistortionCorrectionEnabled: Bool](avcapturedevice/isgeometricdistortioncorrectionenabled.md)
  A Boolean value that indicates whether geometric distortion correction is enabled for this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/isgeometricdistortioncorrectionsupported)*