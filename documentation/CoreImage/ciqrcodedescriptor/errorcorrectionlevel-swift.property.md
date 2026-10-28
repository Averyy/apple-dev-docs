# errorCorrectionLevel

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

The error correction level of the QR code symbol.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var errorCorrectionLevel: CIQRCodeDescriptor.ErrorCorrectionLevel { get }
```

```objc
@property (readonly) CIQRCodeErrorCorrectionLevel errorCorrectionLevel;
```

## Discussion

QR Codes support four levels of Reed-Solomon error correction.

The possible error correction levels are enumerated in [`CIDataMatrixCodeDescriptor.ECCVersion`](../cidatamatrixcodedescriptor/eccversion-swift.enum.md).

## See Also

### Examining a Descriptor
- [var errorCorrectedPayload: Data](./errorcorrectedpayload-swift.property.md)
  The error-corrected codeword payload that comprises the QR code symbol.
- [var symbolVersion: Int](./symbolversion-swift.property.md)
  The version of the QR code which corresponds to the size of the QR code symbol.
- [var maskPattern: UInt8](./maskpattern-swift.property.md)
  The data mask pattern for the QR code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciqrcodedescriptor/errorcorrectionlevel-swift.property)*