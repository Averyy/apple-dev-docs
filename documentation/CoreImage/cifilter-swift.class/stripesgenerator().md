# stripesGenerator()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Generates a line of stripes as an image

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func stripesGenerator() -> any CIFilter & CIStripesGenerator
```

```objc
+ (CIFilter<CIStripesGenerator> *) stripesGeneratorFilter;
```

## Return Value

The generated image.

## Discussion

This method generates a vertical stripped line pattern as an image.

The stripes generator filter uses the following properties:

- **`center`**: A [`CIVector`](../civector.md) representing the center of the image.
- **`color0`**: A [`CIColor`](../cicolor.md) representing the stripes color.
- **`color1`**: A [`CIColor`](../cicolor.md) representing the background color.
- **`width`**: A `float` representing the width of the lines as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`sharpness`**: A `float` representing the sharpness of the lines as an [`NSNumber`](../../Foundation/nsnumber.md).

The following code creates a filter that generates a black and white vertical striped image:

```swift
func stripes() -> CIImage {
    let stripesGenerator = CIFilter.stripesGenerator()
    stripesGenerator.center = CGPoint(x: 150, y: 150)
    stripesGenerator.color0 = .white
    stripesGenerator.color1 = .black
    stripesGenerator.width = 80
    stripesGenerator.sharpness = 1
    return stripesGenerator.outputImage!
}
```

![A series of vertical black and white lines repeating the entire image.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3590971@2x.png)

## See Also

### Filters
- [class func attributedTextImageGenerator() -> any CIFilter & CIAttributedTextImageGenerator](./attributedtextimagegenerator%28%29.md)
  Generates an attributed-text image.
- [class func aztecCodeGenerator() -> any CIFilter & CIAztecCodeGenerator](./azteccodegenerator%28%29.md)
  Generates a low-density barcode.
- [class func barcodeGenerator() -> any CIFilter & CIBarcodeGenerator](./barcodegenerator%28%29.md)
  Generates a barcode as an image from the descriptor.
- [class func blurredRectangleGenerator() -> any CIFilter & CIBlurredRectangleGenerator](./blurredrectanglegenerator%28%29.md)
  Generates a blurred rectangle.
- [class func checkerboardGenerator() -> any CIFilter & CICheckerboardGenerator](./checkerboardgenerator%28%29.md)
  Generates a checkerboard image.
- [class func code128BarcodeGenerator() -> any CIFilter & CICode128BarcodeGenerator](./code128barcodegenerator%28%29.md)
  Generates a high-density, linear barcode.
- [class func lenticularHaloGenerator() -> any CIFilter & CILenticularHaloGenerator](./lenticularhalogenerator%28%29.md)
  Generates a lenticular halo image.
- [class func meshGenerator() -> any CIFilter & CIMeshGenerator](./meshgenerator%28%29.md)
  Generates a pattern made from an array of line segments.
- [class func pdf417BarcodeGenerator() -> any CIFilter & CIPDF417BarcodeGenerator](./pdf417barcodegenerator%28%29.md)
  Generates a high-density linear barcode.
- [class func qrCodeGenerator() -> any CIFilter & CIQRCodeGenerator](./qrcodegenerator%28%29.md)
  Generates a quick response (QR) code image.
- [class func randomGenerator() -> any CIFilter & CIRandomGenerator](./randomgenerator%28%29.md)
  Generates a random filter image.
- [class func roundedRectangleGenerator() -> any CIFilter & CIRoundedRectangleGenerator](./roundedrectanglegenerator%28%29.md)
  Generates a rounded rectangle image.
- [class func roundedRectangleStrokeGenerator() -> any CIFilter & CIRoundedRectangleStrokeGenerator](./roundedrectanglestrokegenerator%28%29.md)
  Creates an image containing the outline of a rounded rectangle.
- [class func starShineGenerator() -> any CIFilter & CIStarShineGenerator](./starshinegenerator%28%29.md)
  Generates a star-shine image.
- [class func sunbeamsGenerator() -> any CIFilter & CISunbeamsGenerator](./sunbeamsgenerator%28%29.md)
  Generates an image resembling the sun.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/stripesgenerator())*