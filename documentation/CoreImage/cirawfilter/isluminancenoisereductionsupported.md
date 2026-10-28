# isLuminanceNoiseReductionSupported

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates if the current image supports luminance noise reduction adjustments.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var isLuminanceNoiseReductionSupported: Bool { get }
```

```objc
@property (readonly, getter=isLuminanceNoiseReductionSupported) BOOL luminanceNoiseReductionSupported;
```

## Discussion

If this value is `true`, you can adjust the amount of luminance noise reduction to apply to the image by setting [`luminanceNoiseReductionAmount`](./luminancenoisereductionamount.md).

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
- [var isMoireReductionSupported: Bool](./ismoirereductionsupported.md)
  A Boolean that indicates if the current image supports moire artifact reduction adjustments.
- [var isSharpnessSupported: Bool](./issharpnesssupported.md)
  A Boolean that indicates if the current image supports sharpness adjustments.
- [var nativeSize: CGSize](./nativesize.md)
  The full native size of the unscaled image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirawfilter/isluminancenoisereductionsupported)*