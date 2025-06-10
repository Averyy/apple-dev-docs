# isAutoDualCameraFusionEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that specifies whether captures automatically combine data from a dual camera device.

**Availability**:
- iOS 10.2+
- iPadOS 10.2+
- Mac Catalyst 13.1+

## Declaration

```swift
var isAutoDualCameraFusionEnabled: Bool { get set }
```

#### Discussion

The default setting is [`true`](https://developer.apple.com/documentation/swift/true), unless you are capturing a RAW photo. (By definition, RAW photos are unprocessed, and image fusion involves processing the captured image).

When you enable this setting, a dual-camera device automatically combines samples from both cameras to produce a higher quality image. This property applies only when using the [`builtInDualCamera`](avcapturedevice/devicetype-swift.struct/builtindualcamera.md) device type on supported devices.

> 💡 **Tip**:  Image processing, including dual camera fusion, increases capture time. To capture photos at the highest possible speed (like in the built-in Camera app’s burst mode), set the [`isAutoDualCameraFusionEnabled`](avcapturephotosettings/isautodualcamerafusionenabled.md) and [`isAutoStillImageStabilizationEnabled`](avcapturephotosettings/isautostillimagestabilizationenabled.md) properties to [`false`](https://developer.apple.com/documentation/swift/false) and the [`flashMode`](avcapturephotosettings/flashmode.md) property to [`AVCaptureDevice.FlashMode.off`](avcapturedevice/flashmode-swift.enum/off.md).

## See Also

- [var flashMode: AVCaptureDevice.FlashMode](avcapturephotosettings/flashmode.md)
  A setting for whether to fire the flash when capturing photos.
- [var isAutoRedEyeReductionEnabled: Bool](avcapturephotosettings/isautoredeyereductionenabled.md)
  A Boolean value that indicates whether to use auto red-eye reduction on flash captures.
- [var maxPhotoDimensions: CMVideoDimensions](avcapturephotosettings/maxphotodimensions.md)
  The maximum resolution of the photo to capture.
- [var photoQualityPrioritization: AVCapturePhotoOutput.QualityPrioritization](avcapturephotosettings/photoqualityprioritization.md)
  A setting that indicates how to prioritize photo quality against speed of photo delivery.
- [var isCameraCalibrationDataDeliveryEnabled: Bool](avcapturephotosettings/iscameracalibrationdatadeliveryenabled.md)
  A Boolean value that determines whether a dual photo capture also delivers camera calibration data.
- [var isAutoContentAwareDistortionCorrectionEnabled: Bool](avcapturephotosettings/isautocontentawaredistortioncorrectionenabled.md)
  A Boolean value that specifies whether the photo output, at its discretion, uses content-aware distortion correction on this photo request.
- [var isAutoVirtualDeviceFusionEnabled: Bool](avcapturephotosettings/isautovirtualdevicefusionenabled.md)
  A Boolean value that specifies whether to use automatic virtual-device image fusion.
- [var virtualDeviceConstituentPhotoDeliveryEnabledDevices: [AVCaptureDevice]](avcapturephotosettings/virtualdeviceconstituentphotodeliveryenableddevices.md)
  The constituent devices for which the virtual device should deliver photos.
- [var isDualCameraDualPhotoDeliveryEnabled: Bool](avcapturephotosettings/isdualcameradualphotodeliveryenabled.md)
  A Boolean value that determines whether a dual camera device delivers images from both cameras.
- [var isAutoStillImageStabilizationEnabled: Bool](avcapturephotosettings/isautostillimagestabilizationenabled.md)
  A Boolean value that specifies whether captures use automatic image stabilization.
- [var isHighResolutionPhotoEnabled: Bool](avcapturephotosettings/ishighresolutionphotoenabled.md)
  A Boolean value that specifies whether to capture still images at the highest resolution supported by the active device and format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/isautodualcamerafusionenabled)*