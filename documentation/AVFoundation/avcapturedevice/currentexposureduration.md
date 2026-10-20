# currentExposureDuration

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

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

```c
extern const CMTime AVCaptureExposureDurationCurrent;
```

#### Discussion

Pass this value to [`setExposureModeCustom(duration:iso:completionHandler:)`](./setexposuremodecustom%28duration,iso,completionhandler%29.md) to lock exposure duration to its current value (that’s, to disable autoexposure).

## See Also

### Exposure constants
- [class let currentISO: Float](./currentiso.md)
  A constant to indicate not to specify a new ISO value, and instead set it to its current value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/currentexposureduration)*