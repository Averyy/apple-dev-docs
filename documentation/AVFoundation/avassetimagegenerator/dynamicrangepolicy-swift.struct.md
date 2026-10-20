# AVAssetImageGenerator.DynamicRangePolicy

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

A type that specifies the dynamic range policy to apply when generating images.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct DynamicRangePolicy
```

```c
typedef NSString * AVAssetImageGeneratorDynamicRangePolicy;
```

## Topics

### Policies
- [static let forceSDR: AVAssetImageGenerator.DynamicRangePolicy](./dynamicrangepolicy-swift.struct/forcesdr.md)
  A policy that forces conversion to standard dynamic range.
- [static let matchSource: AVAssetImageGenerator.DynamicRangePolicy](./dynamicrangepolicy-swift.struct/matchsource.md)
  A policy that preserves the color parameters of the source media.
### Initializers
- [init(rawValue: String)](./dynamicrangepolicy-swift.struct/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [var appliesPreferredTrackTransform: Bool](./appliespreferredtracktransform.md)
  A Boolean value that specifies whether to apply the track matrix or matrices when generating an image from the asset.
- [var apertureMode: AVAssetImageGenerator.ApertureMode?](./aperturemode-swift.property.md)
  Specifies the aperture mode for the generated image.
- [AVAssetImageGenerator.ApertureMode](./aperturemode-swift.struct.md)
  Constants that define aperture modes to use when generating images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/dynamicrangepolicy-swift.struct)*