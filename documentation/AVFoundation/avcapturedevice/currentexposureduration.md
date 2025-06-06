# currentExposureDuration

**Framework**: AVFoundation  
**Kind**: property

A special constant representing the current exposure duration setting.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
class let currentExposureDuration: CMTime
```

#### Discussion

Pass this value to [`setExposureModeCustom(duration:iso:completionHandler:)`](avcapturedevice/setexposuremodecustom(duration:iso:completionhandler:).md) to lock exposure duration to its current value (that’s, to disable autoexposure).

## See Also

- [class let currentISO: Float](avcapturedevice/currentiso.md)
  A constant to indicate not to specify a new ISO value, and instead set it to its current value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/currentexposureduration)*