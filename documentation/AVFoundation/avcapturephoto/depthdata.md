# depthData

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, nullable) AVDepthData * depthData;
```

## Mentions

- [Capturing photos with depth](../capturing-photos-with-depth.md)

## Discussion

To request capture of depth data alongside a photo (on supported devices), set the [`isDepthDataDeliveryEnabled`](../avcapturephotosettings/isdepthdatadeliveryenabled.md) property of your photo settings object to [`true`](../../Swift/true.md) when requesting photo capture. If you did not request depth data delivery, this property’s value is `nil`.

> **Note**:  If you set the [`embedsDepthDataInPhoto`](../avcapturephotosettings/embedsdepthdatainphoto.md) property of your photo object to [`false`](../../Swift/false.md) when requesting photo capture, this property still provides depth data, but that data is not included when generating photo file data for output.

## See Also

### Accessing photo metadata
- [var cameraCalibrationData: AVCameraCalibrationData?](./cameracalibrationdata.md)
  Calibration information for the camera device that captured the photo.
- [var sourceDeviceType: AVCaptureDevice.DeviceType?](./sourcedevicetype.md)
  The type of device that captured the photo.
- [var metadata: [String : Any]](./metadata.md)
  A dictionary of metadata describing the captured image.
- [var portraitEffectsMatte: AVPortraitEffectsMatte?](./portraiteffectsmatte.md)
  The portrait effects matte captured with the photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephoto/depthdata)*