# lensAperture

**Framework**: AVFoundation  
**Kind**: property

The size of the lens diaphragm.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var lensAperture: Float { get }
```

#### Discussion

The value of this property is a float indicating the size (the `f` number) of the lens diaphragm.

This value doesn’t change.

## See Also

- [var exposureDuration: CMTime](avcapturedevice/exposureduration.md)
  The length of time over which exposure takes place.
- [var activeMaxExposureDuration: CMTime](avcapturedevice/activemaxexposureduration.md)
  The maximum exposure duration, in seconds, defined in the autoexposure algorithm.
- [var iso: Float](avcapturedevice/iso.md)
  The current exposure ISO value.
- [func setExposureModeCustom(duration: CMTime, iso: Float, completionHandler: ((CMTime) -> Void)?)](avcapturedevice/setexposuremodecustom(duration:iso:completionhandler:).md)
  Sets the exposure mode to a custom state, and locks exposure duration and ISO at explicit values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/lensaperture)*