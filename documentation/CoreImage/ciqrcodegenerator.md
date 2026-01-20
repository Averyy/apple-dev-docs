# CIQRCodeGenerator

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a QR code generator filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIQRCodeGenerator : CIFilterProtocol
```

## Topics

### Instance Properties
- [var correctionLevel: String](ciqrcodegenerator/correctionlevel.md)
  The QR code correction level: L, M, Q, or H.
- [var message: Data](ciqrcodegenerator/message.md)
  The message to encode in the QR code.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func qrCodeGenerator() -> any CIFilter & CIQRCodeGenerator](cifilter-swift.class/qrcodegenerator.md)
  Generates a quick response (QR) code image.
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
- [protocol CIRandomGenerator](cirandomgenerator.md)
  The properties you use to configure a random generator filter.
- [protocol CIRoundedRectangleGenerator](ciroundedrectanglegenerator.md)
  The properties you use to configure a rounded rectangle generator filter.
- [protocol CIRoundedRectangleStrokeGenerator](ciroundedrectanglestrokegenerator.md)
- [protocol CIStarShineGenerator](cistarshinegenerator.md)
  The properties you use to configure a star-shine generator filter.
- [protocol CIStripesGenerator](cistripesgenerator.md)
  The properties you use to configure a stripes generator filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciqrcodegenerator)*