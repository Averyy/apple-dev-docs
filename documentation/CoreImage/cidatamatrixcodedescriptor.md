# CIDataMatrixCodeDescriptor

**Framework**: Core Image  
**Kind**: class  
**Role**: Class

A concrete subclass the Core Image Barcode Descriptor that represents an Data Matrix code symbol.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CIDataMatrixCodeDescriptor
```

```objc
@interface CIDataMatrixCodeDescriptor : CIBarcodeDescriptor
```

## Overview

A Data Matrix code symbol is a 2D barcode format defined by the ISO/IEC 16022:2006(E) standard. It encodes data in square or rectangular symbol with solid lines on the left and bottom sides

## Topics

### Creating a Descriptor
- [init?(payload: Data, rowCount: Int, columnCount: Int, eccVersion: CIDataMatrixCodeDescriptor.ECCVersion)](./cidatamatrixcodedescriptor/init%28payload,rowcount,columncount,eccversion%29.md)
  Initializes a Data Matrix code descriptor for the given payload and parameters.
- [+ descriptorWithPayload:rowCount:columnCount:eccVersion:](./cidatamatrixcodedescriptor/descriptorwithpayload_rowcount_columncount_eccversion_.md)
  Creates a Data Matrix code descriptor for the given payload and parameters.
### Examining a Descriptor
- [var errorCorrectedPayload: Data](./cidatamatrixcodedescriptor/errorcorrectedpayload-swift.property.md)
  The error-corrected payload containing the data encoded in the Data Matrix code symbol.
- [var rowCount: Int](./cidatamatrixcodedescriptor/rowcount-swift.property.md)
  The number of rows in the Data Matrix code symbol.
- [var columnCount: Int](./cidatamatrixcodedescriptor/columncount-swift.property.md)
  The number of columns in the Data Matrix code symbol.
- [var eccVersion: CIDataMatrixCodeDescriptor.ECCVersion](./cidatamatrixcodedescriptor/eccversion-swift.property.md)
  The error correction version of the Data Matrix code symbol.
### Error Correction Constants
- [CIDataMatrixCodeDescriptor.ECCVersion](./cidatamatrixcodedescriptor/eccversion-swift.enum.md)
  Constants indicating the Data Matrix code ECC version.
### Instance Variables
- [columnCount](./cidatamatrixcodedescriptor/columncount-c.ivar.md)
- [eccVersion](./cidatamatrixcodedescriptor/eccversion-c.ivar.md)
- [errorCorrectedPayload](./cidatamatrixcodedescriptor/errorcorrectedpayload-c.ivar.md)
- [rowCount](./cidatamatrixcodedescriptor/rowcount-c.ivar.md)

## Relationships

### Inherits From
- [CIBarcodeDescriptor](./cibarcodedescriptor.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Barcode Descriptions
- [class CIBarcodeDescriptor](./cibarcodedescriptor.md)
  An abstract base class that represents a machine-readable code’s attributes.
- [class CIQRCodeDescriptor](./ciqrcodedescriptor.md)
  A concrete subclass of the Core Image Barcode Descriptor that represents a square QR code symbol.
- [class CIAztecCodeDescriptor](./ciazteccodedescriptor.md)
  A concrete subclass the Core Image Barcode Descriptor that represents an Aztec code symbol.
- [class CIPDF417CodeDescriptor](./cipdf417codedescriptor.md)
  A concrete subclass of Core Image Barcode Descriptor that represents a PDF417 symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cidatamatrixcodedescriptor)*