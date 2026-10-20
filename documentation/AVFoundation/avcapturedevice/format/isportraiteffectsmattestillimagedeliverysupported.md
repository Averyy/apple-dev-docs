# isPortraitEffectsMatteStillImageDeliverySupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean indicating whether the device supports portrait matte effects in still-image capture.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isPortraitEffectsMatteStillImageDeliverySupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isPortraitEffectsMatteStillImageDeliverySupported) BOOL portraitEffectsMatteStillImageDeliverySupported;
```

## See Also

### Determining Portrait Effects support
- [var isPortraitEffectSupported: Bool](./isportraiteffectsupported.md)
  A Boolean value that indicates whether the format supports the Portrait Effect feature.
- [var videoFrameRateRangeForPortraitEffect: AVFrameRateRange?](./videoframeraterangeforportraiteffect.md)
  The range of frame rates available when Portrait Effect is active.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/isportraiteffectsmattestillimagedeliverysupported)*