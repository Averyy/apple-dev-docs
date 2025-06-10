# AVAssetImageGenerator.ApertureMode

**Framework**: AVFoundation  
**Kind**: struct

Constants that define aperture modes to use when generating images.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct ApertureMode
```

## Topics

### Aperture Modes
- [static let cleanAperture: AVAssetImageGenerator.ApertureMode](avassetimagegenerator/aperturemode-swift.struct/cleanaperture.md)
  A mode that applies both pixel aspect ratio and clean aperture.
- [static let encodedPixels: AVAssetImageGenerator.ApertureMode](avassetimagegenerator/aperturemode-swift.struct/encodedpixels.md)
  A mode that applies neither pixel aspect ratio nor clean aperture.
- [static let productionAperture: AVAssetImageGenerator.ApertureMode](avassetimagegenerator/aperturemode-swift.struct/productionaperture.md)
  A mode that applies only pixel aspect ratio.
### Initializers
- [init(rawValue: String)](avassetimagegenerator/aperturemode-swift.struct/init(rawvalue:).md)
  Creates an aperture mode with a string value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [var apertureMode: AVAssetImageGenerator.ApertureMode?](avassetimagegenerator/aperturemode-swift.property.md)
  Specifies the aperture mode for the generated image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator/aperturemode-swift.struct)*