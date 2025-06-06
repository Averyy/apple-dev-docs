# metadata

**Framework**: AVFoundation  
**Kind**: property

A dictionary of metadata describing the captured image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var metadata: [String : Any] { get }
```

#### Discussion

See `CGImageProperties` for possible keys and values. Metadata captured with a photo may include image orientation, EXIF camera properties, and Live Photo metadata.

## See Also

- [var depthData: AVDepthData?](avcapturephoto/depthdata.md)
  Depth or disparity map data captured with the photo.
- [var cameraCalibrationData: AVCameraCalibrationData?](avcapturephoto/cameracalibrationdata.md)
  Calibration information for the camera device that captured the photo.
- [var sourceDeviceType: AVCaptureDevice.DeviceType?](avcapturephoto/sourcedevicetype.md)
  The type of device that captured the photo.
- [var portraitEffectsMatte: AVPortraitEffectsMatte?](avcapturephoto/portraiteffectsmatte.md)
  The portrait effects matte captured with the photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephoto/metadata)*