# isCameraSensorOrientationCompensationSupported

**Framework**: AVFoundation  
**Kind**: property

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var isCameraSensorOrientationCompensationSupported: Bool { get }
```

#### Discussion

A read-only BOOL value indicating whether still image buffers may be rotated to match the sensor orientation of earlier generation hardware.

Value is YES for camera configurations which support compensation for the sensor orientation, which is applied to HEIC, JPEG, and uncompressed processed photos only; compensation is never applied to Bayer RAW or Apple ProRaw captures.

## See Also

- [var isCameraSensorOrientationCompensationEnabled: Bool](avcapturephotooutput/iscamerasensororientationcompensationenabled.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/iscamerasensororientationcompensationsupported)*