# supportedDecoderVersions

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

An array of all supported decoder versions for the given image type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var supportedDecoderVersions: [CIRAWDecoderVersion] { get }
```

```objc
@property (readonly) NSArray<NSString *> * supportedDecoderVersions;
```

## Discussion

This array is sorted in reverse chronological order. All entries represent a valid version identifier set to [`decoderVersion`](./decoderversion.md).

## See Also

### Inspecting supported camera models, decoders, and filters
- [class var supportedCameraModels: [String]](./supportedcameramodels.md)
  An array containing the names of all supported camera models.
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
- [var nativeSize: CGSize](./nativesize.md)
  The full native size of the unscaled image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirawfilter/supporteddecoderversions)*