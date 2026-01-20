# Tile Effect Filters

**Framework**: Core Image

Produce tiled images from source images.

## Topics

### Filters
- [class func affineClamp() -> any CIFilter & CIAffineClamp](cifilter-swift.class/affineclamp.md)
  Performs a transform on the image and extends the image edges to infinity.
- [class func affineTile() -> any CIFilter & CIAffineTile](cifilter-swift.class/affinetile.md)
  Performs a transform on the image and tiles the result.
- [class func eightfoldReflectedTile() -> any CIFilter & CIEightfoldReflectedTile](cifilter-swift.class/eightfoldreflectedtile.md)
  Creates an eight-way reflected pattern.
- [class func fourfoldReflectedTile() -> any CIFilter & CIFourfoldReflectedTile](cifilter-swift.class/fourfoldreflectedtile.md)
  Creates a four-way reflected pattern.
- [class func fourfoldRotatedTile() -> any CIFilter & CIFourfoldRotatedTile](cifilter-swift.class/fourfoldrotatedtile.md)
  Creates a tiled image by rotating a tile in increments of 90 degrees.
- [class func fourfoldTranslatedTile() -> any CIFilter & CIFourfoldTranslatedTile](cifilter-swift.class/fourfoldtranslatedtile.md)
  Creates a tiled image by applying four translation operations.
- [class func glideReflectedTile() -> any CIFilter & CIGlideReflectedTile](cifilter-swift.class/glidereflectedtile.md)
  Tiles an image by rotating and reflecting a tile from the image.
- [class func kaleidoscope() -> any CIFilter & CIKaleidoscope](cifilter-swift.class/kaleidoscope.md)
  Creates a 12-way kaleidoscopic image from an image.
- [class func opTile() -> any CIFilter & CIOpTile](cifilter-swift.class/optile.md)
  Produces an effect that mimics a style of visual art that uses optical illusions.
- [class func parallelogramTile() -> any CIFilter & CIParallelogramTile](cifilter-swift.class/parallelogramtile.md)
  Warps the image to create a parallelogram and tiles the result.
- [class func perspectiveTile() -> any CIFilter & CIPerspectiveTile](cifilter-swift.class/perspectivetile.md)
  Tiles an image by adjusting the perspective of the image.
- [class func sixfoldReflectedTile() -> any CIFilter & CISixfoldReflectedTile](cifilter-swift.class/sixfoldreflectedtile.md)
  Produces a tiled image from a source image by applying a six-way reflected symmetry.
- [class func sixfoldRotatedTile() -> any CIFilter & CISixfoldRotatedTile](cifilter-swift.class/sixfoldrotatedtile.md)
  Creates a tiled image by rotating in increments of 60 degrees.
- [class func triangleKaleidoscope() -> any CIFilter & CITriangleKaleidoscope](cifilter-swift.class/trianglekaleidoscope.md)
  Create a triangular kaleidoscope effect and then tiles the result.
- [class func triangleTile() -> any CIFilter & CITriangleTile](cifilter-swift.class/triangletile.md)
  Tiles a triangular area of an image.
- [class func twelvefoldReflectedTile() -> any CIFilter & CITwelvefoldReflectedTile](cifilter-swift.class/twelvefoldreflectedtile.md)
  Creates a tiled image by rotating in increments of 30 degrees.
### Protocols
- [protocol CIAffineClamp](ciaffineclamp.md)
  The properties you use to configure an affine clamp filter.
- [protocol CIAffineTile](ciaffinetile.md)
  The properties you use to configure an affine tile filter.
- [protocol CIEightfoldReflectedTile](cieightfoldreflectedtile.md)
  The properties you use to configure an eightfold reflected tile filter.
- [protocol CIFourfoldReflectedTile](cifourfoldreflectedtile.md)
  The properties you use to configure a fourfold reflected tile filter.
- [protocol CIFourfoldRotatedTile](cifourfoldrotatedtile.md)
  The properties you use to configure a fourfold rotated tile filter.
- [protocol CIFourfoldTranslatedTile](cifourfoldtranslatedtile.md)
  The properties you use to configure a fourfold translated tile filter.
- [protocol CIGlideReflectedTile](ciglidereflectedtile.md)
  The properties you use to configure a glide reflected tile filter.
- [protocol CIKaleidoscope](cikaleidoscope.md)
  The properties you use to configure a kaleidoscope filter.
- [protocol CIOpTile](cioptile.md)
  The properties you use to configure an optical tile filter.
- [protocol CIParallelogramTile](ciparallelogramtile.md)
  The properties you use to configure a parallelogram tile filter.
- [protocol CIPerspectiveTile](ciperspectivetile.md)
  The properties you use to configure a perspective tile filter.
- [protocol CISixfoldReflectedTile](cisixfoldreflectedtile.md)
  The properties you use to configure a sixfold reflected tile filter.
- [protocol CISixfoldRotatedTile](cisixfoldrotatedtile.md)
  The properties you use to configure a sixfold rotated tile filter.
- [protocol CITriangleKaleidoscope](citrianglekaleidoscope.md)
  The properties you use to configure a triangle kaleidoscope filter.
- [protocol CITriangleTile](citriangletile.md)
  The properties you use to configure a triangle tile filter.
- [protocol CITwelvefoldReflectedTile](citwelvefoldreflectedtile.md)
  The properties you use to configure a twelvefold reflected tile filter.

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
- [Geometry Adjustment Filters](geometry-adjustment-filters.md)
  Translate, scale, and rotate images in 2D and 3D.
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
- [Transition Filters](transition-filters.md)
  Transition between two images by using effects including page curl and swipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/tile-effect-filters)*