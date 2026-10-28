# exposureDuration

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The length of time over which exposure takes place.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var exposureDuration: CMTime { get }
```

```objc
@property (nonatomic, readonly) CMTime exposureDuration;
```

## Discussion

The exposure duration is between the active format’s [`minExposureDuration`](./format/minexposureduration.md) and [`maxExposureDuration`](./format/maxexposureduration.md).

To set the exposure duration, call the [`setExposureModeCustom(duration:iso:completionHandler:)`](./setexposuremodecustom%28duration,iso,completionhandler%29.md) method.

This property is key-value observable.

## See Also

### Configuring exposure manually
- [func setExposureModeCustom(duration: CMTime, iso: Float, completionHandler: ((CMTime) -> Void)?)](./setexposuremodecustom%28duration,iso,completionhandler%29.md)
  Sets the exposure mode to a custom state, and locks exposure duration and ISO at explicit values.
- [func setExposureModeCustom(lensAperture: Float, duration: CMTime, iso: Float, completionHandler: ((CMTime) -> Void)?)](./setexposuremodecustom%28lensaperture,duration,iso,completionhandler%29.md)
  Sets a custom exposure mode with the specified lens aperture, exposure duration, and ISO values.
- [class let autoExposureDuration: CMTime](./autoexposureduration.md)
  A special value that may be passed as the duration parameter of a device’s `setExposureModeCustom...` methods to allow the system’s auto-exposure system to manage the exposure duration.
- [class let autoISO: Float](./autoiso.md)
  A special value that may be passed as the ISO parameter of a device’s `setExposureModeCustom...` methods to allow the system’s auto-exposure system to manage the gain value.
- [class let autoLensAperture: Float](./autolensaperture.md)
  A special value that may be passed as the lensAperture parameter of a device’s `setExposureModeCustom...` methods to allow the system’s auto-exposure system to manage the aperture.
- [class let currentLensAperture: Float](./currentlensaperture.md)
  A special value that may be passed as the lensAperture parameter of a device’s `setExposureModeCustom...` methods to lock at the current position.
- [var iso: Float](./iso.md)
  The current exposure ISO value.
- [var lensAperture: Float](./lensaperture.md)
  The size of the lens diaphragm.
- [var activeMaxExposureDuration: CMTime](./activemaxexposureduration.md)
  The maximum exposure duration, in seconds, defined in the autoexposure algorithm.
- [var automaticallyAdjustsExposureDuration: Bool](./automaticallyadjustsexposureduration.md)
  This property reports true whenever exposureDuration is unlocked, either by setting exposureMode to one of the automatic modes, or by passing `AVCaptureExposureDurationAuto` to the duration parameter of [`setExposureModeCustom(duration:iso:completionHandler:)`](./setexposuremodecustom%28duration,iso,completionhandler%29.md) or [`setExposureModeCustom(lensAperture:duration:iso:completionHandler:)`](./setexposuremodecustom%28lensaperture,duration,iso,completionhandler%29.md).
- [var automaticallyAdjustsISO: Bool](./automaticallyadjustsiso.md)
  This property reports true whenever ISO is unlocked, either by setting exposureMode to one of the automatic modes, or by passing `AVCaptureISOAuto` to the ISO parameter of [`setExposureModeCustom(duration:iso:completionHandler:)`](./setexposuremodecustom%28duration,iso,completionhandler%29.md) or [`setExposureModeCustom(lensAperture:duration:iso:completionHandler:)`](./setexposuremodecustom%28lensaperture,duration,iso,completionhandler%29.md).
- [var automaticallyAdjustsLensAperture: Bool](./automaticallyadjustslensaperture.md)
  This property reports true whenever lensAperture is unlocked, either by setting exposureMode to one of the automatic modes, or by passing `AVCaptureLensApertureAuto` to the aperture parameter of [`setExposureModeCustom(lensAperture:duration:iso:completionHandler:)`](./setexposuremodecustom%28lensaperture,duration,iso,completionhandler%29.md).
- [var autoExposureLensApertureRateLimit: Float](./autoexposurelensapertureratelimit.md)
  Specifies a rate limit for aperture motion, whenever auto-exposure is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/exposureduration)*