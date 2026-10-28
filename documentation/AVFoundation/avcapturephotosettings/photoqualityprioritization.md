# photoQualityPrioritization

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A setting that indicates how to prioritize photo quality against speed of photo delivery.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- tvOS 17.0+

## Declaration

```swift
var photoQualityPrioritization: AVCapturePhotoOutput.QualityPrioritization { get set }
```

```objc
@property (nonatomic) AVCapturePhotoQualityPrioritization photoQualityPrioritization;
```

## Discussion

[`AVCapturePhotoOutput`](../avcapturephotooutput.md) applies a variety of techniques to improve photo quality, depending on the source device’s [`activeFormat`](../avcapturedevice/activeformat.md). Some of these techniques — which include reducing noise, preserving detail in low light, and freezing motion — can take significant processing time before the system returns a photo to your delegate callback. This property allows you to specify your preferred quality versus speed of delivery.

The default value of this property is [`AVCapturePhotoOutput.QualityPrioritization.balanced`](../avcapturephotooutput/qualityprioritization/balanced.md) and indicates that speed and quality are of equal importance to you.

When you need to prioritize speed at the expense of quality, use [`AVCapturePhotoOutput.QualityPrioritization.speed`](../avcapturephotooutput/qualityprioritization/speed.md). Use [`AVCapturePhotoOutput.QualityPrioritization.quality`](../avcapturephotooutput/qualityprioritization/quality.md) to prioritize the best quality at the expense of speed.

## See Also

### Configuring photo settings
- [var flashMode: AVCaptureDevice.FlashMode](./flashmode.md)
  A setting for whether to fire the flash when capturing photos.
- [var isAutoRedEyeReductionEnabled: Bool](./isautoredeyereductionenabled.md)
  A Boolean value that indicates whether to use auto red-eye reduction on flash captures.
- [var maxPhotoDimensions: CMVideoDimensions](./maxphotodimensions.md)
  The maximum resolution of the photo to capture.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/photoqualityprioritization)*