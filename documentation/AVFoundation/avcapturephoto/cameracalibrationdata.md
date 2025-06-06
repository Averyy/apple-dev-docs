# cameraCalibrationData

**Framework**: AVFoundation  
**Kind**: property

Calibration information for the camera device that captured the photo.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var cameraCalibrationData: AVCameraCalibrationData? { get }
```

#### Discussion

Camera calibration data is present only if you specified the [`isCameraCalibrationDataDeliveryEnabled`](avcapturephotosettings/iscameracalibrationdatadeliveryenabled.md) and [`isDualCameraDualPhotoDeliveryEnabled`](avcapturephotosettings/isdualcameradualphotodeliveryenabled.md) settings when requesting capture. For camera calibration data in a capture that includes depth data, see the [`AVDepthData`](avdepthdata.md) [`cameraCalibrationData`](avdepthdata/cameracalibrationdata.md) property.

## See Also

- [var depthData: AVDepthData?](avcapturephoto/depthdata.md)
  Depth or disparity map data captured with the photo.
- [var sourceDeviceType: AVCaptureDevice.DeviceType?](avcapturephoto/sourcedevicetype.md)
  The type of device that captured the photo.
- [var metadata: [String : Any]](avcapturephoto/metadata.md)
  A dictionary of metadata describing the captured image.
- [var portraitEffectsMatte: AVPortraitEffectsMatte?](avcapturephoto/portraiteffectsmatte.md)
  The portrait effects matte captured with the photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephoto/cameracalibrationdata)*