# CIPDF417CodeDescriptor

**Framework**: Core Image  
**Kind**: class  
**Role**: Class

A concrete subclass of Core Image Barcode Descriptor that represents a PDF417 symbol.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CIPDF417CodeDescriptor
```

```objc
@interface CIPDF417CodeDescriptor : CIBarcodeDescriptor
```

#### Overview

PDF417 is a stacked linear barcode symbol format used predominantly in transport, ID cards, and inventory management. Each pattern in the code comprises 4 bars and spaces, 17 units long.

Refer to the ISO/IEC 15438:2006(E) for the PDF417 symbol specification.

## Topics

### Creating a Descriptor
- [init?(payload: Data, isCompact: Bool, rowCount: Int, columnCount: Int)](./cipdf417codedescriptor/init%28payload,iscompact,rowcount,columncount%29.md)
  Initializes an PDF417 code descriptor for the given payload and parameters.
- [+ descriptorWithPayload:isCompact:rowCount:columnCount:](./cipdf417codedescriptor/descriptorwithpayload_iscompact_rowcount_columncount_.md)
  Creates an PDF417 code descriptor for the given payload and parameters.
### Examining a Descriptor
- [var errorCorrectedPayload: Data](./cipdf417codedescriptor/errorcorrectedpayload-swift.property.md)
  The error-corrected payload containing the data encoded in the PDF417 code symbol.
- [var isCompact: Bool](./cipdf417codedescriptor/iscompact-swift.property.md)
  A boolean value telling if the PDF417 code is compact.
- [var rowCount: Int](./cipdf417codedescriptor/rowcount-swift.property.md)
  The number of rows in the PDF417 code symbol.
- [var columnCount: Int](./cipdf417codedescriptor/columncount-swift.property.md)
  The number of columns in the PDF417 code symbol.
### Instance Variables
- [columnCount](./cipdf417codedescriptor/columncount-c.ivar.md)
- [errorCorrectedPayload](./cipdf417codedescriptor/errorcorrectedpayload-c.ivar.md)
- [isCompact](./cipdf417codedescriptor/iscompact-c.ivar.md)
- [rowCount](./cipdf417codedescriptor/rowcount-c.ivar.md)

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
- [class CIDataMatrixCodeDescriptor](./cidatamatrixcodedescriptor.md)
  A concrete subclass the Core Image Barcode Descriptor that represents an Data Matrix code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipdf417codedescriptor)*