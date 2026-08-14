# virtualDeviceConstituentPhotoDeliveryEnabledDevices

**Framework**: AVFoundation  
**Kind**: property

The constituent devices for which the virtual device should deliver photos.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var virtualDeviceConstituentPhotoDeliveryEnabledDevices: [AVCaptureDevice] { get set }
```

#### Discussion

You can opt in to constituent-device photo delivery by setting this property to any subset of the devices in the virtual device’s [`constituentDevices`](avcapturedevice/constituentdevices.md) array. The framework calls your [`photoOutput(_:didFinishProcessingPhoto:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:error:).md)callback once for each of the devices you include in the array.

You may only set this property to a non-`nil` array if you’ve set your photo output’s [`isVirtualDeviceConstituentPhotoDeliveryEnabled`](avcapturephotooutput/isvirtualdeviceconstituentphotodeliveryenabled.md) property to [`true`](https://developer.apple.com/documentation/swift/true), and your delegate implements the [`photoOutput(_:didFinishProcessingPhoto:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:error:).md) method.

The default value of this property is an empty array.

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
- [var isDualCameraDualPhotoDeliveryEnabled: Bool](avcapturephotosettings/isdualcameradualphotodeliveryenabled.md)
  A Boolean value that determines whether a dual camera device delivers images from both cameras.
- [var isAutoDualCameraFusionEnabled: Bool](avcapturephotosettings/isautodualcamerafusionenabled.md)
  A Boolean value that specifies whether captures automatically combine data from a dual camera device.
- [var isAutoStillImageStabilizationEnabled: Bool](avcapturephotosettings/isautostillimagestabilizationenabled.md)
  A Boolean value that specifies whether captures use automatic image stabilization.
- [var isHighResolutionPhotoEnabled: Bool](avcapturephotosettings/ishighresolutionphotoenabled.md)
  A Boolean value that specifies whether to capture still images at the highest resolution supported by the active device and format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/virtualdeviceconstituentphotodeliveryenableddevices)*