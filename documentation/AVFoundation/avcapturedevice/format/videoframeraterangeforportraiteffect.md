# videoFrameRateRangeForPortraitEffect

**Framework**: AVFoundation  
**Kind**: property

The range of frame rates available when Portrait Effect is active.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+

## Declaration

```swift
var videoFrameRateRangeForPortraitEffect: AVFrameRateRange? { get }
```

#### Discussion

Devices may support a limited range of frame rates when Portrait Effect is active. If a device format doesn’t support Portrait Effect, the value of this property is `nil`.

## See Also

- [var isPortraitEffectSupported: Bool](avcapturedevice/format/isportraiteffectsupported.md)
  A Boolean value that indicates whether the format supports the Portrait Effect feature.
- [var isPortraitEffectsMatteStillImageDeliverySupported: Bool](avcapturedevice/format/isportraiteffectsmattestillimagedeliverysupported.md)
  A Boolean indicating whether the device supports portrait matte effects in still-image capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videoframeraterangeforportraiteffect)*