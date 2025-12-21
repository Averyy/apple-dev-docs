# cameraCalibrationDataLensCollection

**Framework**: AVFoundation  
**Kind**: property

Specifies intrinsic and extrinsic parameters for single or multiple lenses.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var cameraCalibrationDataLensCollection: CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection?
```

#### Discussion

The property value is an array of dictionaries describing the camera calibration data for each lens. The camera calibration data includes intrinsics and extrinics with other parameters.  This property is only applicable when the projection kind is kCMTagProjectionTypeParametricImmersive.  Can be nil if the value is unknown.

## See Also

- [var cameraSystemBaseline: UInt32?](avspatialvideoconfiguration-swift.struct/camerasystembaseline.md)
  Specifies the distance between centers of the lenses of the camera system that created the video.
- [var disparityAdjustment: Int32?](avspatialvideoconfiguration-swift.struct/disparityadjustment.md)
  Specifies a relative shift of the left and right images, which changes the zero parallax plane.
- [var horizontalFieldOfView: UInt32?](avspatialvideoconfiguration-swift.struct/horizontalfieldofview.md)
  Specifies horizontal field of view in thousandths of a degree. Can be nil if the value is unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avspatialvideoconfiguration-swift.struct/cameracalibrationdatalenscollection)*