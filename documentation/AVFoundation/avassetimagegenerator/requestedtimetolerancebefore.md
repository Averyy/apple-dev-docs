# requestedTimeToleranceBefore

**Framework**: AVFoundation  
**Kind**: property

A maximum length of time before the requested time to allow image generation to occur.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var requestedTimeToleranceBefore: CMTime { get set }
```

## Mentions

- [Creating images from a video asset](creating-images-from-a-video-asset.md)

#### Discussion

The default value is [`positiveInfinity`](https://developer.apple.com/documentation/coremedia/cmtime/1400789-positiveinfinity). Set the values of [`requestedTimeToleranceBefore`](avassetimagegenerator/requestedtimetolerancebefore.md) and [`requestedTimeToleranceAfter`](avassetimagegenerator/requestedtimetoleranceafter.md) to [`zero`](https://developer.apple.com/documentation/CoreMedia/CMTime/zero) to request frame-accurate image generation; this may incur additional decoding delay.

## See Also

- [var maximumSize: CGSize](avassetimagegenerator/maximumsize.md)
  The maximum size of images to generate.
- [var requestedTimeToleranceAfter: CMTime](avassetimagegenerator/requestedtimetoleranceafter.md)
  A maximum length of time after the requested time to allow image generation to occur.
- [var dynamicRangePolicy: AVAssetImageGenerator.DynamicRangePolicy](avassetimagegenerator/dynamicrangepolicy-swift.property.md)
  The dynamic range policy to use when generating images.
- [AVAssetImageGenerator.DynamicRangePolicy](avassetimagegenerator/dynamicrangepolicy-swift.struct.md)
  A type that specifies the dynamic range policy to apply when generating images.
- [var appliesPreferredTrackTransform: Bool](avassetimagegenerator/appliespreferredtracktransform.md)
  A Boolean value that specifies whether to apply the track matrix or matrices when generating an image from the asset.
- [var apertureMode: AVAssetImageGenerator.ApertureMode?](avassetimagegenerator/aperturemode-swift.property.md)
  Specifies the aperture mode for the generated image.
- [AVAssetImageGenerator.ApertureMode](avassetimagegenerator/aperturemode-swift.struct.md)
  Constants that define aperture modes to use when generating images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/requestedtimetolerancebefore)*