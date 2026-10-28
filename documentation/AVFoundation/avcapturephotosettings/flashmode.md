# flashMode

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A setting for whether to fire the flash when capturing photos.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- tvOS 17.0+

## Declaration

```swift
var flashMode: AVCaptureDevice.FlashMode { get set }
```

```objc
@property (nonatomic) AVCaptureFlashMode flashMode;
```

## Discussion

The default value for this setting is [`AVCaptureDevice.FlashMode.off`](../avcapturedevice/flashmode-swift.enum/off.md).

> **Note**:  This setting supersedes the deprecated [`AVCaptureDevice`](../avcapturedevice.md) [`flashMode`](../avcapturedevice/flashmode-swift.property.md) property. When using the [`AVCapturePhotoOutput`](../avcapturephotooutput.md) class, the capture device’s flash mode doesn’t apply—use this property on your photo settings object instead.

Assuming a static scene, using the [`AVCaptureDevice.FlashMode.auto`](../avcapturedevice/flashmode-swift.enum/auto.md) setting is equivalent to testing the [`AVCapturePhotoOutput`](../avcapturephotooutput.md) [`isFlashScene`](../avcapturephotooutput/isflashscene.md) property (which indicates whether flash is recommended for the scene currently visible to the camera), and then setting the [`flashMode`](./flashmode.md) property of your photo settings output accordingly before requesting a capture. However, the visible scene can change between when you request a capture and when the camera hardware captures an image—the automatic setting ensures that the flash is enabled or disabled appropriately at the moment of capture. When the capture occurs, your [`AVCapturePhotoCaptureDelegate`](../avcapturephotocapturedelegate.md) methods receive an [`AVCaptureResolvedPhotoSettings`](../avcaptureresolvedphotosettings.md) object whose [`isFlashEnabled`](../avcaptureresolvedphotosettings/isflashenabled.md) property indicates which flash mode was used for that capture.

> **Note**:  When the device becomes very hot, the flash becomes temporarily unavailable until the device cools down (see the [`AVCaptureDevice`](../avcapturedevice.md) [`isFlashAvailable`](../avcapturedevice/isflashavailable.md) property). While the flash is unavailable, a photo output’s [`supportedFlashModes`](../avcapturephotooutput/supportedflashmodes-4u69s.md) property still reports the [`AVCaptureDevice.FlashMode.on`](../avcapturedevice/flashmode-swift.enum/on.md) and [`AVCaptureDevice.FlashMode.auto`](../avcapturedevice/flashmode-swift.enum/auto.md) options as available, so you can still enable the flash in your photo settings even when the flash is temporarily unavailable.
>
> When the photo output calls your [`AVCapturePhotoCaptureDelegate`](../avcapturephotocapturedelegate.md) methods, check the [`isFlashEnabled`](../avcaptureresolvedphotosettings/isflashenabled.md) property of the provided [`AVCaptureResolvedPhotoSettings`](../avcaptureresolvedphotosettings.md) to verify whether the flash is in use.

When specifying a flash mode, the following requirements apply:

- The specified mode must be present in the photo output’s [`supportedFlashModes`](../avcapturephotooutput/supportedflashmodes-4u69s.md) array.
- You may not enable image stabilization if the flash mode is [`AVCaptureDevice.FlashMode.on`](../avcapturedevice/flashmode-swift.enum/on.md). (Enabling the flash takes priority over the [`isAutoStillImageStabilizationEnabled`](./isautostillimagestabilizationenabled.md) setting).

The capture output validates these requirements when you call the [`capturePhoto(with:delegate:)`](../avcapturephotooutput/capturephoto%28with,delegate%29.md) method. If your settings don’t meet these requirements, that method raises an exception.

## See Also

### Configuring photo settings
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
- [var isDualCameraDualPhotoDeliveryEnabled: Bool](./isdualcameradualphotodeliveryenabled.md)
  A Boolean value that determines whether a dual camera device delivers images from both cameras.
- [var isAutoDualCameraFusionEnabled: Bool](./isautodualcamerafusionenabled.md)
  A Boolean value that specifies whether captures automatically combine data from a dual camera device.
- [var isAutoStillImageStabilizationEnabled: Bool](./isautostillimagestabilizationenabled.md)
  A Boolean value that specifies whether captures use automatic image stabilization.
- [var isHighResolutionPhotoEnabled: Bool](./ishighresolutionphotoenabled.md)
  A Boolean value that specifies whether to capture still images at the highest resolution supported by the active device and format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/flashmode)*