# checkerboardGenerator()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Generates a checkerboard image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func checkerboardGenerator() -> any CIFilter & CICheckerboardGenerator
```

```objc
+ (CIFilter<CICheckerboardGenerator> *) checkerboardGeneratorFilter;
```

## Return Value

The generated image.

## Discussion

This method generates a checkerboard pattern as an image. The effect requires the size, sharpness, and color properties to create the pattern.

The checkerboard generator filter uses the following properties:

- **`center`**: A `vector` representing the center of the image as a [`CIVector`](../civector.md).
- **`color0`**: A [`CIColor`](../cicolor.md) representing the first color of the pattern.
- **`color1`**: A [`CIColor`](../cicolor.md) representing the second color of the pattern.
- **`sharpness`**: A `float` representing the sharpness of the pattern as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`width`**: A `float` representing the width of the checkerboard squares as an [`NSNumber`](../../Foundation/nsnumber.md).

The following code creates a filter that generates a black-and-white checkered pattern:

```swift
func checkerBoard() -> CIImage {
    let checkerBoardGenerator = CIFilter.checkerboardGenerator()
    checkerBoardGenerator.setDefaults()
    checkerBoardGenerator.center = CGPoint(x: 0, y: 0)
    checkerBoardGenerator.color0 = .white
    checkerBoardGenerator.color1 = .black
    checkerBoardGenerator.width = 40
    checkerBoardGenerator.sharpness = 1
    return checkerBoardGenerator.outputImage!
}
```

![An image of small black-and-white squares repeating, creating a checkerboard pattern.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3590970@2x.png)

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
- [class func stripesGenerator() -> any CIFilter & CIStripesGenerator](./stripesgenerator%28%29.md)
  Generates a line of stripes as an image
- [class func sunbeamsGenerator() -> any CIFilter & CISunbeamsGenerator](./sunbeamsgenerator%28%29.md)
  Generates an image resembling the sun.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/checkerboardgenerator())*