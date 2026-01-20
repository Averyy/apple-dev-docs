# CIRAWDecoderVersion

**Framework**: Core Image  
**Kind**: struct

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct CIRAWDecoderVersion
```

## Topics

### Initializers
- [init(rawValue: String)](cirawdecoderversion/init(rawvalue:).md)
### Type Properties
- [static let none: CIRAWDecoderVersion](cirawdecoderversion/none.md)
- [static let version6: CIRAWDecoderVersion](cirawdecoderversion/version6.md)
- [static let version6DNG: CIRAWDecoderVersion](cirawdecoderversion/version6dng.md)
- [static let version7: CIRAWDecoderVersion](cirawdecoderversion/version7.md)
- [static let version7DNG: CIRAWDecoderVersion](cirawdecoderversion/version7dng.md)
- [static let version8: CIRAWDecoderVersion](cirawdecoderversion/version8.md)
- [static let version8DNG: CIRAWDecoderVersion](cirawdecoderversion/version8dng.md)
- [static let version9: CIRAWDecoderVersion](cirawdecoderversion/version9.md)
- [static let version9DNG: CIRAWDecoderVersion](cirawdecoderversion/version9dng.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class var supportedCameraModels: [String]](cirawfilter/supportedcameramodels.md)
  An array containing the names of all supported camera models.
- [var supportedDecoderVersions: [CIRAWDecoderVersion]](cirawfilter/supporteddecoderversions.md)
  An array of all supported decoder versions for the given image type.
- [var isColorNoiseReductionSupported: Bool](cirawfilter/iscolornoisereductionsupported.md)
  A Boolean that indicates if the current image supports color noise reduction adjustments.
- [var isContrastSupported: Bool](cirawfilter/iscontrastsupported.md)
  A Boolean that indicates if the current image supports contrast adjustments.
- [var isDetailSupported: Bool](cirawfilter/isdetailsupported.md)
  A Boolean that indicates if the current image supports detail enhancement adjustments.
- [var isLensCorrectionSupported: Bool](cirawfilter/islenscorrectionsupported.md)
  A Boolean that indicates if you can enable lens correction for the current image.
- [var isLocalToneMapSupported: Bool](cirawfilter/islocaltonemapsupported.md)
  A Boolean that indicates if the current image supports local tone curve adjustments.
- [var isLuminanceNoiseReductionSupported: Bool](cirawfilter/isluminancenoisereductionsupported.md)
  A Boolean that indicates if the current image supports luminance noise reduction adjustments.
- [var isMoireReductionSupported: Bool](cirawfilter/ismoirereductionsupported.md)
  A Boolean that indicates if the current image supports moire artifact reduction adjustments.
- [var isSharpnessSupported: Bool](cirawfilter/issharpnesssupported.md)
  A Boolean that indicates if the current image supports sharpness adjustments.
- [var nativeSize: CGSize](cirawfilter/nativesize.md)
  The full native size of the unscaled image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirawdecoderversion)*