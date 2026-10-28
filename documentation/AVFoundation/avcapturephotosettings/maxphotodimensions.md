# maxPhotoDimensions

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The maximum resolution of the photo to capture.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 17.0+

## Declaration

```swift
var maxPhotoDimensions: CMVideoDimensions { get set }
```

```objc
@property (nonatomic) CMVideoDimensions maxPhotoDimensions;
```

## Discussion

Setting a value specifies a maximum for the captured image. The dimensions must match one of the dimensions returned by capture device’s active format’s [`supportedMaxPhotoDimensions`](../avcapturedevice/format/supportedmaxphotodimensions.md), and be equal to or smaller than the value of the photo outputs [`maxPhotoDimensions`](../avcapturephotooutput/maxphotodimensions.md).

This property defaults to the smallest dimensions returned by [`supportedMaxPhotoDimensions`](../avcapturedevice/format/supportedmaxphotodimensions.md).

## See Also

### Configuring photo settings
- [var flashMode: AVCaptureDevice.FlashMode](./flashmode.md)
  A setting for whether to fire the flash when capturing photos.
- [var isAutoRedEyeReductionEnabled: Bool](./isautoredeyereductionenabled.md)
  A Boolean value that indicates whether to use auto red-eye reduction on flash captures.
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
- [var isAutoDualCameraFusionEnabled: Bool](./isautodualcamerafusionenabled.md)
  A Boolean value that specifies whether captures automatically combine data from a dual camera device.
- [var isAutoStillImageStabilizationEnabled: Bool](./isautostillimagestabilizationenabled.md)
  A Boolean value that specifies whether captures use automatic image stabilization.
- [var isHighResolutionPhotoEnabled: Bool](./ishighresolutionphotoenabled.md)
  A Boolean value that specifies whether to capture still images at the highest resolution supported by the active device and format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/maxphotodimensions)*