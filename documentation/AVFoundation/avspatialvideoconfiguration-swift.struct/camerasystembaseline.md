# cameraSystemBaseline

**Framework**: AVFoundation  
**Kind**: property

Specifies the distance between centers of the lenses of the camera system that created the video.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var cameraSystemBaseline: UInt32?
```

#### Discussion

The distance is in micrometers or thousandths of a millimeter. Can be nil if the value is unknown.

## See Also

- [var cameraCalibrationDataLensCollection: CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection?](avspatialvideoconfiguration-swift.struct/cameracalibrationdatalenscollection.md)
  Specifies intrinsic and extrinsic parameters for single or multiple lenses.
- [var disparityAdjustment: Int32?](avspatialvideoconfiguration-swift.struct/disparityadjustment.md)
  Specifies a relative shift of the left and right images, which changes the zero parallax plane.
- [var horizontalFieldOfView: UInt32?](avspatialvideoconfiguration-swift.struct/horizontalfieldofview.md)
  Specifies horizontal field of view in thousandths of a degree. Can be nil if the value is unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avspatialvideoconfiguration-swift.struct/camerasystembaseline)*