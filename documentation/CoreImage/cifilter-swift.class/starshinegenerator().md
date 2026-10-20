# starShineGenerator()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Generates a star-shine image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func starShineGenerator() -> any CIFilter & CIStarShineGenerator
```

```objc
+ (CIFilter<CIStarShineGenerator> *) starShineGeneratorFilter;
```

#### Return Value

The generated image.

#### Discussion

This method generates a star-shine image. The effect is similar to a supernova effect. You can use this filter to simulate a lens flare.

The star-shine generator filter uses the following properties:

- **`center`**: A `vector` representing the center of the flare as a [`CGPoint`](../../CoreFoundation/cgpoint.md).
- **`color`**: A color representing the color of the flare as a [`cgColor`](../../UIKit/uicolor/cgcolor.md).
- **`radius`**: A `float` representing the radius of the flare as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`crossScale`**: A `float` representing the cross flare size relative to the round central flare as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`crossAngle`**: A `float` representing the angle of the flare as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`crossOpacity`**: A `float` representing the thickness of the cross opacity as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`crossWidth`**: A `float` representing the cross width as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`epsilon`**: A `float` representing the epsilon as an [`NSNumber`](../../Foundation/nsnumber.md).

The following code generates a star-shaped silhouette with a black background.

```swift
func starShine() -> CIImage {
    let starShineGenerator = CIFilter.starShineGenerator()
    starShineGenerator.center = CGPoint(x: 150, y: 150)
    starShineGenerator.color = .green
    starShineGenerator.radius = 50
    starShineGenerator.crossScale = 15
    starShineGenerator.crossAngle = 0.60
    starShineGenerator.crossOpacity = -2
    starShineGenerator.crossWidth = 2.5
    starShineGenerator.epsilon = -2.0
    return starShineGenerator.outputImage!
}
```

![A picture of an object that is similar to a square with the corners stretched farther out from the body and a green gradient behind the star shine.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3590972@2x.png)

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
- [class func stripesGenerator() -> any CIFilter & CIStripesGenerator](./stripesgenerator%28%29.md)
  Generates a line of stripes as an image
- [class func sunbeamsGenerator() -> any CIFilter & CISunbeamsGenerator](./sunbeamsgenerator%28%29.md)
  Generates an image resembling the sun.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/starshinegenerator())*