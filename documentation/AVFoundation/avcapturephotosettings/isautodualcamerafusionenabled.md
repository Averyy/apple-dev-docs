# isAutoDualCameraFusionEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether captures automatically combine data from a dual camera device.

**Availability**:
- iOS 10.2+ - Deprecated in 13.0
- iPadOS 10.2+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
var isAutoDualCameraFusionEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isAutoDualCameraFusionEnabled) BOOL autoDualCameraFusionEnabled;
```

#### Discussion

The default setting is [`true`](../../Swift/true.md), unless you are capturing a RAW photo. (By definition, RAW photos are unprocessed, and image fusion involves processing the captured image).

When you enable this setting, a dual-camera device automatically combines samples from both cameras to produce a higher quality image. This property applies only when using the [`builtInDualCamera`](../avcapturedevice/devicetype-swift.struct/builtindualcamera.md) device type on supported devices.

> 💡 **Tip**:  Image processing, including dual camera fusion, increases capture time. To capture photos at the highest possible speed (like in the built-in Camera app’s burst mode), set the [`isAutoDualCameraFusionEnabled`](./isautodualcamerafusionenabled.md) and [`isAutoStillImageStabilizationEnabled`](./isautostillimagestabilizationenabled.md) properties to [`false`](../../Swift/false.md) and the [`flashMode`](./flashmode.md) property to [`AVCaptureDevice.FlashMode.off`](../avcapturedevice/flashmode-swift.enum/off.md).

## See Also

### Configuring photo settings
- [var flashMode: AVCaptureDevice.FlashMode](./flashmode.md)
  A setting for whether to fire the flash when capturing photos.
- [var isAutoRedEyeReductionEnabled: Bool](./isautoredeyereductionenabled.md)
  A Boolean value that indicates whether to use auto red-eye reduction on flash captures.
- [var maxPhotoDimensions: CMVideoDimensions](./maxphotodimensions.md)
  The maximum resolution of the photo to capture.
- [var photoQualityPrioritization: AVCapturePhotoOutput.QualityPrioritization](./photoqualityprioritization.md)
  A setting that indicates how to prioritize photo quality against speed of photo delivery.
- [var isCameraCalibrationDataDeliveryEnabled: Bool](./iscameracalibrationdatadeliveryenabled.md)
  A Boolean value that determines whether a dual photo capture also delivers camera calibration data.
- [var isAutoContentAwareDistortionCorrectionEnabled: Bool](./isautocontentawaredistortioncorrectionenabled.md)
  A Boolean value that specifies whether the photo output, at its discretion, uses content-aware distortion correction on this photo request.
- [var isAutoVirtualDeviceFusionEnabled: Bool](./isautovirtualdevicefusionenabled.md)
  A Boolean value that specifies whether to use automatic virtual-device image fusion.
- [var virtualDeviceConstituentPhotoDeliveryEnabledDevices: [AVCaptureDevice]](./virtualdeviceconstituentphotodeliveryenableddevices.md)
  The constituent devices for which the virtual device should deliver photos.
- [var isDualCameraDualPhotoDeliveryEnabled: Bool](./isdualcameradualphotodeliveryenabled.md)
  A Boolean value that determines whether a dual camera device delivers images from both cameras.
- [var isAutoStillImageStabilizationEnabled: Bool](./isautostillimagestabilizationenabled.md)
  A Boolean value that specifies whether captures use automatic image stabilization.
- [var isHighResolutionPhotoEnabled: Bool](./ishighresolutionphotoenabled.md)
  A Boolean value that specifies whether to capture still images at the highest resolution supported by the active device and format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/isautodualcamerafusionenabled)*