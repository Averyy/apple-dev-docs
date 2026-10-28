# apertureMode

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, nullable) AVAssetImageGeneratorApertureMode apertureMode;
```

## Discussion

The default value is [`cleanAperture`](./aperturemode-swift.struct/cleanaperture.md).

## See Also

### Configuring image generation
- [var maximumSize: CGSize](./maximumsize.md)
  The maximum size of images to generate.
- [var requestedTimeToleranceBefore: CMTime](./requestedtimetolerancebefore.md)
  A maximum length of time before the requested time to allow image generation to occur.
- [var requestedTimeToleranceAfter: CMTime](./requestedtimetoleranceafter.md)
  A maximum length of time after the requested time to allow image generation to occur.
- [var dynamicRangePolicy: AVAssetImageGenerator.DynamicRangePolicy](./dynamicrangepolicy-swift.property.md)
  The dynamic range policy to use when generating images.
- [AVAssetImageGenerator.DynamicRangePolicy](./dynamicrangepolicy-swift.struct.md)
  A type that specifies the dynamic range policy to apply when generating images.
- [var appliesPreferredTrackTransform: Bool](./appliespreferredtracktransform.md)
  A Boolean value that specifies whether to apply the track matrix or matrices when generating an image from the asset.
- [AVAssetImageGenerator.ApertureMode](./aperturemode-swift.struct.md)
  Constants that define aperture modes to use when generating images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/aperturemode-swift.property)*