# code128BarcodeGenerator()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Generates a high-density, linear barcode.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func code128BarcodeGenerator() -> any CIFilter & CICode128BarcodeGenerator
```

```objc
+ (CIFilter<CICode128BarcodeGenerator> *) code128BarcodeGeneratorFilter;
```

## Return Value

The generated image.

## Discussion

This method generates a Code 128 barcode as an image. Code 128 is a high-density linear barcode defined in the ISO/IEC 15417:2007 standard. Use this filter to generate alphanumeric or numeric-only barcodes. The barcode can contain any of the 128 ASCII characters.

The Code 128 barcode filter uses the following properties:

- **`message`**: [`NSData`](../../Foundation/nsdata.md) containing the message to encode in the Code 128 barcode.
- **`quietSpace`**: [`NSNumber`](../../Foundation/nsnumber.md) containing the number of empty white pixels that should surround the barcode.
- **`barcodeHeight`**: [`NSNumber`](../../Foundation/nsnumber.md) containing the height of the generated barcode in pixels.

The following code creates a filter that generates a Code 128 barcode:

```swift
func code128Barcode(barcode: String) -> CIImage {
    let code128Barcode = CIFilter.code128BarcodeGenerator()
    code128Barcode.message = barcode.data(using: .ascii)!
    code128Barcode.quietSpace = 5
    code128Barcode.barcodeHeight = 20
    return code128Barcode.outputImage!
}
```

![An image of a black and white barcode made of vertical lines of various widths representing the encoded data of: hello!](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3546314@2x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/code128barcodegenerator())*