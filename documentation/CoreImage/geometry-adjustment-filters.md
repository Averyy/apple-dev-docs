# Geometry Adjustment Filters

**Framework**: Core Image

Translate, scale, and rotate images in 2D and 3D.

## Topics

### Filters
- [class func bicubicScaleTransform() -> any CIFilter & CIBicubicScaleTransform](cifilter-swift.class/bicubicscaletransform.md)
  Produces a high-quality scaled version of an image.
- [class func edgePreserveUpsample() -> any CIFilter & CIEdgePreserveUpsample](cifilter-swift.class/edgepreserveupsample.md)
  Creates a high-quality upscaled image.
- [class func keystoneCorrectionCombined() -> any CIFilter & CIKeystoneCorrectionCombined](cifilter-swift.class/keystonecorrectioncombined.md)
  Adjusts the image vertically and horizontally to remove distortion.
- [class func keystoneCorrectionHorizontal() -> any CIFilter & CIKeystoneCorrectionHorizontal](cifilter-swift.class/keystonecorrectionhorizontal.md)
  Horizontally adjusts an image to remove distortion.
- [class func keystoneCorrectionVertical() -> any CIFilter & CIKeystoneCorrectionVertical](cifilter-swift.class/keystonecorrectionvertical.md)
  Vertically adjusts an image to remove distortion.
- [class func lanczosScaleTransform() -> any CIFilter & CILanczosScaleTransform](cifilter-swift.class/lanczosscaletransform.md)
  Creates a high-quality, scaled version of a source image.
- [class func perspectiveCorrection() -> any CIFilter & CIPerspectiveCorrection](cifilter-swift.class/perspectivecorrection.md)
  Transforms an image’s perspective.
- [class func perspectiveRotate() -> any CIFilter & CIPerspectiveRotate](cifilter-swift.class/perspectiverotate.md)
  Rotates an image in a 3D space.
- [class func perspectiveTransform() -> any CIFilter & CIPerspectiveTransform](cifilter-swift.class/perspectivetransform.md)
  Alters an image’s geometry to adjust the perspective.
- [class func perspectiveTransformWithExtent() -> any CIFilter & CIPerspectiveTransformWithExtent](cifilter-swift.class/perspectivetransformwithextent.md)
  Alters an image’s geometry to adjust the perspective while applying constraints.
- [class func straighten() -> any CIFilter & CIStraighten](cifilter-swift.class/straighten.md)
  Rotates and crops an image.
### Protocols
- [protocol CIBicubicScaleTransform](cibicubicscaletransform.md)
  The properties you use to configure a bicubic scale transform filter.
- [protocol CIEdgePreserveUpsample](ciedgepreserveupsample.md)
  The properties you use to configure an edge preserve upsample filter.
- [protocol CIFourCoordinateGeometryFilter](cifourcoordinategeometryfilter.md)
  The properties you use to configure a geometry adjustment filters that requires four coordinates.
- [protocol CIKeystoneCorrectionCombined](cikeystonecorrectioncombined.md)
  The properties you use to configure a keystone correction combined filter.
- [protocol CIKeystoneCorrectionHorizontal](cikeystonecorrectionhorizontal.md)
  The properties you use to configure a keystone correction horizontal filter.
- [protocol CIKeystoneCorrectionVertical](cikeystonecorrectionvertical.md)
  The properties you use to configure a keystone correction vertical filter.
- [protocol CILanczosScaleTransform](cilanczosscaletransform.md)
  The properties you use to configure a Lanczos scale transform filter.
- [protocol CIPerspectiveCorrection](ciperspectivecorrection.md)
  The properties you use to configure a perspective correction filter.
- [protocol CIPerspectiveRotate](ciperspectiverotate.md)
  The properties you use to configure a perspective rotate filter.
- [protocol CIPerspectiveTransform](ciperspectivetransform.md)
  The properties you use to configure a perspective transform filter.
- [protocol CIPerspectiveTransformWithExtent](ciperspectivetransformwithextent.md)
  The properties you use to configure a perspective transform with extent filter.
- [protocol CIStraighten](cistraighten.md)
  The properties you use to configure a straighten filter.

## See Also

- [Blur Filters](blur-filters.md)
  Apply blurs, simulate motion and zoom effects, reduce noise, and erode and dilate image regions.
- [Color Adjustment Filters](color-adjustment-filters.md)
  Apply color transformations, including exposure, hue, and tint adjustments.
- [Color Effect Filters](color-effect-filters.md)
  Apply color effects, including photo effects, dithering, and color maps.
- [Composite Operations](composite-operations.md)
  Composite images by using a range of blend modes and compositing operators.
- [Convolution Filters](convolution-filters.md)
  Produce effects such as blurring, sharpening, edge detection, translation, and embossing.
- [Distortion Filters](distortion-filters.md)
  Apply distortion to images.
- [Generator Filters](generator-filters.md)
  Generate barcode, geometric, and special-effect images.
- [Gradient Filters](gradient-filters.md)
  Generate linear and radial gradients.
- [Halftone Effect Filters](halftone-effect-filters.md)
  Simulate monochrome and CMYK halftone screens.
- [Reduction Filters](reduction-filters.md)
  Create statistical information about an image.
- [Sharpening Filters](sharpening-filters.md)
  Apply sharpening to images.
- [Stylizing Filters](stylizing-filters.md)
  Create stylized versions of images by applying effects including pixelation and line overlays.
- [Tile Effect Filters](tile-effect-filters.md)
  Produce tiled images from source images.
- [Transition Filters](transition-filters.md)
  Transition between two images by using effects including page curl and swipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/geometry-adjustment-filters)*