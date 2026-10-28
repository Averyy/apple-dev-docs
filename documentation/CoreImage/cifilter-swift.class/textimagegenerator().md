# textImageGenerator()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Generates a text image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func textImageGenerator() -> any CIFilter & CITextImageGenerator
```

```objc
+ (CIFilter<CITextImageGenerator> *) textImageGeneratorFilter;
```

## Return Value

The generated image.

## Discussion

This method generates a text image. The effect takes the input string property and the scale factor to scale up the text. You commonly combine this filter with other filters to create a watermark on images.

The text image generator filter uses the following properties:

- **`text`**: The `string` to render. The string can contain non-ASCII characters.
- **`fontName`**: A `string` representing the name of the font to be used to generate the image.
- **`fontSize`**: A `float` representing the size of the font as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`scaleFactor`**: A `float` representing the scale of the font for the generated text as an [`NSNumber`](../../Foundation/nsnumber.md).

The following code creates a filter that generates a string of text as a grayscale image:

```swift
func textImage(inputText: String) -> CIImage {
    let textImageGenerator = CIFilter.textImageGenerator()
    textImageGenerator.text = inputText
    textImageGenerator.fontName = "Helvetica"
    textImageGenerator.fontSize = 25
    textImageGenerator.scaleFactor = 4
    return textImageGenerator.outputImage!
}
```

![An image with the text Hello World! in black and a hand wave emoticon in gray.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3546321@2x.png)

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
- [class func stripesGenerator() -> any CIFilter & CIStripesGenerator](./stripesgenerator%28%29.md)
  Generates a line of stripes as an image


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/textimagegenerator())*