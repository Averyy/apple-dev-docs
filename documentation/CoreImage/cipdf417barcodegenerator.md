# CIPDF417BarcodeGenerator

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a PDF417 barcode generator filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIPDF417BarcodeGenerator : CIFilterProtocol
```

## Topics

### Instance Properties
- [var alwaysSpecifyCompaction: Float](cipdf417barcodegenerator/alwaysspecifycompaction.md)
  A Boolean value specifying whether to force compaction style.
- [var compactStyle: Float](cipdf417barcodegenerator/compactstyle.md)
  A Boolean value specifying whether to force compact style Aztec code.
- [var compactionMode: Float](cipdf417barcodegenerator/compactionmode.md)
  The compaction mode of the generated barcode.
- [var correctionLevel: Float](cipdf417barcodegenerator/correctionlevel.md)
  The correction level ratio of the generated barcode.
- [var dataColumns: Float](cipdf417barcodegenerator/datacolumns.md)
  The number of data columns in the generated barcode.
- [var maxHeight: Float](cipdf417barcodegenerator/maxheight.md)
  The maximum height, in pixels, of the generated barcode.
- [var maxWidth: Float](cipdf417barcodegenerator/maxwidth.md)
  The maximum width, in pixels, of the generated barcode.
- [var message: Data](cipdf417barcodegenerator/message.md)
  The message to encode in the PDF417 barcode.
- [var minHeight: Float](cipdf417barcodegenerator/minheight.md)
  The minimum height, in pixels, of the generated barcode.
- [var minWidth: Float](cipdf417barcodegenerator/minwidth.md)
  The minimum width, in pixels, of the generated barcode.
- [var preferredAspectRatio: Float](cipdf417barcodegenerator/preferredaspectratio.md)
  The preferred aspect ratio of the generated barcode.
- [var rows: Float](cipdf417barcodegenerator/rows.md)
  The number of rows in the generated barcode.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func pdf417BarcodeGenerator() -> any CIFilter & CIPDF417BarcodeGenerator](cifilter-swift.class/pdf417barcodegenerator.md)
  Generates a high-density linear barcode.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipdf417barcodegenerator)*