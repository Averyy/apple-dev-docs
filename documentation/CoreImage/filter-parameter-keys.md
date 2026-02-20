# Filter Parameter Keys

**Framework**: Core Image

Keys for input parameters to filters.

#### Overview

These keys represent some of the most commonly used input parameters. A filter can use other kinds of input parameters.

## Topics

### Constants
- [static let constrainedHigh: CIDynamicRangeOption](cidynamicrangeoption/constrainedhigh.md)
  Use extended dynamic range, but brightness is modulated to optimize for co-existence with other composited content.
- [static let high: CIDynamicRangeOption](cidynamicrangeoption/high.md)
  Use High dynamic range.
- [static let standard: CIDynamicRangeOption](cidynamicrangeoption/standard.md)
  Use Standard dynamic range.
- [let kCIInputAmountKey: String](kciinputamountkey.md)
- [let kCIInputAngleKey: String](kciinputanglekey.md)
  The angle.
- [let kCIInputAspectRatioKey: String](kciinputaspectratiokey.md)
  Aspect Ratio.
- [let kCIInputBackgroundImageKey: String](kciinputbackgroundimagekey.md)
  A key for the [`CIImage`](ciimage.md) object to use as a background image.
- [let kCIInputBacksideImageKey: String](kciinputbacksideimagekey.md)
  A key to get or set the backside image for a transition Core Image filter.
- [let kCIInputBiasVectorKey: String](kciinputbiasvectorkey.md)
  A key to get or set the vector bias value of a Core Image filter.
- [let kCIInputBrightnessKey: String](kciinputbrightnesskey.md)
  Brightness level.
- [let kCIInputCenterKey: String](kciinputcenterkey.md)
  A key for a [`CIVector`](civector.md) object that specifies the center of the area, as   and  - coordinates, to be filtered.
- [let kCIInputColorKey: String](kciinputcolorkey.md)
  A key for a [`CIColor`](cicolor.md) object that specifies a color value.
- [let kCIInputColor0Key: String](kciinputcolor0key.md)
  A key to get or set a color value of a Core Image filter.
- [let kCIInputColor1Key: String](kciinputcolor1key.md)
  A key to get or set a color value of a Core Image filter.
- [let kCIInputColorSpaceKey: String](kciinputcolorspacekey.md)
  A key to get or set a color space value of a Core Image filter.
- [let kCIInputContrastKey: String](kciinputcontrastkey.md)
  A contrast level.
- [let kCIInputCountKey: String](kciinputcountkey.md)
  A key to get or set the scalar count value of a Core Image filter.
- [let kCIInputDepthImageKey: String](kciinputdepthimagekey.md)
  A key for an image with depth values.
- [let kCIInputDisparityImageKey: String](kciinputdisparityimagekey.md)
  A key for an image with disparity values.
- [let kCIInputEVKey: String](kciinputevkey.md)
  How many F-stops brighter or darker the image should be.
- [let kCIInputExtentKey: String](kciinputextentkey.md)
  A key for a [`CIVector`](civector.md) object that specifies a rectangle that defines the extent of the effect.
- [let kCIInputExtrapolateKey: String](kciinputextrapolatekey.md)
  A key to get or set the boolean behavior of a Core Image filter that specifies if the filter should extrapolate a table beyond the defined range.
- [let kCIInputGradientImageKey: String](kciinputgradientimagekey.md)
  A key for a [`CIImage`](ciimage.md) object that specifies an environment map with alpha. Typically, this image contains highlight and shadow.
- [let kCIInputImageKey: String](kciinputimagekey.md)
  A key for the [`CIImage`](ciimage.md) object to use as an input image. For filters that also use a background image, this key refers to the foreground image.
- [let kCIInputIntensityKey: String](kciinputintensitykey.md)
  An intensity value.
- [let kCIInputMaskImageKey: String](kciinputmaskimagekey.md)
  A key for a [`CIImage`](ciimage.md) object to use as a mask.
- [let kCIInputMatteImageKey: String](kciinputmatteimagekey.md)
- [let kCIInputPaletteImageKey: String](kciinputpaletteimagekey.md)
  A key to get or set the palette image for a  Core Image filter.
- [let kCIInputPerceptualKey: String](kciinputperceptualkey.md)
  A key to get or set the boolean behavior of a Core Image filter that specifies if the filter should operate in linear or perceptual colors.
- [let kCIInputPoint0Key: String](kciinputpoint0key.md)
  A key to get or set the coordinate value of a Core Image filter.
The value for this key needs to be a [`CIVector`](civector.md) instance containing the `x,y` coordinate.
- [let kCIInputPoint1Key: String](kciinputpoint1key.md)
  A key to get or set a coordinate value of a Core Image filter.
The value for this key needs to be a [`CIVector`](civector.md) instance containing the `x,y` coordinate.
- [let kCIInputRadiusKey: String](kciinputradiuskey.md)
  The distance from the center of an effect.
- [let kCIInputRadius0Key: String](kciinputradius0key.md)
  A key to get or set the geometric radius value of a Core Image filter.
- [let kCIInputRadius1Key: String](kciinputradius1key.md)
  A key to get or set the geometric radius value of a Core Image filter.
- [let kCIInputRefractionKey: String](kciinputrefractionkey.md)
  The index of refraction to use.
- [let kCIInputSaturationKey: String](kciinputsaturationkey.md)
  The amount to adjust the saturation.
- [let kCIInputScaleKey: String](kciinputscalekey.md)
  The amount of scale to apply.
- [let kCIInputShadingImageKey: String](kciinputshadingimagekey.md)
  A key for a [`CIImage`](ciimage.md) object  that specifies an environment map with alpha values. Typically this image contains highlight and shadow.
- [let kCIInputSharpnessKey: String](kciinputsharpnesskey.md)
  Amount of sharpening to apply.
- [let kCIInputTargetImageKey: String](kciinputtargetimagekey.md)
  A key for a [`CIImage`](ciimage.md) object that is the target image for a transition.
- [let kCIInputThresholdKey: String](kciinputthresholdkey.md)
  A key to get or set the scalar threshold value of a Core Image filter.
- [let kCIInputTimeKey: String](kciinputtimekey.md)
  Specify a time.
- [let kCIInputTransformKey: String](kciinputtransformkey.md)
  Transformation to apply.
- [let kCIInputVersionKey: String](kciinputversionkey.md)
  Version Key
- [let kCIInputWeightsKey: String](kciinputweightskey.md)
  A key for a [`CIVector`](civector.md) object that describes a weight matrix for use with a convolution filter.
- [let kCIInputWidthKey: String](kciinputwidthkey.md)
  A key for a scalar value that specifies the width of the effect.
- [let kCIOutputImageKey: String](kcioutputimagekey.md)
  A key for the [`CIImage`](ciimage.md) object produced by a filter.
### Deprecated
- [static let baselineExposure: CIRAWFilterOption](cirawfilteroption/baselineexposure.md)
  The amount of baseline exposure applied.
- [static let disableGamutMap: CIRAWFilterOption](cirawfilteroption/disablegamutmap.md)
  Whether or not to disable gamut mapping.
- [static let moireAmount: CIRAWFilterOption](cirawfilteroption/moireamount.md)
  The amount of moiré reduction to apply.

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
- [RAW Image Options](raw-image-options.md)
  Options for creating a [`CIFilter`](cifilter-swift.class.md) object from RAW image data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/filter-parameter-keys)*