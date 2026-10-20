# nativeSize

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

The full native size of the unscaled image.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var nativeSize: CGSize { get }
```

```objc
@property (readonly) CGSize nativeSize;
```

#### Discussion

This value isn’t affected by orientation changes.

## See Also

### Inspecting supported camera models, decoders, and filters
- [class var supportedCameraModels: [String]](./supportedcameramodels.md)
  An array containing the names of all supported camera models.
- [var supportedDecoderVersions: [CIRAWDecoderVersion]](./supporteddecoderversions.md)
  An array of all supported decoder versions for the given image type.
- [struct CIRAWDecoderVersion](../cirawdecoderversion.md)
- [var isColorNoiseReductionSupported: Bool](./iscolornoisereductionsupported.md)
  A Boolean that indicates if the current image supports color noise reduction adjustments.
- [var isContrastSupported: Bool](./iscontrastsupported.md)
  A Boolean that indicates if the current image supports contrast adjustments.
- [var isDetailSupported: Bool](./isdetailsupported.md)
  A Boolean that indicates if the current image supports detail enhancement adjustments.
- [var isLensCorrectionSupported: Bool](./islenscorrectionsupported.md)
  A Boolean that indicates if you can enable lens correction for the current image.
- [var isLocalToneMapSupported: Bool](./islocaltonemapsupported.md)
  A Boolean that indicates if the current image supports local tone curve adjustments.
- [var isLuminanceNoiseReductionSupported: Bool](./isluminancenoisereductionsupported.md)
  A Boolean that indicates if the current image supports luminance noise reduction adjustments.
- [var isMoireReductionSupported: Bool](./ismoirereductionsupported.md)
  A Boolean that indicates if the current image supports moire artifact reduction adjustments.
- [var isSharpnessSupported: Bool](./issharpnesssupported.md)
  A Boolean that indicates if the current image supports sharpness adjustments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirawfilter/nativesize)*