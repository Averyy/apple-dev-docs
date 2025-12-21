# appliesPreferredTrackTransform

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that specifies whether to apply the track matrix or matrices when generating an image from the asset.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var appliesPreferredTrackTransform: Bool { get set }
```

#### Discussion

The default value is [`false`](https://developer.apple.com/documentation/Swift/false). This class only supports rotation by 90, 180, or 270 degrees.

The image generator ignores this property if you set a value for the [`videoComposition`](avassetimagegenerator/videocomposition.md) property.

## See Also

- [var maximumSize: CGSize](avassetimagegenerator/maximumsize.md)
  The maximum size of images to generate.
- [var requestedTimeToleranceBefore: CMTime](avassetimagegenerator/requestedtimetolerancebefore.md)
  A maximum length of time before the requested time to allow image generation to occur.
- [var requestedTimeToleranceAfter: CMTime](avassetimagegenerator/requestedtimetoleranceafter.md)
  A maximum length of time after the requested time to allow image generation to occur.
- [var dynamicRangePolicy: AVAssetImageGenerator.DynamicRangePolicy](avassetimagegenerator/dynamicrangepolicy-swift.property.md)
  The dynamic range policy to use when generating images.
- [AVAssetImageGenerator.DynamicRangePolicy](avassetimagegenerator/dynamicrangepolicy-swift.struct.md)
  A type that specifies the dynamic range policy to apply when generating images.
- [var apertureMode: AVAssetImageGenerator.ApertureMode?](avassetimagegenerator/aperturemode-swift.property.md)
  Specifies the aperture mode for the generated image.
- [AVAssetImageGenerator.ApertureMode](avassetimagegenerator/aperturemode-swift.struct.md)
  Constants that define aperture modes to use when generating images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/appliespreferredtracktransform)*