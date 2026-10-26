# CIQRCodeDescriptor

**Framework**: Core Image  
**Kind**: class  
**Role**: Class

A concrete subclass of the Core Image Barcode Descriptor that represents a square QR code symbol.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CIQRCodeDescriptor
```

```objc
@interface CIQRCodeDescriptor : CIBarcodeDescriptor
```

#### Overview

ISO/IEC 18004 defines versions from 1 to 40, where a higher symbol version indicates a larger data-carrying capacity. QR Codes can encode text, vCard contact information, or Uniform Resource Identifiers (URI).

## Topics

### Creating a Descriptor
- [init?(payload: Data, symbolVersion: Int, maskPattern: UInt8, errorCorrectionLevel: CIQRCodeDescriptor.ErrorCorrectionLevel)](./ciqrcodedescriptor/init%28payload,symbolversion,maskpattern,errorcorrectionlevel%29.md)
  Initializes a QR code descriptor for the given payload and parameters.
- [+ descriptorWithPayload:symbolVersion:maskPattern:errorCorrectionLevel:](./ciqrcodedescriptor/descriptorwithpayload_symbolversion_maskpattern_errorcorrectionlevel_.md)
  Creates a QR code descriptor for the given payload and parameters.
### Examining a Descriptor
- [var errorCorrectedPayload: Data](./ciqrcodedescriptor/errorcorrectedpayload-swift.property.md)
  The error-corrected codeword payload that comprises the QR code symbol.
- [var symbolVersion: Int](./ciqrcodedescriptor/symbolversion-swift.property.md)
  The version of the QR code which corresponds to the size of the QR code symbol.
- [var maskPattern: UInt8](./ciqrcodedescriptor/maskpattern-swift.property.md)
  The data mask pattern for the QR code symbol.
- [var errorCorrectionLevel: CIQRCodeDescriptor.ErrorCorrectionLevel](./ciqrcodedescriptor/errorcorrectionlevel-swift.property.md)
  The error correction level of the QR code symbol.
### Error Correction Constants
- [CIQRCodeDescriptor.ErrorCorrectionLevel](./ciqrcodedescriptor/errorcorrectionlevel-swift.enum.md)
  Constants indicating the percentage of the symbol that is dedicated to error correction.
### Instance Variables
- [errorCorrectedPayload](./ciqrcodedescriptor/errorcorrectedpayload-c.ivar.md)
- [errorCorrectionLevel](./ciqrcodedescriptor/errorcorrectionlevel-c.ivar.md)
- [maskPattern](./ciqrcodedescriptor/maskpattern-c.ivar.md)
- [symbolVersion](./ciqrcodedescriptor/symbolversion-c.ivar.md)

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
- [class CIAztecCodeDescriptor](./ciazteccodedescriptor.md)
  A concrete subclass the Core Image Barcode Descriptor that represents an Aztec code symbol.
- [class CIPDF417CodeDescriptor](./cipdf417codedescriptor.md)
  A concrete subclass of Core Image Barcode Descriptor that represents a PDF417 symbol.
- [class CIDataMatrixCodeDescriptor](./cidatamatrixcodedescriptor.md)
  A concrete subclass the Core Image Barcode Descriptor that represents an Data Matrix code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciqrcodedescriptor)*