# isHighResolutionPhotoEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that specifies whether to capture still images at the highest resolution supported by the active device and format.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var isHighResolutionPhotoEnabled: Bool { get set }
```

#### Discussion

When this setting is [`false`](https://developer.apple.com/documentation/swift/false) (the default), a photo capture output delivers images with the dimensions specified by the [`formatDescription`](avcapturedevice/format/formatdescription.md) property of the source [`AVCaptureDevice`](avcapturedevice.md) object’s active capture format. However, some devices and capture formats allow for still image capture at resolutions higher than their video capture (and streaming photo preview) resolution. To capture the highest possible resolution for still photos (described by the capture format’s [`highResolutionStillImageDimensions`](avcapturedevice/format/highresolutionstillimagedimensions.md) property), change this setting to [`true`](https://developer.apple.com/documentation/swift/true).

If any output connected to your capture session enables video stabilization (see the [`AVCaptureConnection`](avcaptureconnection.md) [`preferredVideoStabilizationMode`](avcaptureconnection/preferredvideostabilizationmode.md) property), captured images may be around 10% smaller than the maximum still image dimensions. (This size change is an effect of video stabilization, which works by cropping and rotating to find the stable region in a moving image). Examine the [`AVCaptureResolvedPhotoSettings`](avcaptureresolvedphotosettings.md) object provided to your photo capture delegate to find the actual dimensions of each captured photo.

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
- [var isAutoStillImageStabilizationEnabled: Bool](avcapturephotosettings/isautostillimagestabilizationenabled.md)
  A Boolean value that specifies whether captures use automatic image stabilization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/ishighresolutionphotoenabled)*