# depthData

**Framework**: AVFoundation  
**Kind**: property

Depth or disparity map data captured with the photo.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var depthData: AVDepthData? { get }
```

## Mentions

- [Capturing Photos with Depth](capturing-photos-with-depth.md)

#### Discussion

To request capture of depth data alongside a photo (on supported devices), set the [`isDepthDataDeliveryEnabled`](avcapturephotosettings/isdepthdatadeliveryenabled.md) property of your photo settings object to [`true`](https://developer.apple.com/documentation/swift/true) when requesting photo capture. If you did not request depth data delivery, this property’s value is `nil`.

> **Note**:  If you set the [`embedsDepthDataInPhoto`](avcapturephotosettings/embedsdepthdatainphoto.md) property of your photo object to [`false`](https://developer.apple.com/documentation/swift/false) when requesting photo capture, this property still provides depth data, but that data is not included when generating photo file data for output.

 If you set the [`embedsDepthDataInPhoto`](avcapturephotosettings/embedsdepthdatainphoto.md) property of your photo object to [`false`](https://developer.apple.com/documentation/swift/false) when requesting photo capture, this property still provides depth data, but that data is not included when generating photo file data for output.

## See Also

- [var cameraCalibrationData: AVCameraCalibrationData?](avcapturephoto/cameracalibrationdata.md)
  Calibration information for the camera device that captured the photo.
- [var sourceDeviceType: AVCaptureDevice.DeviceType?](avcapturephoto/sourcedevicetype.md)
  The type of device that captured the photo.
- [var metadata: [String : Any]](avcapturephoto/metadata.md)
  A dictionary of metadata describing the captured image.
- [var portraitEffectsMatte: AVPortraitEffectsMatte?](avcapturephoto/portraiteffectsmatte.md)
  The portrait effects matte captured with the photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephoto/depthdata)*