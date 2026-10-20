# disparityAdjustment

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Specifies a relative shift of the left and right images, which changes the zero parallax plane.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var disparityAdjustment: Int32?
```

#### Discussion

The value is in normalized image space and measured over the range of -10000 to 10000 mapping to the uniform range [-1.0…1.0]. The interval of 0.0 to 1.0 or 0 to 10000 maps onto the stereo eye view image width. The negative interval 0.0 to -1.0 or 0 to -10000 similarly map onto the stereo eye view image width. Can be nil if the value is unknown.

## See Also

### Modifying the configuration
- [var cameraCalibrationDataLensCollection: CMFormatDescription.Extensions.Value.CameraCalibrationDataLensCollection?](./cameracalibrationdatalenscollection.md)
  Specifies intrinsic and extrinsic parameters for single or multiple lenses.
- [var cameraSystemBaseline: UInt32?](./camerasystembaseline.md)
  Specifies the distance between centers of the lenses of the camera system that created the video.
- [var horizontalFieldOfView: UInt32?](./horizontalfieldofview.md)
  Specifies horizontal field of view in thousandths of a degree. Can be nil if the value is unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avspatialvideoconfiguration-swift.struct/disparityadjustment)*