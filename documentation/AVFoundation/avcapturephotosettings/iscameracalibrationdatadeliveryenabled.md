# isCameraCalibrationDataDeliveryEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that determines whether a dual photo capture also delivers camera calibration data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isCameraCalibrationDataDeliveryEnabled: Bool { get set }
```

#### Discussion

When this setting is [`false`](https://developer.apple.com/documentation/Swift/false) (the default), and the [`isDualCameraDualPhotoDeliveryEnabled`](avcapturephotosettings/isdualcameradualphotodeliveryenabled.md) setting is [`true`](https://developer.apple.com/documentation/Swift/true), dual photo capture doesn’t deliver additional data.

If you change this setting to [`true`](https://developer.apple.com/documentation/Swift/true), the [`AVCapturePhoto`](avcapturephoto.md) results from a dual photo capture include [`AVCameraCalibrationData`](avcameracalibrationdata.md) objects that describe the imaging parameters for each camera. This data can be useful for performing computer vision tasks on the resulting images.

## See Also

- [var flashMode: AVCaptureDevice.FlashMode](avcapturephotosettings/flashmode.md)
  A setting for whether to fire the flash when capturing photos.
- [var isAutoRedEyeReductionEnabled: Bool](avcapturephotosettings/isautoredeyereductionenabled.md)
  A Boolean value that indicates whether to use auto red-eye reduction on flash captures.
- [var maxPhotoDimensions: CMVideoDimensions](avcapturephotosettings/maxphotodimensions.md)
  The maximum resolution of the photo to capture.
- [var photoQualityPrioritization: AVCapturePhotoOutput.QualityPrioritization](avcapturephotosettings/photoqualityprioritization.md)
  A setting that indicates how to prioritize photo quality against speed of photo delivery.
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
- [var isAutoStillImageStabilizationEnabled: Bool](avcapturephotosettings/isautostillimagestabilizationenabled.md)
  A Boolean value that specifies whether captures use automatic image stabilization.
- [var isHighResolutionPhotoEnabled: Bool](avcapturephotosettings/ishighresolutionphotoenabled.md)
  A Boolean value that specifies whether to capture still images at the highest resolution supported by the active device and format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/iscameracalibrationdatadeliveryenabled)*