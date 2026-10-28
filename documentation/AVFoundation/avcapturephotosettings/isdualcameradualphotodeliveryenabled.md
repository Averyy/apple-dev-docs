# isDualCameraDualPhotoDeliveryEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether a dual camera device delivers images from both cameras.

**Availability**:
- iOS 11.0+ - Deprecated in 13.0
- iPadOS 11.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
var isDualCameraDualPhotoDeliveryEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isDualCameraDualPhotoDeliveryEnabled) BOOL dualCameraDualPhotoDeliveryEnabled;
```

## Discussion

When this property is [`false`](../../Swift/false.md) (the default), and the photo output is configured with a capture device of the [`builtInDualCamera`](../avcapturedevice/devicetype-swift.struct/builtindualcamera.md) type, the photo output delivers a single main photo image for each capture. (The device determines how to produce that image from one or both cameras).

If you change this setting to [`true`](../../Swift/true.md), your delegate’s [`photoOutput(_:didFinishProcessingPhoto:error:)`](../avcapturephotocapturedelegate/photooutput%28_,didfinishprocessingphoto,error%29.md) method fires at least twice for each main image—once for the telephoto image and again for the wide-angle image. Setting this property to true when not using a dual-camera device raises an exception.

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
- [var isAutoDualCameraFusionEnabled: Bool](./isautodualcamerafusionenabled.md)
  A Boolean value that specifies whether captures automatically combine data from a dual camera device.
- [var isAutoStillImageStabilizationEnabled: Bool](./isautostillimagestabilizationenabled.md)
  A Boolean value that specifies whether captures use automatic image stabilization.
- [var isHighResolutionPhotoEnabled: Bool](./ishighresolutionphotoenabled.md)
  A Boolean value that specifies whether to capture still images at the highest resolution supported by the active device and format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/isdualcameradualphotodeliveryenabled)*