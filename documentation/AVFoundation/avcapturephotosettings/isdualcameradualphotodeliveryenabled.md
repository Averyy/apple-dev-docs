# isDualCameraDualPhotoDeliveryEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that determines whether a dual camera device delivers images from both cameras.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var isDualCameraDualPhotoDeliveryEnabled: Bool { get set }
```

#### Discussion

When this property is [`false`](https://developer.apple.com/documentation/swift/false) (the default), and the photo output is configured with a capture device of the [`builtInDualCamera`](avcapturedevice/devicetype-swift.struct/builtindualcamera.md) type, the photo output delivers a single main photo image for each capture. (The device determines how to produce that image from one or both cameras).

If you change this setting to [`true`](https://developer.apple.com/documentation/swift/true), your delegate’s [`photoOutput(_:didFinishProcessingPhoto:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:error:).md) method fires at least twice for each main image—once for the telephoto image and again for the wide-angle image. Setting this property to true when not using a dual-camera device raises an exception.

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
- [var isAutoDualCameraFusionEnabled: Bool](avcapturephotosettings/isautodualcamerafusionenabled.md)
  A Boolean value that specifies whether captures automatically combine data from a dual camera device.
- [var isAutoStillImageStabilizationEnabled: Bool](avcapturephotosettings/isautostillimagestabilizationenabled.md)
  A Boolean value that specifies whether captures use automatic image stabilization.
- [var isHighResolutionPhotoEnabled: Bool](avcapturephotosettings/ishighresolutionphotoenabled.md)
  A Boolean value that specifies whether to capture still images at the highest resolution supported by the active device and format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/isdualcameradualphotodeliveryenabled)*