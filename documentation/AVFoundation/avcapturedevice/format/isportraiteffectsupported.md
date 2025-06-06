# isPortraitEffectSupported

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the format supports the Portrait Effect feature.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+

## Declaration

```swift
var isPortraitEffectSupported: Bool { get }
```

#### Discussion

Enabling a Portrait Effect applies a shallow depth-of-field effect to objects in the background. See the [`isPortraitEffectEnabled`](avcapturedevice/isportraiteffectenabled.md) property of [`AVCaptureDevice`](avcapturedevice.md) for more information.

## See Also

- [var isPortraitEffectsMatteStillImageDeliverySupported: Bool](avcapturedevice/format/isportraiteffectsmattestillimagedeliverysupported.md)
  A Boolean indicating whether the device supports portrait matte effects in still-image capture.
- [var videoFrameRateRangeForPortraitEffect: AVFrameRateRange?](avcapturedevice/format/videoframeraterangeforportraiteffect.md)
  The range of frame rates available when Portrait Effect is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/isportraiteffectsupported)*