# extendedDynamicRangeAmount

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

A value that indicates the amount of extended dynamic range (EDR) to apply to the image.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var extendedDynamicRangeAmount: Float { get set }
```

```objc
@property (readwrite) float extendedDynamicRangeAmount;
```

#### Discussion

The value should be in the range of `0...2`. The default value is `0`. A value of `0` indicates no EDR. A value of `1` indicates default EDR, and a value of `2` indicates maximum EDR.

## See Also

### Configuring a filter
- [var baselineExposure: Float](./baselineexposure.md)
  A value that indicates the baseline exposure to apply to the image.
- [var boostAmount: Float](./boostamount.md)
  A value that indicates the amount of global tone curve to apply to the image.
- [var boostShadowAmount: Float](./boostshadowamount.md)
  A value that indicates the amount to boost the shadow areas of the image.
- [var colorNoiseReductionAmount: Float](./colornoisereductionamount.md)
  A value that indicates the amount of chroma noise reduction to apply to the image.
- [var contrastAmount: Float](./contrastamount.md)
  A value that indicates the amount of local contrast to apply to the edges of the image.
- [var decoderVersion: CIRAWDecoderVersion](./decoderversion.md)
  A value that indicates the decoder version to use.
- [var detailAmount: Float](./detailamount.md)
  A value that indicates the amount of detail enhancement to apply to the edges of the image.
- [var exposure: Float](./exposure.md)
  A value that indicates the amount of exposure to apply to the image.
- [var isDraftModeEnabled: Bool](./isdraftmodeenabled.md)
  A Boolean that indicates whether to enable draft mode.
- [var isGamutMappingEnabled: Bool](./isgamutmappingenabled.md)
  A Boolean that indicates whether to enable gamut mapping.
- [var isLensCorrectionEnabled: Bool](./islenscorrectionenabled.md)
  A Boolean that indicates whether to enable lens correction.
- [var linearSpaceFilter: CIFilter?](./linearspacefilter.md)
  An optional filter you can apply to the RAW image while it’s in linear space.
- [var localToneMapAmount: Float](./localtonemapamount.md)
  A value that indicates the amount of local tone curve to apply to the image.
- [var luminanceNoiseReductionAmount: Float](./luminancenoisereductionamount.md)
  A value that indicates the amount of luminance noise reduction to apply to the image.
- [var moireReductionAmount: Float](./moirereductionamount.md)
  A value that indicates the amount of moire artifact reduction to apply to high frequency areas of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirawfilter/extendeddynamicrangeamount)*