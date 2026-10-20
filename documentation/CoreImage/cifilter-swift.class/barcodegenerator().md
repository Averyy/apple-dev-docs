# barcodeGenerator()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Generates a barcode as an image from the descriptor.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func barcodeGenerator() -> any CIFilter & CIBarcodeGenerator
```

```objc
+ (CIFilter<CIBarcodeGenerator> *) barcodeGeneratorFilter;
```

#### Return Value

The generated image.

#### Discussion

This method generates a custom barcode as an image. The effect uses barcode descriptors to specify properties of the generated barcode.

The barcode generator uses the following property:

- **`barcodeDescriptor`**: An instance of [`CIBarcodeDescriptor`](../cibarcodedescriptor.md) with the input parameters supplied.

The following code creates a filter that generates a QR code containing the text *Johnny Appleseed.*

```swift
func barcode(inputMessage: Data) -> CIImage {
   let barcodeGenerator = CIFilter.barcodeGenerator()
    barcodeGenerator.barcodeDescriptor = CIQRCodeDescriptor(payload: inputMessage, symbolVersion: 1, maskPattern: 4, errorCorrectionLevel: .levelL)!
    return barcodeGenerator.outputImage!
}

let johnnyAppleseed: [UInt8] = [0x41, 0x04, 0xA6, 0xF6, 0x86, 0xE6, 0xE7, 0x92, 0x04, 0x17, 0x07, 0x06, 0xC6, 0x57, 0x36, 0x56, 0x56, 0x40, 0xEC]
let data = Data(johnnyAppleseed)

let bImage = barcode(inputMessage: data)
```

![A QR code containing the text Johnny Appleseed.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-4327881@2x.png)

## See Also

### Related Documentation
- [class CIAztecCodeDescriptor](../ciazteccodedescriptor.md)
  A concrete subclass the Core Image Barcode Descriptor that represents an Aztec code symbol.
- [class CIDataMatrixCodeDescriptor](../cidatamatrixcodedescriptor.md)
  A concrete subclass the Core Image Barcode Descriptor that represents an Data Matrix code symbol.
- [class CIPDF417CodeDescriptor](../cipdf417codedescriptor.md)
  A concrete subclass of Core Image Barcode Descriptor that represents a PDF417 symbol.
- [class CIQRCodeDescriptor](../ciqrcodedescriptor.md)
  A concrete subclass of the Core Image Barcode Descriptor that represents a square QR code symbol.
### Filters
- [class func attributedTextImageGenerator() -> any CIFilter & CIAttributedTextImageGenerator](./attributedtextimagegenerator%28%29.md)
  Generates an attributed-text image.
- [class func aztecCodeGenerator() -> any CIFilter & CIAztecCodeGenerator](./azteccodegenerator%28%29.md)
  Generates a low-density barcode.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/barcodegenerator())*