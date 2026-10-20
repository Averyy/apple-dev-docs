# Generator Filters

**Framework**: Core Image  
**Role**: API Collection

Generate barcode, geometric, and special-effect images.

## Topics

### Filters
- [class func attributedTextImageGenerator() -> any CIFilter & CIAttributedTextImageGenerator](./cifilter-swift.class/attributedtextimagegenerator%28%29.md)
  Generates an attributed-text image.
- [class func aztecCodeGenerator() -> any CIFilter & CIAztecCodeGenerator](./cifilter-swift.class/azteccodegenerator%28%29.md)
  Generates a low-density barcode.
- [class func barcodeGenerator() -> any CIFilter & CIBarcodeGenerator](./cifilter-swift.class/barcodegenerator%28%29.md)
  Generates a barcode as an image from the descriptor.
- [class func blurredRectangleGenerator() -> any CIFilter & CIBlurredRectangleGenerator](./cifilter-swift.class/blurredrectanglegenerator%28%29.md)
  Generates a blurred rectangle.
- [class func checkerboardGenerator() -> any CIFilter & CICheckerboardGenerator](./cifilter-swift.class/checkerboardgenerator%28%29.md)
  Generates a checkerboard image.
- [class func code128BarcodeGenerator() -> any CIFilter & CICode128BarcodeGenerator](./cifilter-swift.class/code128barcodegenerator%28%29.md)
  Generates a high-density, linear barcode.
- [class func lenticularHaloGenerator() -> any CIFilter & CILenticularHaloGenerator](./cifilter-swift.class/lenticularhalogenerator%28%29.md)
  Generates a lenticular halo image.
- [class func meshGenerator() -> any CIFilter & CIMeshGenerator](./cifilter-swift.class/meshgenerator%28%29.md)
  Generates a pattern made from an array of line segments.
- [class func pdf417BarcodeGenerator() -> any CIFilter & CIPDF417BarcodeGenerator](./cifilter-swift.class/pdf417barcodegenerator%28%29.md)
  Generates a high-density linear barcode.
- [class func qrCodeGenerator() -> any CIFilter & CIQRCodeGenerator](./cifilter-swift.class/qrcodegenerator%28%29.md)
  Generates a quick response (QR) code image.
- [class func randomGenerator() -> any CIFilter & CIRandomGenerator](./cifilter-swift.class/randomgenerator%28%29.md)
  Generates a random filter image.
- [class func roundedRectangleGenerator() -> any CIFilter & CIRoundedRectangleGenerator](./cifilter-swift.class/roundedrectanglegenerator%28%29.md)
  Generates a rounded rectangle image.
- [class func roundedRectangleStrokeGenerator() -> any CIFilter & CIRoundedRectangleStrokeGenerator](./cifilter-swift.class/roundedrectanglestrokegenerator%28%29.md)
  Creates an image containing the outline of a rounded rectangle.
- [class func starShineGenerator() -> any CIFilter & CIStarShineGenerator](./cifilter-swift.class/starshinegenerator%28%29.md)
  Generates a star-shine image.
- [class func stripesGenerator() -> any CIFilter & CIStripesGenerator](./cifilter-swift.class/stripesgenerator%28%29.md)
  Generates a line of stripes as an image
- [class func sunbeamsGenerator() -> any CIFilter & CISunbeamsGenerator](./cifilter-swift.class/sunbeamsgenerator%28%29.md)
  Generates an image resembling the sun.
- [class func textImageGenerator() -> any CIFilter & CITextImageGenerator](./cifilter-swift.class/textimagegenerator%28%29.md)
  Generates a text image.
### Protocols
- [protocol CICode128BarcodeGenerator](./cicode128barcodegenerator.md)
  The properties you use to configure a Code 128 barcode generator filter.
- [protocol CIAttributedTextImageGenerator](./ciattributedtextimagegenerator.md)
  The properties you use to configure an attributed-text image generator filter.
- [protocol CIAztecCodeGenerator](./ciazteccodegenerator.md)
  The properties you use to configure an Aztec code generator filter.
- [protocol CIBarcodeGenerator](./cibarcodegenerator.md)
  The properties you use to configure a barcode generator filter.
- [protocol CIBlurredRectangleGenerator](./ciblurredrectanglegenerator.md)
- [protocol CIRoundedRectangleStrokeGenerator](./ciroundedrectanglestrokegenerator.md)
- [protocol CICheckerboardGenerator](./cicheckerboardgenerator.md)
  The properties you use to configure a checkerboard generator filter.
- [protocol CILenticularHaloGenerator](./cilenticularhalogenerator.md)
  The properties you use to configure a lenticular halo generator filter.
- [protocol CIMeshGenerator](./cimeshgenerator.md)
  The properties you use to configure a mesh generator filter.
- [protocol CIPDF417BarcodeGenerator](./cipdf417barcodegenerator.md)
  The properties you use to configure a PDF417 barcode generator filter.
- [protocol CIQRCodeGenerator](./ciqrcodegenerator.md)
  The properties you use to configure a QR code generator filter.
- [protocol CIRandomGenerator](./cirandomgenerator.md)
  The properties you use to configure a random generator filter.
- [protocol CIRoundedRectangleGenerator](./ciroundedrectanglegenerator.md)
  The properties you use to configure a rounded rectangle generator filter.
- [protocol CIRoundedRectangleStrokeGenerator](./ciroundedrectanglestrokegenerator.md)
- [protocol CIStarShineGenerator](./cistarshinegenerator.md)
  The properties you use to configure a star-shine generator filter.
- [protocol CIStripesGenerator](./cistripesgenerator.md)
  The properties you use to configure a stripes generator filter.
- [protocol CISunbeamsGenerator](./cisunbeamsgenerator.md)
  The properties you use to configure a sunbeams generator filter.
- [protocol CITextImageGenerator](./citextimagegenerator.md)
  The properties you use to configure a text image generator filter.

## See Also

### Filter Catalog
- [Blur Filters](./blur-filters.md)
  Apply blurs, simulate motion and zoom effects, reduce noise, and erode and dilate image regions.
- [Color Adjustment Filters](./color-adjustment-filters.md)
  Apply color transformations, including exposure, hue, and tint adjustments.
- [Color Effect Filters](./color-effect-filters.md)
  Apply color effects, including photo effects, dithering, and color maps.
- [Composite Operations](./composite-operations.md)
  Composite images by using a range of blend modes and compositing operators.
- [Convolution Filters](./convolution-filters.md)
  Produce effects such as blurring, sharpening, edge detection, translation, and embossing.
- [Distortion Filters](./distortion-filters.md)
  Apply distortion to images.
- [Geometry Adjustment Filters](./geometry-adjustment-filters.md)
  Translate, scale, and rotate images in 2D and 3D.
- [Gradient Filters](./gradient-filters.md)
  Generate linear and radial gradients.
- [Halftone Effect Filters](./halftone-effect-filters.md)
  Simulate monochrome and CMYK halftone screens.
- [Reduction Filters](./reduction-filters.md)
  Create statistical information about an image.
- [Sharpening Filters](./sharpening-filters.md)
  Apply sharpening to images.
- [Stylizing Filters](./stylizing-filters.md)
  Create stylized versions of images by applying effects including pixelation and line overlays.
- [Tile Effect Filters](./tile-effect-filters.md)
  Produce tiled images from source images.
- [Transition Filters](./transition-filters.md)
  Transition between two images by using effects including page curl and swipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/generator-filters)*