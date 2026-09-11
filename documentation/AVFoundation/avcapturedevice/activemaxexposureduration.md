# activeMaxExposureDuration

**Framework**: AVFoundation  
**Kind**: property

The maximum exposure duration, in seconds, defined in the autoexposure algorithm.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var activeMaxExposureDuration: CMTime { get set }
```

#### Discussion

When you set the exposureMode to [`AVCaptureDevice.ExposureMode.autoExpose`](avcapturedevice/exposuremode-swift.enum/autoexpose.md) or [`AVCaptureDevice.ExposureMode.continuousAutoExposure`](avcapturedevice/exposuremode-swift.enum/continuousautoexposure.md), the autoexposure algorithm picks a default maximum exposure duration that’s tuned for the current configuration, balancing low light image quality with motion preservation. By querying or key-value observing this property, you can determine the current maximum exposure duration in use.

You may also override the default value by setting this property to a value between the format’s [`minExposureDuration`](avcapturedevice/format/minexposureduration.md) and [`maxExposureDuration`](avcapturedevice/format/maxexposureduration.md) values. The system throws an exception if you pass an out-of-bounds exposure value.

Setting the property to the special value of [`invalid`](https://developer.apple.com/documentation/coremedia/cmtime/invalid) resets the autoexposure maximum duration to the device’s default for your current configuration. When the device’s [`activeFormat`](avcapturedevice/activeformat.md) or the capture session’s [`sessionPreset`](avcapturesession/sessionpreset.md) changes, this property resets to the default max exposure duration for the new format or session preset.

On some devices, the auto exposure algorithm picks a different maximum exposure duration for a given format depending on whether you used the [`sessionPreset`](avcapturesession/sessionpreset.md) or [`activeFormat`](avcapturedevice/activeformat.md) APIs to set to set the format. To ensure uniform default handling of maximum exposure duration, set the value of a capture input’s [`unifiedAutoExposureDefaultsEnabled`](avcapturedeviceinput/unifiedautoexposuredefaultsenabled.md) property to [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [func setExposureModeCustom(duration: CMTime, iso: Float, completionHandler: ((CMTime) -> Void)?)](avcapturedevice/setexposuremodecustom(duration:iso:completionhandler:).md)
  Sets the exposure mode to a custom state, and locks exposure duration and ISO at explicit values.
- [func setExposureModeCustom(lensAperture: Float, duration: CMTime, iso: Float, completionHandler: ((CMTime) -> Void)?)](avcapturedevice/setexposuremodecustom(lensaperture:duration:iso:completionhandler:).md)
  Sets a custom exposure mode with the specified lens aperture, exposure duration, and ISO values.
- [class let autoExposureDuration: CMTime](avcapturedevice/autoexposureduration.md)
  A special value that may be passed as the duration parameter of a device’s `setExposureModeCustom...` methods to allow the system’s auto-exposure system to manage the exposure duration.
- [class let autoISO: Float](avcapturedevice/autoiso.md)
  A special value that may be passed as the ISO parameter of a device’s `setExposureModeCustom...` methods to allow the system’s auto-exposure system to manage the gain value.
- [class let autoLensAperture: Float](avcapturedevice/autolensaperture.md)
  A special value that may be passed as the lensAperture parameter of a device’s `setExposureModeCustom...` methods to allow the system’s auto-exposure system to manage the aperture.
- [class let currentLensAperture: Float](avcapturedevice/currentlensaperture.md)
  A special value that may be passed as the lensAperture parameter of a device’s `setExposureModeCustom...` methods to lock at the current position.
- [var exposureDuration: CMTime](avcapturedevice/exposureduration.md)
  The length of time over which exposure takes place.
- [var iso: Float](avcapturedevice/iso.md)
  The current exposure ISO value.
- [var lensAperture: Float](avcapturedevice/lensaperture.md)
  The size of the lens diaphragm.
- [var automaticallyAdjustsExposureDuration: Bool](avcapturedevice/automaticallyadjustsexposureduration.md)
  This property reports true whenever exposureDuration is unlocked, either by setting exposureMode to one of the automatic modes, or by passing `AVCaptureExposureDurationAuto` to the duration parameter of [`setExposureModeCustom(duration:iso:completionHandler:)`](avcapturedevice/setexposuremodecustom(duration:iso:completionhandler:).md) or [`setExposureModeCustom(lensAperture:duration:iso:completionHandler:)`](avcapturedevice/setexposuremodecustom(lensaperture:duration:iso:completionhandler:).md).
- [var automaticallyAdjustsISO: Bool](avcapturedevice/automaticallyadjustsiso.md)
  This property reports true whenever ISO is unlocked, either by setting exposureMode to one of the automatic modes, or by passing `AVCaptureISOAuto` to the ISO parameter of [`setExposureModeCustom(duration:iso:completionHandler:)`](avcapturedevice/setexposuremodecustom(duration:iso:completionhandler:).md) or [`setExposureModeCustom(lensAperture:duration:iso:completionHandler:)`](avcapturedevice/setexposuremodecustom(lensaperture:duration:iso:completionhandler:).md).
- [var automaticallyAdjustsLensAperture: Bool](avcapturedevice/automaticallyadjustslensaperture.md)
  This property reports true whenever lensAperture is unlocked, either by setting exposureMode to one of the automatic modes, or by passing `AVCaptureLensApertureAuto` to the aperture parameter of [`setExposureModeCustom(lensAperture:duration:iso:completionHandler:)`](avcapturedevice/setexposuremodecustom(lensaperture:duration:iso:completionhandler:).md).
- [var autoExposureLensApertureRateLimit: Float](avcapturedevice/autoexposurelensapertureratelimit.md)
  Specifies a rate limit for aperture motion, whenever auto-exposure is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/activemaxexposureduration)*