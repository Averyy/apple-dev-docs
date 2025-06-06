# isAutoVirtualDeviceFusionEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that specifies whether to use automatic virtual-device image fusion.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isAutoVirtualDeviceFusionEnabled: Bool { get set }
```

#### Discussion

When [`isAutoVirtualDeviceFusionEnabled`](avcapturephotosettings/isautovirtualdevicefusionenabled.md) and [`isVirtualDeviceFusionSupported`](avcapturephotooutput/isvirtualdevicefusionsupported.md) are true, the framework may fuse constituent camera images of a virtual device to improve still image quality, depending on the current zoom factor, light levels, and focus position. You can determine whether virtual device fusion is enabled for a particular capture request by inspecting the [`isVirtualDeviceFusionEnabled`](avcaptureresolvedphotosettings/isvirtualdevicefusionenabled.md) property of [`AVCaptureResolvedPhotoSettings`](avcaptureresolvedphotosettings.md).

The default value for this property is true, unless you’re capturing a RAW photo or a bracket using [`AVCapturePhotoBracketSettings`](avcapturephotobracketsettings.md).

> **Note**:  When using the deprecated [`AVCaptureStillImageOutput`](avcapturestillimageoutput.md) interface with a virtual device, [`isAutoVirtualDeviceFusionEnabled`](avcapturephotosettings/isautovirtualdevicefusionenabled.md) is always enabled, if supported.

 When using the deprecated [`AVCaptureStillImageOutput`](avcapturestillimageoutput.md) interface with a virtual device, [`isAutoVirtualDeviceFusionEnabled`](avcapturephotosettings/isautovirtualdevicefusionenabled.md) is always enabled, if supported.

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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/isautovirtualdevicefusionenabled)*