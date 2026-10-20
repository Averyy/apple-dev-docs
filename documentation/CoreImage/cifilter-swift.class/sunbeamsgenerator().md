# sunbeamsGenerator()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Generates an image resembling the sun.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class func sunbeamsGenerator() -> any CIFilter & CISunbeamsGenerator
```

```objc
+ (CIFilter<CISunbeamsGenerator> *) sunbeamsGeneratorFilter;
```

#### Return Value

The generated image.

#### Discussion

This method generates a sunbeam as an image. The effect generates a center-textured sun with striations. You can combine with other filters to create more sophisticated images.

The sunbeams generator filter uses the following properties:

- **`center`**: A vector representing the center of the image as a [`CIVector`](../civector.md).
- **`color`**: A [`CIColor`](../cicolor.md) representing the color of the sun.
- **`sunRadius`**: A `float` representing the radius of the center sun as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`maxStriationRadius`**: A `float` representing the striation radius as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`striationStrength`**: A `float` representing the striation strength as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`striationContrast`**: A `float` representing the striation contrast as an [`NSNumber`](../../Foundation/nsnumber.md).
- **`time`**: A `float` representing the time as an [`NSNumber`](../../Foundation/nsnumber.md).

The following code creates a filter that generates an image that resembles a yellow sun with sunbeams:

```swift
    func sunBeam () -> CIImage {
        let sunBeamGenerator = CIFilter.sunbeamsGenerator()
        sunBeamGenerator.center = CGPoint(x: 150, y: 150)
        sunBeamGenerator.color = CIColor(red: 0.96, green: 1, blue: 1, alpha: 1)
        sunBeamGenerator.sunRadius = 40
        sunBeamGenerator.maxStriationRadius = 2.58
        sunBeamGenerator.striationStrength = 0.50
        sunBeamGenerator.striationContrast = 1.38
        sunBeamGenerator.time = 0
        return sunBeamGenerator.outputImage!
    }
```

![An image of a hazy yellow and white ball with lines of color gradually fading to the periphery.](https://developer.apple.com/tutorials/images/com.apple.coreimage/media-3546315@2x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/sunbeamsgenerator())*