# BarcodeAnchor.Symbology

**Framework**: ARKit  
**Kind**: enum

Values that describe specific kinds of barcodes.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
enum Symbology
```

## Topics

### Barcode symbologies
- [BarcodeAnchor.Symbology.aztec](barcodeanchor/symbology-swift.enum/aztec.md)
  The value that represents the Aztec barcode symbology.
- [BarcodeAnchor.Symbology.codabar](barcodeanchor/symbology-swift.enum/codabar.md)
  The value that represents the Codabar barcode symbology.
- [BarcodeAnchor.Symbology.code128](barcodeanchor/symbology-swift.enum/code128.md)
  The value that represents the Code 128 barcode symbology.
- [BarcodeAnchor.Symbology.code39](barcodeanchor/symbology-swift.enum/code39.md)
  The value that represents the Code 39 barcode symbology.
- [BarcodeAnchor.Symbology.code39Checksum](barcodeanchor/symbology-swift.enum/code39checksum.md)
  The value that represents the Code 39 checksum barcode symbology.
- [BarcodeAnchor.Symbology.code39FullAscii](barcodeanchor/symbology-swift.enum/code39fullascii.md)
  The value that represents the Code 39 full ASCII barcode symbology.
- [BarcodeAnchor.Symbology.code39FullAsciiChecksum](barcodeanchor/symbology-swift.enum/code39fullasciichecksum.md)
  The value that represents the Code 39 full ASCII checksum barcode symbology.
- [BarcodeAnchor.Symbology.code93](barcodeanchor/symbology-swift.enum/code93.md)
  The value that represents the Code 93 symbology.
- [BarcodeAnchor.Symbology.code93i](barcodeanchor/symbology-swift.enum/code93i.md)
  The value that represents the Code 93i barcode symbology.
- [BarcodeAnchor.Symbology.dataMatrix](barcodeanchor/symbology-swift.enum/datamatrix.md)
  The value that represents the Data Matrix barcode symbology.
- [BarcodeAnchor.Symbology.ean13](barcodeanchor/symbology-swift.enum/ean13.md)
  The value that represents the EAN13 barcode symbology.
- [BarcodeAnchor.Symbology.ean8](barcodeanchor/symbology-swift.enum/ean8.md)
  The value that represents the EAN8 barcode symbology.
- [BarcodeAnchor.Symbology.gs1DataBar](barcodeanchor/symbology-swift.enum/gs1databar.md)
  The value that represents the GS1 DataBar barcode symbology.
- [BarcodeAnchor.Symbology.gs1DataBarExpanded](barcodeanchor/symbology-swift.enum/gs1databarexpanded.md)
  The value that represents the GS1 DataBar Expanded barcode symbology.
- [BarcodeAnchor.Symbology.gs1DataBarLimited](barcodeanchor/symbology-swift.enum/gs1databarlimited.md)
  The value that represents the GS1 DataBar Limited barcode symbology.
- [BarcodeAnchor.Symbology.itf](barcodeanchor/symbology-swift.enum/itf.md)
  The value that represents the ITF barcode symbology.
- [BarcodeAnchor.Symbology.itf14](barcodeanchor/symbology-swift.enum/itf14.md)
  The value that represents the ITF14 barcode symbology.
- [BarcodeAnchor.Symbology.itfChecksum](barcodeanchor/symbology-swift.enum/itfchecksum.md)
  The value that represents the ITF checksum barcode symbology.
- [BarcodeAnchor.Symbology.microPDF417](barcodeanchor/symbology-swift.enum/micropdf417.md)
  The value that represents the Micro PDF417 barcode symbology.
- [BarcodeAnchor.Symbology.microQR](barcodeanchor/symbology-swift.enum/microqr.md)
  The value that represents the Micro QR barcode symbology.
- [BarcodeAnchor.Symbology.msiPlessey](barcodeanchor/symbology-swift.enum/msiplessey.md)
  The value that represents the MSI Plessy barcode symbology.
- [BarcodeAnchor.Symbology.pdf417](barcodeanchor/symbology-swift.enum/pdf417.md)
  The value that represents the PDF417 barcode symbology.
- [BarcodeAnchor.Symbology.qr](barcodeanchor/symbology-swift.enum/qr.md)
  The value that represents the QR barcode symbology.
- [BarcodeAnchor.Symbology.upce](barcodeanchor/symbology-swift.enum/upce.md)
  The value that represents the UPCE barcode symbology.
### Instance Properties
- [var description: String](barcodeanchor/symbology-swift.enum/description.md)
  A textual representation of BarcodeAnchor.Symbology

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var extent: SIMD3<Float>](barcodeanchor/extent.md)
  The extent of the detected barcode’s bounds.
- [var originFromAnchorTransform: simd_float4x4](barcodeanchor/originfromanchortransform.md)
  The transform from the barcode anchor to the origin coordinate system.
- [var payloadData: Data](barcodeanchor/payloaddata.md)
  The encoded payload data of the detected barcode.
- [var payloadString: String?](barcodeanchor/payloadstring.md)
  The decoded payload string value of the detected barcode.
- [var symbology: BarcodeAnchor.Symbology](barcodeanchor/symbology-swift.property.md)
  The symbology of the detected barcode.
- [var id: UUID](barcodeanchor/id.md)
  The unique identifier of an anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/barcodeanchor/symbology-swift.enum)*