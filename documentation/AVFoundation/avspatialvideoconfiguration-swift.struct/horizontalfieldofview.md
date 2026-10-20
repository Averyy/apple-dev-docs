# horizontalFieldOfView

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Specifies horizontal field of view in thousandths of a degree. Can be nil if the value is unknown.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var horizontalFieldOfView: UInt32?
```

## See Also

### Modifying the configuration
- [var cameraCalibrationDataLensCollection: CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection?](./cameracalibrationdatalenscollection.md)
  Specifies intrinsic and extrinsic parameters for single or multiple lenses.
- [var cameraSystemBaseline: UInt32?](./camerasystembaseline.md)
  Specifies the distance between centers of the lenses of the camera system that created the video.
- [var disparityAdjustment: Int32?](./disparityadjustment.md)
  Specifies a relative shift of the left and right images, which changes the zero parallax plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avspatialvideoconfiguration-swift.struct/horizontalfieldofview)*