# CIAztecCodeDescriptor

**Framework**: Core Image  
**Kind**: class  
**Role**: Class

A concrete subclass the Core Image Barcode Descriptor that represents an Aztec code symbol.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class CIAztecCodeDescriptor
```

```objc
@interface CIAztecCodeDescriptor : CIBarcodeDescriptor
```

## Overview

An Aztec code symbol is a 2D barcode format defined by the ISO/IEC 24778:2008 standard. It encodes data in concentric square rings around a central bullseye pattern.

## Topics

### Creating a Descriptor
- [init?(payload: Data, isCompact: Bool, layerCount: Int, dataCodewordCount: Int)](./ciazteccodedescriptor/init%28payload,iscompact,layercount,datacodewordcount%29.md)
  Initializes an Aztec code descriptor for the given payload and parameters.
- [+ descriptorWithPayload:isCompact:layerCount:dataCodewordCount:](./ciazteccodedescriptor/descriptorwithpayload_iscompact_layercount_datacodewordcount_.md)
  Creates an Aztec code descriptor for the given payload and parameters.
### Examining a Descriptor
- [var errorCorrectedPayload: Data](./ciazteccodedescriptor/errorcorrectedpayload-swift.property.md)
  The error-corrected payload that comprises the the Aztec code symbol.
- [var isCompact: Bool](./ciazteccodedescriptor/iscompact-swift.property.md)
  A Boolean value telling if the Aztec code is compact.
- [var layerCount: Int](./ciazteccodedescriptor/layercount-swift.property.md)
  The number of data layers in the Aztec code symbol.
- [var dataCodewordCount: Int](./ciazteccodedescriptor/datacodewordcount-swift.property.md)
  The number of non-error-correction codewords carried by the Aztec code symbol.
### Instance Variables
- [dataCodewordCount](./ciazteccodedescriptor/datacodewordcount-c.ivar.md)
- [errorCorrectedPayload](./ciazteccodedescriptor/errorcorrectedpayload-c.ivar.md)
- [isCompact](./ciazteccodedescriptor/iscompact-c.ivar.md)
- [layerCount](./ciazteccodedescriptor/layercount-c.ivar.md)

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
- [class CIPDF417CodeDescriptor](./cipdf417codedescriptor.md)
  A concrete subclass of Core Image Barcode Descriptor that represents a PDF417 symbol.
- [class CIDataMatrixCodeDescriptor](./cidatamatrixcodedescriptor.md)
  A concrete subclass the Core Image Barcode Descriptor that represents an Data Matrix code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciazteccodedescriptor)*