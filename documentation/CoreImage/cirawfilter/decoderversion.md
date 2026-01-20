# decoderVersion

**Framework**: Core Image  
**Kind**: property

A value that indicates the decoder version to use.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var decoderVersion: CIRAWDecoderVersion { get set }
```

#### Discussion

The value should be in the range of `0` to the current decoder version.

A newly initialized object defaults to the newest available decoder version for the given image type. You can request an older version to maintain compatibility with older releases. However, the version you request needs to be a member of [`supportedDecoderVersions`](cirawfilter/supporteddecoderversions.md), otherwise the system generates a `nil` output image.

When you request a specific version of the decoder, Core Image produces an image that looks the same across different versions. However, Core Image doesn’t guarantee that the bits are the same across versions, because the rounding behavior of floating-point arithmetic varies due to differences in compilers or hardware.

## See Also

- [var baselineExposure: Float](cirawfilter/baselineexposure.md)
  A value that indicates the baseline exposure to apply to the image.
- [var boostAmount: Float](cirawfilter/boostamount.md)
  A value that indicates the amount of global tone curve to apply to the image.
- [var boostShadowAmount: Float](cirawfilter/boostshadowamount.md)
  A value that indicates the amount to boost the shadow areas of the image.
- [var colorNoiseReductionAmount: Float](cirawfilter/colornoisereductionamount.md)
  A value that indicates the amount of chroma noise reduction to apply to the image.
- [var contrastAmount: Float](cirawfilter/contrastamount.md)
  A value that indicates the amount of local contrast to apply to the edges of the image.
- [var detailAmount: Float](cirawfilter/detailamount.md)
  A value that indicates the amount of detail enhancement to apply to the edges of the image.
- [var exposure: Float](cirawfilter/exposure.md)
  A value that indicates the amount of exposure to apply to the image.
- [var extendedDynamicRangeAmount: Float](cirawfilter/extendeddynamicrangeamount.md)
  A value that indicates the amount of extended dynamic range (EDR) to apply to the image.
- [var isDraftModeEnabled: Bool](cirawfilter/isdraftmodeenabled.md)
  A Boolean that indicates whether to enable draft mode.
- [var isGamutMappingEnabled: Bool](cirawfilter/isgamutmappingenabled.md)
  A Boolean that indicates whether to enable gamut mapping.
- [var isLensCorrectionEnabled: Bool](cirawfilter/islenscorrectionenabled.md)
  A Boolean that indicates whether to enable lens correction.
- [var linearSpaceFilter: CIFilter?](cirawfilter/linearspacefilter.md)
  An optional filter you can apply to the RAW image while it’s in linear space.
- [var localToneMapAmount: Float](cirawfilter/localtonemapamount.md)
  A value that indicates the amount of local tone curve to apply to the image.
- [var luminanceNoiseReductionAmount: Float](cirawfilter/luminancenoisereductionamount.md)
  A value that indicates the amount of luminance noise reduction to apply to the image.
- [var moireReductionAmount: Float](cirawfilter/moirereductionamount.md)
  A value that indicates the amount of moire artifact reduction to apply to high frequency areas of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirawfilter/decoderversion)*