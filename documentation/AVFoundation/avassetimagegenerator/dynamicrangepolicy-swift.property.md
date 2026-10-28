# dynamicRangePolicy

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The dynamic range policy to use when generating images.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var dynamicRangePolicy: AVAssetImageGenerator.DynamicRangePolicy { get set }
```

```objc
@property (nonatomic, copy) AVAssetImageGeneratorDynamicRangePolicy dynamicRangePolicy;
```

## Discussion

This property defaults to [`forceSDR`](./dynamicrangepolicy-swift.struct/forcesdr.md).

## See Also

### Configuring image generation
- [var maximumSize: CGSize](./maximumsize.md)
  The maximum size of images to generate.
- [var requestedTimeToleranceBefore: CMTime](./requestedtimetolerancebefore.md)
  A maximum length of time before the requested time to allow image generation to occur.
- [var requestedTimeToleranceAfter: CMTime](./requestedtimetoleranceafter.md)
  A maximum length of time after the requested time to allow image generation to occur.
- [AVAssetImageGenerator.DynamicRangePolicy](./dynamicrangepolicy-swift.struct.md)
  A type that specifies the dynamic range policy to apply when generating images.
- [var appliesPreferredTrackTransform: Bool](./appliespreferredtracktransform.md)
  A Boolean value that specifies whether to apply the track matrix or matrices when generating an image from the asset.
- [var apertureMode: AVAssetImageGenerator.ApertureMode?](./aperturemode-swift.property.md)
  Specifies the aperture mode for the generated image.
- [AVAssetImageGenerator.ApertureMode](./aperturemode-swift.struct.md)
  Constants that define aperture modes to use when generating images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/dynamicrangepolicy-swift.property)*