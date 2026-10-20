# blurredRectangleGenerator()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Generates a blurred rectangle.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class func blurredRectangleGenerator() -> any CIFilter & CIBlurredRectangleGenerator
```

```objc
+ (CIFilter<CIBlurredRectangleGenerator> *) blurredRectangleGeneratorFilter;
```

#### Return Value

A [`CIImage`](../ciimage.md) containing a blurred rectangle.

#### Discussion

Creates a [`CIImage`](../ciimage.md) containing a blurred rectangle. The resulting image size is the extent of the rectangle plus any additional space required for the blur effect.

The blurred rectangle filter uses the following properties:

- **`extent`**: A [`CGRect`](../../CoreFoundation/cgrect.md) that defines the extent of the effect.
- **`color`**: A [`CIColor`](../cicolor.md) specifying the color of the rectangle.
- **`sigma`**: A `float` specifying the sigma for the Gaussian blur.

The following code creates a filter that generates a blurred red rectangle with a width of 200 x 100 pixels.

```swift
func blurredRectangle() -> CIImage {
    let filter = CIFilter.blurredRectangleGenerator()
    filter.extent = CGRect(x: 0, y: 0, width: 200, height: 100)
    filter.color = CIColor.red
    filter.sigma = 10.0
    return filter.outputImage!
}
```

![An image of a blurred rectangle with an aspect ratio of 2 to 1.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-4407302@2x.png)

## See Also

### Filters
- [class func attributedTextImageGenerator() -> any CIFilter & CIAttributedTextImageGenerator](./attributedtextimagegenerator%28%29.md)
  Generates an attributed-text image.
- [class func aztecCodeGenerator() -> any CIFilter & CIAztecCodeGenerator](./azteccodegenerator%28%29.md)
  Generates a low-density barcode.
- [class func barcodeGenerator() -> any CIFilter & CIBarcodeGenerator](./barcodegenerator%28%29.md)
  Generates a barcode as an image from the descriptor.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/blurredrectanglegenerator())*