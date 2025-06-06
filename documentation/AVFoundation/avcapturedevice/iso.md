# iso

**Framework**: AVFoundation  
**Kind**: property

The current exposure ISO value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var iso: Float { get }
```

#### Discussion

This property controls the sensor’s sensitivity to light by applying a gain value to the signal. This value is between the active format’s [`minISO`](avcapturedevice/format/miniso.md) and [`maxISO`](avcapturedevice/format/maxiso.md) values. Higher values result in noisier images.

To set the ISO, call the [`setExposureModeCustom(duration:iso:completionHandler:)`](avcapturedevice/setexposuremodecustom(duration:iso:completionhandler:).md) method.

This property is key-value observable.

## See Also

- [var exposureDuration: CMTime](avcapturedevice/exposureduration.md)
  The length of time over which exposure takes place.
- [var activeMaxExposureDuration: CMTime](avcapturedevice/activemaxexposureduration.md)
  The maximum exposure duration, in seconds, defined in the autoexposure algorithm.
- [var lensAperture: Float](avcapturedevice/lensaperture.md)
  The size of the lens diaphragm.
- [func setExposureModeCustom(duration: CMTime, iso: Float, completionHandler: ((CMTime) -> Void)?)](avcapturedevice/setexposuremodecustom(duration:iso:completionhandler:).md)
  Sets the exposure mode to a custom state, and locks exposure duration and ISO at explicit values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/iso)*