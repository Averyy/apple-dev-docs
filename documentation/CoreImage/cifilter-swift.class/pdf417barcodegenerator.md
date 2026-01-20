# pdf417BarcodeGenerator()

**Framework**: Core Image  
**Kind**: method

Generates a high-density linear barcode.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func pdf417BarcodeGenerator() -> any CIFilter & CIPDF417BarcodeGenerator
```

#### Return Value

The generated image.

#### Discussion

This method generates a PDF417 barcode as an image. PDF417 is a high-density stacked linear barcode format defined in the ISO 15438 standard. Use this filter to generate alphanumeric or numeric-only barcodes. Commonly used on identification cards or inventory management because of the large amount of data the barcode can hold.

The PDF417 barcode generator filter uses the following properties:

The `compactionMode` property takes one of the following numeric values:

| Value | Name | Description |
| --- | --- | --- |
| `1` | Automatic | The generator automatically chooses a compression method. This option is the default. |
| `2` | Numeric | Valid only when the message is an ASCII-encoded string of digits, achieving optimal compression for that type of data. |
| `3` | Text | Valid only when the message is all ASCII-encoded alphanumeric and punctuation characters, achieving optimal compression for that type of data. |
| `4` | Byte | Valid for any data, but least compact. |

Select either 1 or the appropriate valid value for your data that gives the most compact output.

The following code creates a filter that generates a PDF417 barcode:

```swift
func pdf417Barcode(inputMessage: String) -> CIImage {
    let pdf417BarcodeGenerator = CIFilter.pdf417BarcodeGenerator()
    pdf417BarcodeGenerator.message = inputMessage.data(using: .ascii)!
    pdf417BarcodeGenerator.minWidth = 56
    pdf417BarcodeGenerator.maxWidth = 58
    pdf417BarcodeGenerator.maxHeight = 283
    pdf417BarcodeGenerator.minHeight = 13
    pdf417BarcodeGenerator.dataColumns = 9
    pdf417BarcodeGenerator.rows = 6
    pdf417BarcodeGenerator.preferredAspectRatio = 0.0
    pdf417BarcodeGenerator.compactionMode = 1
    pdf417BarcodeGenerator.compactStyle = 1
    pdf417BarcodeGenerator.correctionLevel = 0.01
    pdf417BarcodeGenerator.alwaysSpecifyCompaction = 0
    return pdf417BarcodeGenerator.outputImage!
}
```

![An image of a black and white PDF417 barcode made of vertical lines of various widths and squares representing the encoded data of 47212826.](https://docs-assets.developer.apple.com/published/78d6a4f5ff73d2f4ea6d592ad3a14c84/media-3546316%402x.png)

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
- [class func qrCodeGenerator() -> any CIFilter & CIQRCodeGenerator](cifilter-swift.class/qrcodegenerator.md)
  Generates a quick response (QR) code image.
- [class func randomGenerator() -> any CIFilter & CIRandomGenerator](cifilter-swift.class/randomgenerator.md)
  Generates a random filter image.
- [class func roundedRectangleGenerator() -> any CIFilter & CIRoundedRectangleGenerator](cifilter-swift.class/roundedrectanglegenerator.md)
  Generates a rounded rectangle image.
- [class func roundedRectangleStrokeGenerator() -> any CIFilter & CIRoundedRectangleStrokeGenerator](cifilter-swift.class/roundedrectanglestrokegenerator.md)
  Creates an image containing the outline of a rounded rectangle.
- [class func starShineGenerator() -> any CIFilter & CIStarShineGenerator](cifilter-swift.class/starshinegenerator.md)
  Generates a star-shine image.
- [class func stripesGenerator() -> any CIFilter & CIStripesGenerator](cifilter-swift.class/stripesgenerator.md)
  Generates a line of stripes as an image
- [class func sunbeamsGenerator() -> any CIFilter & CISunbeamsGenerator](cifilter-swift.class/sunbeamsgenerator.md)
  Generates an image resembling the sun.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/pdf417barcodegenerator())*