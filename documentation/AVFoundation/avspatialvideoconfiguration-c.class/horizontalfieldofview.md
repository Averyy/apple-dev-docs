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

```objc
@property (atomic, copy, nullable) NSNumber * horizontalFieldOfView;
```

## See Also

### Modifying the configuration
- [cameraCalibrationDataLensCollection](./cameracalibrationdatalenscollection.md)
  Specifies intrinsic and extrinsic parameters for single or multiple lenses.
- [cameraSystemBaseline](./camerasystembaseline.md)
  Specifies the distance between centers of the lenses of the camera system that created the video.
- [disparityAdjustment](./disparityadjustment.md)
  Specifies a relative shift of the left and right images, which changes the zero parallax plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avspatialvideoconfiguration-c.class/horizontalfieldofview)*