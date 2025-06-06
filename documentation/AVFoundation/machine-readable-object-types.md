# Machine-Readable Object Types

**Framework**: AVFoundation

Constants used to specify the type of barcode to scan.

#### Overview

These constants are used in conjunction with the [`AVCaptureMetadataOutput`](avcapturemetadataoutput.md) class’s [`metadataObjectTypes`](avcapturemetadataoutput/metadataobjecttypes.md) property to specify the type (“symbology”) of barcode to scan. When a barcode is detected, the type property of `AVMetadataMachineReadableCodeObject` reflects the constant for the detected barcode’s symbology.

## Topics

### Constants
- [static let upce: AVMetadataObject.ObjectType](avmetadataobject/objecttype/upce.md)
  A constant that identifies the UPC-E symbology.
- [static let code39: AVMetadataObject.ObjectType](avmetadataobject/objecttype/code39.md)
  A constant that identifies the Code 39 symbology.
- [static let code39Mod43: AVMetadataObject.ObjectType](avmetadataobject/objecttype/code39mod43.md)
  A constant that identifies the Code 39 mod 43 symbology.
- [static let ean13: AVMetadataObject.ObjectType](avmetadataobject/objecttype/ean13.md)
  A constant that identifies the EAN-13 symbology.
- [static let ean8: AVMetadataObject.ObjectType](avmetadataobject/objecttype/ean8.md)
  A constant that identifies the EAN-8 symbology.
- [static let code93: AVMetadataObject.ObjectType](avmetadataobject/objecttype/code93.md)
  A constant that identifies the Code 93 symbology.
- [static let code128: AVMetadataObject.ObjectType](avmetadataobject/objecttype/code128.md)
  A constant that identifies the Code 128 symbology.
- [static let pdf417: AVMetadataObject.ObjectType](avmetadataobject/objecttype/pdf417.md)
  A constant that identifies the PDF417 symbology.
- [static let qr: AVMetadataObject.ObjectType](avmetadataobject/objecttype/qr.md)
  A constant that identifies the QR symbology.
- [static let aztec: AVMetadataObject.ObjectType](avmetadataobject/objecttype/aztec.md)
  A constant that identifies the Aztec symbology.
- [static let interleaved2of5: AVMetadataObject.ObjectType](avmetadataobject/objecttype/interleaved2of5.md)
  A constant that identifies the Interleaved 2 of 5 symbology.
- [static let itf14: AVMetadataObject.ObjectType](avmetadataobject/objecttype/itf14.md)
  A constant that identifies the ITF14 symbology.
- [static let dataMatrix: AVMetadataObject.ObjectType](avmetadataobject/objecttype/datamatrix.md)
  A constant that identifies the DataMatrix symbology.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/machine-readable-object-types)*