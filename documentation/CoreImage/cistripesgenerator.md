# CIStripesGenerator

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a stripes generator filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIStripesGenerator : CIFilterProtocol
```

## Topics

### Instance Properties
- [var center: CGPoint](cistripesgenerator/center.md)
  The x and y position to use as the center of the stripe pattern.
- [var color0: CIColor](cistripesgenerator/color0.md)
  A color to use for the odd stripes.
- [var color1: CIColor](cistripesgenerator/color1.md)
  A color to use for the even stripes.
- [var sharpness: Float](cistripesgenerator/sharpness.md)
  The sharpness of the stripe pattern.
- [var width: Float](cistripesgenerator/width.md)
  The width of a stripe.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func stripesGenerator() -> any CIFilter & CIStripesGenerator](cifilter-swift.class/stripesgenerator.md)
  Generates a line of stripes as an image
- [protocol CICode128BarcodeGenerator](cicode128barcodegenerator.md)
  The properties you use to configure a Code 128 barcode generator filter.
- [protocol CIAttributedTextImageGenerator](ciattributedtextimagegenerator.md)
  The properties you use to configure an attributed-text image generator filter.
- [protocol CIAztecCodeGenerator](ciazteccodegenerator.md)
  The properties you use to configure an Aztec code generator filter.
- [protocol CIBarcodeGenerator](cibarcodegenerator.md)
  The properties you use to configure a barcode generator filter.
- [protocol CIBlurredRectangleGenerator](ciblurredrectanglegenerator.md)
- [protocol CIRoundedRectangleStrokeGenerator](ciroundedrectanglestrokegenerator.md)
- [protocol CICheckerboardGenerator](cicheckerboardgenerator.md)
  The properties you use to configure a checkerboard generator filter.
- [protocol CILenticularHaloGenerator](cilenticularhalogenerator.md)
  The properties you use to configure a lenticular halo generator filter.
- [protocol CIMeshGenerator](cimeshgenerator.md)
  The properties you use to configure a mesh generator filter.
- [protocol CIPDF417BarcodeGenerator](cipdf417barcodegenerator.md)
  The properties you use to configure a PDF417 barcode generator filter.
- [protocol CIQRCodeGenerator](ciqrcodegenerator.md)
  The properties you use to configure a QR code generator filter.
- [protocol CIRandomGenerator](cirandomgenerator.md)
  The properties you use to configure a random generator filter.
- [protocol CIRoundedRectangleGenerator](ciroundedrectanglegenerator.md)
  The properties you use to configure a rounded rectangle generator filter.
- [protocol CIRoundedRectangleStrokeGenerator](ciroundedrectanglestrokegenerator.md)
- [protocol CIStarShineGenerator](cistarshinegenerator.md)
  The properties you use to configure a star-shine generator filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cistripesgenerator)*