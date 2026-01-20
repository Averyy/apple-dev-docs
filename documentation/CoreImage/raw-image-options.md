# RAW Image Options

**Framework**: Core Image

Options for creating a [`CIFilter`](cifilter-swift.class.md) object from RAW image data.

#### Overview

You can also use the key [`kCIInputEVKey`](kciinputevkey.md) for RAW images.

## Topics

### Constants
- [static let decoderVersion: CIRAWFilterOption](cirawfilteroption/decoderversion.md)
  A key for the version number of the method to be used for decoding. A newly initialized object defaults to the newest available decoder version for the given image type. You can request an alternative, older version to maintain compatibility with older releases. Must be one of the values listed for the [`supportedDecoderVersions`](cirawfilteroption/supporteddecoderversions.md) key, otherwise a `nil` output image is generated. The associated value must be an `NSNumber` object that specifies an integer value in range of `0` to the current decoder version. When you request a specific version of the decoder, Core Image produces an image that is  the same across different versions of the operating system. Core Image, however, does not guarantee that  the same bits are produced across different versions of the operating system. That’s because the rounding behavior of floating-point arithmetic can vary due to differences in compilers or hardware. Note that this option has no effect if the image used for initialization is not RAW.
- [static let supportedDecoderVersions: CIRAWFilterOption](cirawfilteroption/supporteddecoderversions.md)
  A key for the supported decoder versions.
- [static let boostAmount: CIRAWFilterOption](cirawfilteroption/boostamount.md)
  A key for the amount of boost to apply to an image.
- [static let neutralChromaticityX: CIRAWFilterOption](cirawfilteroption/neutralchromaticityx.md)
  The x value of the chromaticity.
- [static let neutralChromaticityY: CIRAWFilterOption](cirawfilteroption/neutralchromaticityy.md)
  The y value of the chromaticity.
- [static let neutralTemperature: CIRAWFilterOption](cirawfilteroption/neutraltemperature.md)
  A key for neutral temperature.
- [static let neutralTint: CIRAWFilterOption](cirawfilteroption/neutraltint.md)
  A key for the neutral tint.
- [static let neutralLocation: CIRAWFilterOption](cirawfilteroption/neutrallocation.md)
  A key for the neutral position. Use this key to set the location in geometric coordinates of the unrotated output image that should be used as neutral. You cannot query this value; it is undefined for reading. The associated value is a two-element [`CIVector`](civector.md) object that specifies the location (`x`, `y`).
- [static let scaleFactor: CIRAWFilterOption](cirawfilteroption/scalefactor.md)
  A key for the scale factor.
- [static let allowDraftMode: CIRAWFilterOption](cirawfilteroption/allowdraftmode.md)
  A key for allowing draft mode.
- [static let ignoreImageOrientation: CIRAWFilterOption](cirawfilteroption/ignoreimageorientation.md)
  A key for specifying whether to ignore the image orientation
- [static let imageOrientation: CIRAWFilterOption](cirawfilteroption/imageorientation.md)
  A key for the image orientation.
- [static let enableSharpening: CIRAWFilterOption](cirawfilteroption/enablesharpening.md)
  A key for the sharpening state.
- [static let enableChromaticNoiseTracking: CIRAWFilterOption](cirawfilteroption/enablechromaticnoisetracking.md)
  A key for progressive chromatic noise tracking (based on ISO and exposure time).
- [static let noiseReductionAmount: CIRAWFilterOption](cirawfilteroption/noisereductionamount.md)
  A key for the amount to reduce noise in the image.
- [static let enableVendorLensCorrection: CIRAWFilterOption](cirawfilteroption/enablevendorlenscorrection.md)
  A key for whether to automatically correct for image distortion from known lenses.
- [static let luminanceNoiseReductionAmount: CIRAWFilterOption](cirawfilteroption/luminancenoisereductionamount.md)
  A key for the amount of noise reduction to apply to luminance data in the image.
- [static let colorNoiseReductionAmount: CIRAWFilterOption](cirawfilteroption/colornoisereductionamount.md)
  A key for the amount of noise reduction to apply to color data in the image.
- [static let noiseReductionSharpnessAmount: CIRAWFilterOption](cirawfilteroption/noisereductionsharpnessamount.md)
  A key for the amount of sharpness enhancement to apply during noise reduction.
- [static let noiseReductionContrastAmount: CIRAWFilterOption](cirawfilteroption/noisereductioncontrastamount.md)
  A key for the amount of contrast enhancement to apply during noise reduction.
- [static let noiseReductionDetailAmount: CIRAWFilterOption](cirawfilteroption/noisereductiondetailamount.md)
  A key for the amount of detail enhancement to apply during noise reduction.
- [static let boostShadowAmount: CIRAWFilterOption](cirawfilteroption/boostshadowamount.md)
  A key for the amount to boost the shadow areas of the image.
- [let kCIInputBiasKey: String](kciinputbiaskey.md)
  Simple bias value.
- [static let linearSpaceFilter: CIRAWFilterOption](cirawfilteroption/linearspacefilter.md)
  A key for the filter to apply to the image while it is temporarily in a linear color space as part of  RAW image processing. The associated value must be a [`CIFilter`](cifilter-swift.class.md) object.
- [static let outputNativeSize: CIRAWFilterOption](cirawfilteroption/outputnativesize.md)
  A key for the full native size of the original, non-transformed RAW image. The associated value is a [`CIVector`](civector.md) object whose X and Y values are the image’s width and height. This key is read-only.
- [static let activeKeys: CIRAWFilterOption](cirawfilteroption/activekeys.md)
  A key for the set of input keys available for use.

## See Also

- [Filter Attribute Keys](filter-attribute-keys.md)
  Attributes for a filter and its parameters.
- [Data Type Attributes](data-type-attributes.md)
  Numeric data types.
- [Vector Quantity Attributes](vector-quantity-attributes.md)
  Vector data types.
- [Color Attribute Keys](color-attribute-keys.md)
  Color types.
- [Image Attribute Keys](image-attribute-keys.md)
  Image Types
- [Filter Category Keys](filter-category-keys.md)
  Categories of filters.
- [Options for Applying a Filter](options-for-applying-a-filter.md)
  Options that control the application of a custom Core Image filter.
- [User Interface Control Options](user-interface-control-options.md)
  Sets of controls for various user scenarios.
- [User Interface Options](user-interface-options.md)
  Keys or values for the size of the input parameter controls for a filter view.
- [Filter Parameter Keys](filter-parameter-keys.md)
  Keys for input parameters to filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/raw-image-options)*