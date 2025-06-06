# apertureMode

**Framework**: AVFoundation  
**Kind**: property

Specifies the aperture mode for the generated image.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var apertureMode: AVAssetImageGenerator.ApertureMode? { get set }
```

#### Discussion

The default value is [`cleanAperture`](avassetimagegenerator/aperturemode-swift.struct/cleanaperture.md).

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
- [var appliesPreferredTrackTransform: Bool](avassetimagegenerator/appliespreferredtracktransform.md)
  A Boolean value that specifies whether to apply the track matrix or matrices when generating an image from the asset.
- [AVAssetImageGenerator.ApertureMode](avassetimagegenerator/aperturemode-swift.struct.md)
  Constants that define aperture modes to use when generating images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/aperturemode-swift.property)*