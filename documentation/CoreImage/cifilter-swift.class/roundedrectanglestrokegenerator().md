# roundedRectangleStrokeGenerator()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Creates an image containing the outline of a rounded rectangle.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class func roundedRectangleStrokeGenerator() -> any CIFilter & CIRoundedRectangleStrokeGenerator
```

```objc
+ (CIFilter<CIRoundedRectangleStrokeGenerator> *) roundedRectangleStrokeGeneratorFilter;
```

## Return Value

A [`CIImage`](../ciimage.md) containing the stroked rectangle.

## Discussion

This filter creates an outline of a rounded rectangle.

The filter takes the following properties:

- **`extent`**: A [`CGRect`](../../CoreFoundation/cgrect.md) containing the position and size of the rectangle.
- **`width`**: The width of the stroke to draw.
- **`radius`**: The corner radius.

The following code generates an image containing a stroked rounded rectangle:

```swift
func roundedRectangleStroke() -> CIImage {
    let filter = CIFilter.roundedRectangleStrokeGenerator()
    filter.extent = CGRect(x: 0, y: 0, width: 200, height: 100)
    filter.color = CIColor.red
    filter.width = 5
    filter.radius = 20
    return filter.outputImage!
}
```

![An image containing an outlined rectangle with rounded corners.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-4407287@2x.png)

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
- [class func starShineGenerator() -> any CIFilter & CIStarShineGenerator](./starshinegenerator%28%29.md)
  Generates a star-shine image.
- [class func stripesGenerator() -> any CIFilter & CIStripesGenerator](./stripesgenerator%28%29.md)
  Generates a line of stripes as an image
- [class func sunbeamsGenerator() -> any CIFilter & CISunbeamsGenerator](./sunbeamsgenerator%28%29.md)
  Generates an image resembling the sun.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/roundedrectanglestrokegenerator())*