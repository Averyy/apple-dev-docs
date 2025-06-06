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

Setting the property to the special value of [`invalid`](https://developer.apple.com/documentation/coremedia/cmtime/1400807-invalid) resets the autoexposure maximum duration to the device’s default for your current configuration. When the device’s [`activeFormat`](avcapturedevice/activeformat.md) or the capture session’s [`sessionPreset`](avcapturesession/sessionpreset.md) changes, this property resets to the default max exposure duration for the new format or session preset.

On some devices, the auto exposure algorithm picks a different maximum exposure duration for a given format depending on whether you used the [`sessionPreset`](avcapturesession/sessionpreset.md) or [`activeFormat`](avcapturedevice/activeformat.md) APIs to set to set the format. To ensure uniform default handling of maximum exposure duration, set the value of a capture input’s [`unifiedAutoExposureDefaultsEnabled`](avcapturedeviceinput/unifiedautoexposuredefaultsenabled.md) property to [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var exposureDuration: CMTime](avcapturedevice/exposureduration.md)
  The length of time over which exposure takes place.
- [var iso: Float](avcapturedevice/iso.md)
  The current exposure ISO value.
- [var lensAperture: Float](avcapturedevice/lensaperture.md)
  The size of the lens diaphragm.
- [func setExposureModeCustom(duration: CMTime, iso: Float, completionHandler: ((CMTime) -> Void)?)](avcapturedevice/setexposuremodecustom(duration:iso:completionhandler:).md)
  Sets the exposure mode to a custom state, and locks exposure duration and ISO at explicit values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/activemaxexposureduration)*