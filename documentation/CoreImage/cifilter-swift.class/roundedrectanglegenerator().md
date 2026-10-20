# roundedRectangleGenerator()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Generates a rounded rectangle image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func roundedRectangleGenerator() -> any CIFilter & CIRoundedRectangleGenerator
```

```objc
+ (CIFilter<CIRoundedRectangleGenerator> *) roundedRectangleGeneratorFilter;
```

#### Return Value

The generated image.

#### Discussion

This method generates a rounded rectangle image with the specified size, corner radius, and color properties.

The rounded rectangle generator filter uses the following properties:

- **`color`**: A [`CIColor`](../cicolor.md) representing the color of the rounded rectangle.
- **`extent`**: A [`CGRect`](../../CoreFoundation/cgrect.md) representing the size of the rounded rectangle.
- **`radius`**: A `float` representing the curve of the rectangle’s corners.

The following code creates a filter that generates a light blue square with rounded corners:

```swift
func roundedRectangle () -> CIImage {
    let roundedRectangleGenerator = CIFilter.roundedRectangleGenerator()
    roundedRectangleGenerator.color = CIColor(red: 96/255, green: 173/255, blue: 193/255)
    roundedRectangleGenerator.extent = CGRect(x: 0, y: 1, width: 700, height: 700)
    roundedRectangleGenerator.radius = 100
    return roundedRectangleGenerator.outputImage!
}
```

![A light blue square with rounded corners.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3546319@2x.png)

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
- [class func roundedRectangleStrokeGenerator() -> any CIFilter & CIRoundedRectangleStrokeGenerator](./roundedrectanglestrokegenerator%28%29.md)
  Creates an image containing the outline of a rounded rectangle.
- [class func starShineGenerator() -> any CIFilter & CIStarShineGenerator](./starshinegenerator%28%29.md)
  Generates a star-shine image.
- [class func stripesGenerator() -> any CIFilter & CIStripesGenerator](./stripesgenerator%28%29.md)
  Generates a line of stripes as an image
- [class func sunbeamsGenerator() -> any CIFilter & CISunbeamsGenerator](./sunbeamsgenerator%28%29.md)
  Generates an image resembling the sun.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/roundedrectanglegenerator())*