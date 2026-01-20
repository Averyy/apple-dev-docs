# errorCorrectionLevel

**Framework**: Core Image  
**Kind**: property

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

#### Discussion

QR Codes support four levels of Reed-Solomon error correction.

The possible error correction levels are enumerated in [`CIDataMatrixCodeDescriptor.ECCVersion`](cidatamatrixcodedescriptor/eccversion-swift.enum.md).

## See Also

- [var errorCorrectedPayload: Data](ciqrcodedescriptor/errorcorrectedpayload-swift.property.md)
  The error-corrected codeword payload that comprises the QR code symbol.
- [var symbolVersion: Int](ciqrcodedescriptor/symbolversion-swift.property.md)
  The version of the QR code which corresponds to the size of the QR code symbol.
- [var maskPattern: UInt8](ciqrcodedescriptor/maskpattern-swift.property.md)
  The data mask pattern for the QR code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciqrcodedescriptor/errorcorrectionlevel-swift.property)*