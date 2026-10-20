# portraitEffectsMatte

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The portrait effects matte captured with the photo.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var portraitEffectsMatte: AVPortraitEffectsMatte? { get }
```

```objc
@property (readonly, nullable) AVPortraitEffectsMatte * portraitEffectsMatte;
```

## Mentions

- [Configuring camera capture to collect a Portrait Effects matte](../configuring-camera-capture-to-collect-a-portrait-effects-matte.md)

## See Also

### Accessing photo metadata
- [var depthData: AVDepthData?](./depthdata.md)
  Depth or disparity map data captured with the photo.
- [var cameraCalibrationData: AVCameraCalibrationData?](./cameracalibrationdata.md)
  Calibration information for the camera device that captured the photo.
- [var sourceDeviceType: AVCaptureDevice.DeviceType?](./sourcedevicetype.md)
  The type of device that captured the photo.
- [var metadata: [String : Any]](./metadata.md)
  A dictionary of metadata describing the captured image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephoto/portraiteffectsmatte)*