# boostShadowAmount

**Framework**: Core Image  
**Kind**: property  
**Role**: Type Property

A key for the amount to boost the shadow areas of the image.

**Availability**:
- iOS 10.0+ - Deprecated in 27.2
- iPadOS 10.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.5+ - Deprecated in 27.2
- tvOS 10.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use new CIRAWFilter class instead.

## Declaration

```swift
static let boostShadowAmount: CIRAWFilterOption
```

```c
extern CIRAWFilterOption const kCIInputBoostShadowAmountKey;
```

## Discussion

The associated value must be an [`NSNumber`](../../Foundation/nsnumber.md) object that specifies floating-point value. The value has no effect if the image used for initialization is not RAW.

## See Also

### Type Properties
- [static let activeKeys: CIRAWFilterOption](./activekeys.md)
  A key for the set of input keys available for use.
- [static let allowDraftMode: CIRAWFilterOption](./allowdraftmode.md)
  A key for allowing draft mode.
- [static let baselineExposure: CIRAWFilterOption](./baselineexposure.md)
  The amount of baseline exposure applied.
- [static let boostAmount: CIRAWFilterOption](./boostamount.md)
  A key for the amount of boost to apply to an image.
- [static let ciInputEnableEDRModeKey: CIRAWFilterOption](./ciinputenableedrmodekey.md)
- [static let ciInputLocalToneMapAmountKey: CIRAWFilterOption](./ciinputlocaltonemapamountkey.md)
- [static let colorNoiseReductionAmount: CIRAWFilterOption](./colornoisereductionamount.md)
  A key for the amount of noise reduction to apply to color data in the image.
- [static let decoderVersion: CIRAWFilterOption](./decoderversion.md)
  A key for the version number of the method to be used for decoding. A newly initialized object defaults to the newest available decoder version for the given image type. You can request an alternative, older version to maintain compatibility with older releases. Must be one of the values listed for the [`supportedDecoderVersions`](./supporteddecoderversions.md) key, otherwise a `nil` output image is generated. The associated value must be an `NSNumber` object that specifies an integer value in range of `0` to the current decoder version. When you request a specific version of the decoder, Core Image produces an image that is *visually* the same across different versions of the operating system. Core Image, however, does not guarantee that  the same bits are produced across different versions of the operating system. That’s because the rounding behavior of floating-point arithmetic can vary due to differences in compilers or hardware. Note that this option has no effect if the image used for initialization is not RAW.
- [static let disableGamutMap: CIRAWFilterOption](./disablegamutmap.md)
  Whether or not to disable gamut mapping.
- [static let enableChromaticNoiseTracking: CIRAWFilterOption](./enablechromaticnoisetracking.md)
  A key for progressive chromatic noise tracking (based on ISO and exposure time).
- [static let enableSharpening: CIRAWFilterOption](./enablesharpening.md)
  A key for the sharpening state.
- [static let enableVendorLensCorrection: CIRAWFilterOption](./enablevendorlenscorrection.md)
  A key for whether to automatically correct for image distortion from known lenses.
- [static let ignoreImageOrientation: CIRAWFilterOption](./ignoreimageorientation.md)
  A key for specifying whether to ignore the image orientation
- [static let imageOrientation: CIRAWFilterOption](./imageorientation.md)
  A key for the image orientation.
- [static let linearSpaceFilter: CIRAWFilterOption](./linearspacefilter.md)
  A key for the filter to apply to the image while it is temporarily in a linear color space as part of  RAW image processing. The associated value must be a [`CIFilter`](../cifilter-swift.class.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cirawfilteroption/boostshadowamount)*