# sourceDeviceType

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The type of device that captured the photo.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var sourceDeviceType: AVCaptureDevice.DeviceType? { get }
```

```objc
@property (readonly, nullable) AVCaptureDeviceType sourceDeviceType;
```

#### Discussion

When you capture dual photos with a [`builtInDualCamera`](../avcapturedevice/devicetype-swift.struct/builtindualcamera.md) device and the [`isDualCameraDualPhotoDeliveryEnabled`](../avcapturephotosettings/isdualcameradualphotodeliveryenabled.md) setting, use this property to determine which of the two resulting photo objects is from the [`builtInWideAngleCamera`](../avcapturedevice/devicetype-swift.struct/builtinwideanglecamera.md) or [`builtInTelephotoCamera`](../avcapturedevice/devicetype-swift.struct/builtintelephotocamera.md) device.

For all other captures, this property’s value is equal to the [`deviceType`](../avcapturedevice/devicetype-swift.property.md) property of the capture device to which the photo output is connected.

This property’s value can be `nil` if the [`AVCapturePhoto`](../avcapturephoto.md) object did not come from an [`AVCaptureDevice`](../avcapturedevice.md) capture.

## See Also

### Accessing photo metadata
- [var depthData: AVDepthData?](./depthdata.md)
  Depth or disparity map data captured with the photo.
- [var cameraCalibrationData: AVCameraCalibrationData?](./cameracalibrationdata.md)
  Calibration information for the camera device that captured the photo.
- [var metadata: [String : Any]](./metadata.md)
  A dictionary of metadata describing the captured image.
- [var portraitEffectsMatte: AVPortraitEffectsMatte?](./portraiteffectsmatte.md)
  The portrait effects matte captured with the photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephoto/sourcedevicetype)*