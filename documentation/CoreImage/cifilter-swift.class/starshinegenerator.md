# starShineGenerator()

**Framework**: Core Image  
**Kind**: method

Generates a star-shine image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func starShineGenerator() -> any CIFilter & CIStarShineGenerator
```

#### Return Value

The generated image.

#### Discussion

This method generates a star-shine image. The effect is similar to a supernova effect. You can use this filter to simulate a lens flare.

The star-shine generator filter uses the following properties:

The following code generates a star-shaped silhouette with a black background.

```swift
func starShine() -> CIImage {
    let starShineGenerator = CIFilter.starShineGenerator()
    starShineGenerator.center = CGPoint(x: 150, y: 150)
    starShineGenerator.color = .green
    starShineGenerator.radius = 50
    starShineGenerator.crossScale = 15
    starShineGenerator.crossAngle = 0.60
    starShineGenerator.crossOpacity = -2
    starShineGenerator.crossWidth = 2.5
    starShineGenerator.epsilon = -2.0
    return starShineGenerator.outputImage!
}
```

![A picture of an object that is similar to a square with the corners stretched farther out from the body and a green gradient behind the star shine.](https://docs-assets.developer.apple.com/published/bcef55292331767f620710cf9ec93495/media-3590972%402x.png)

## See Also

- [class func attributedTextImageGenerator() -> any CIFilter & CIAttributedTextImageGenerator](cifilter-swift.class/attributedtextimagegenerator.md)
  Generates an attributed-text image.
- [class func aztecCodeGenerator() -> any CIFilter & CIAztecCodeGenerator](cifilter-swift.class/azteccodegenerator.md)
  Generates a low-density barcode.
- [class func barcodeGenerator() -> any CIFilter & CIBarcodeGenerator](cifilter-swift.class/barcodegenerator.md)
  Generates a barcode as an image from the descriptor.
- [class func blurredRectangleGenerator() -> any CIFilter & CIBlurredRectangleGenerator](cifilter-swift.class/blurredrectanglegenerator.md)
  Generates a blurred rectangle.
- [class func checkerboardGenerator() -> any CIFilter & CICheckerboardGenerator](cifilter-swift.class/checkerboardgenerator.md)
  Generates a checkerboard image.
- [class func code128BarcodeGenerator() -> any CIFilter & CICode128BarcodeGenerator](cifilter-swift.class/code128barcodegenerator.md)
  Generates a high-density, linear barcode.
- [class func lenticularHaloGenerator() -> any CIFilter & CILenticularHaloGenerator](cifilter-swift.class/lenticularhalogenerator.md)
  Generates a lenticular halo image.
- [class func meshGenerator() -> any CIFilter & CIMeshGenerator](cifilter-swift.class/meshgenerator.md)
  Generates a pattern made from an array of line segments.
- [class func pdf417BarcodeGenerator() -> any CIFilter & CIPDF417BarcodeGenerator](cifilter-swift.class/pdf417barcodegenerator.md)
  Generates a high-density linear barcode.
- [class func qrCodeGenerator() -> any CIFilter & CIQRCodeGenerator](cifilter-swift.class/qrcodegenerator.md)
  Generates a quick response (QR) code image.
- [class func randomGenerator() -> any CIFilter & CIRandomGenerator](cifilter-swift.class/randomgenerator.md)
  Generates a random filter image.
- [class func roundedRectangleGenerator() -> any CIFilter & CIRoundedRectangleGenerator](cifilter-swift.class/roundedrectanglegenerator.md)
  Generates a rounded rectangle image.
- [class func roundedRectangleStrokeGenerator() -> any CIFilter & CIRoundedRectangleStrokeGenerator](cifilter-swift.class/roundedrectanglestrokegenerator.md)
  Creates an image containing the outline of a rounded rectangle.
- [class func stripesGenerator() -> any CIFilter & CIStripesGenerator](cifilter-swift.class/stripesgenerator.md)
  Generates a line of stripes as an image
- [class func sunbeamsGenerator() -> any CIFilter & CISunbeamsGenerator](cifilter-swift.class/sunbeamsgenerator.md)
  Generates an image resembling the sun.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/starshinegenerator())*