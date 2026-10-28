# aztecCodeGenerator()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Generates a low-density barcode.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func aztecCodeGenerator() -> any CIFilter & CIAztecCodeGenerator
```

```objc
+ (CIFilter<CIAztecCodeGenerator> *) aztecCodeGeneratorFilter;
```

## Return Value

The generated image.

## Discussion

This method generates an Aztec code as an image. The Aztec barcode code is a low-density barcode defined in the ISO/IEC 24778:2008 standard. This code is commonly used for transport ticketing or boarding passes.

The Aztec code generator filter uses the following properties:

- **`message`**: The data to be encoded as an Aztec code. An [`NSData`](../../Foundation/nsdata.md) object whose display name is Message.
- **`correctionLevel`**: A `float` representing the percentage of redundancy to add to the message data. A higher correction level allows the barcode to be correctly read even when partially damaged.
- **`layers`**: A `float` representing the number of concentric squares encoding the barcode data. When the value is zero, Core Image automatically determines the appropriate number of layers to encode the message data at the specified correction level.
- **`compactStyle`**: A `float` determining the use of compact or full-size Aztec barcode format. The compact format can store up to 44 bytes of message data in up to 4 layers. The full-size format can store up to 1914 bytes of message data in up to 32 layers. Leave unset, or set to 0 for automatic.

The following code creates a filter that generates an Aztec barcode:

```swift
func aztecCode(inputMessage: String) -> CIImage {
    let aztecCodeGenerator = CIFilter.aztecCodeGenerator()
    aztecCodeGenerator.correctionLevel = 15
    aztecCodeGenerator.compactStyle = 0
    aztecCodeGenerator.message = inputMessage.data(using: .ascii)!
    aztecCodeGenerator.layers = 10
    return aztecCodeGenerator.outputImage!
}
```

![An image of a black and white Aztec code made of small squares representing the encoded data of: Filter an image, generate a barcode, what else can CoreImage do?](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3546310@2x.png)

## See Also

### Filters
- [class func attributedTextImageGenerator() -> any CIFilter & CIAttributedTextImageGenerator](./attributedtextimagegenerator%28%29.md)
  Generates an attributed-text image.
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
- [class func sunbeamsGenerator() -> any CIFilter & CISunbeamsGenerator](./sunbeamsgenerator%28%29.md)
  Generates an image resembling the sun.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/azteccodegenerator())*