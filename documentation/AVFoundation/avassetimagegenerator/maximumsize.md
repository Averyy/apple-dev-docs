# maximumSize

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The maximum size of images to generate.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var maximumSize: CGSize { get set }
```

```objc
@property (nonatomic) CGSize maximumSize;
```

## Mentions

- [Creating images from a video asset](../creating-images-from-a-video-asset.md)

## Discussion

The default value is [`zero`](../../CoreFoundation/cgsize/zero.md), which generates images at the asset’s unscaled dimensions.

Setting a size scales images to fit their defined bounding boxes. You define the aspect ratio of the scaled image by setting a value for the [`apertureMode`](./aperturemode-swift.property.md) property.

## See Also

### Configuring image generation
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
- [var apertureMode: AVAssetImageGenerator.ApertureMode?](./aperturemode-swift.property.md)
  Specifies the aperture mode for the generated image.
- [AVAssetImageGenerator.ApertureMode](./aperturemode-swift.struct.md)
  Constants that define aperture modes to use when generating images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/maximumsize)*