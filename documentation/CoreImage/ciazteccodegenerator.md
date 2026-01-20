# CIAztecCodeGenerator

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure an Aztec code generator filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIAztecCodeGenerator : CIFilterProtocol
```

## Topics

### Instance Properties
- [var compactStyle: Float](ciazteccodegenerator/compactstyle.md)
  A Boolean that specifies whether to force a compact style Aztec code.
- [var correctionLevel: Float](ciazteccodegenerator/correctionlevel.md)
  The Aztec error correction, a value from 5 to 95.
- [var layers: Float](ciazteccodegenerator/layers.md)
  The number of Aztec layers, a value from 1 to 32.
- [var message: Data](ciazteccodegenerator/message.md)
  The message to encode in the Aztec barcode.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func aztecCodeGenerator() -> any CIFilter & CIAztecCodeGenerator](cifilter-swift.class/azteccodegenerator.md)
  Generates a low-density barcode.
- [protocol CICode128BarcodeGenerator](cicode128barcodegenerator.md)
  The properties you use to configure a Code 128 barcode generator filter.
- [protocol CIAttributedTextImageGenerator](ciattributedtextimagegenerator.md)
  The properties you use to configure an attributed-text image generator filter.
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
- [protocol CIStripesGenerator](cistripesgenerator.md)
  The properties you use to configure a stripes generator filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciazteccodegenerator)*