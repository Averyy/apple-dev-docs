# isAutoStillImageStabilizationEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that specifies whether captures use automatic image stabilization.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var isAutoStillImageStabilizationEnabled: Bool { get set }
```

#### Discussion

The default setting is [`true`](https://developer.apple.com/documentation/swift/true), unless you are capturing a RAW photo (By definition, RAW photos are unprocessed, and image stabilization involves processing the captured image).

When you enable this setting, the device automatically applies stabilization in low-light conditions to counteract hand shake. Automatic stabilization always includes digital image stabilization, and may also include optical lens stabilization, based on the current device.

Automatic image stabilization is not compatible with the [`AVCaptureDevice.FlashMode.on`](avcapturedevice/flashmode-swift.enum/on.md) setting. If you explicitly enable the flash, the photo output ignores your image stabilization setting, and the [`isStillImageStabilizationEnabled`](avcaptureresolvedphotosettings/isstillimagestabilizationenabled.md) property of the [`AVCaptureResolvedPhotoSettings`](avcaptureresolvedphotosettings.md) object provided to your photo capture delegate is always [`false`](https://developer.apple.com/documentation/swift/false).

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
- [var isAutoDualCameraFusionEnabled: Bool](avcapturephotosettings/isautodualcamerafusionenabled.md)
  A Boolean value that specifies whether captures automatically combine data from a dual camera device.
- [var isHighResolutionPhotoEnabled: Bool](avcapturephotosettings/ishighresolutionphotoenabled.md)
  A Boolean value that specifies whether to capture still images at the highest resolution supported by the active device and format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/isautostillimagestabilizationenabled)*