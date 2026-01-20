# maskPattern

**Framework**: Core Image  
**Kind**: property

The data mask pattern for the QR code symbol.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var maskPattern: UInt8 { get }
```

#### Discussion

QR Codes support eight data mask patterns, which are used to avoid large black or large white areas inside the symbol body. Valid values range from 0 to 7.

## See Also

- [var errorCorrectedPayload: Data](ciqrcodedescriptor/errorcorrectedpayload-swift.property.md)
  The error-corrected codeword payload that comprises the QR code symbol.
- [var symbolVersion: Int](ciqrcodedescriptor/symbolversion-swift.property.md)
  The version of the QR code which corresponds to the size of the QR code symbol.
- [var errorCorrectionLevel: CIQRCodeDescriptor.ErrorCorrectionLevel](ciqrcodedescriptor/errorcorrectionlevel-swift.property.md)
  The error correction level of the QR code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciqrcodedescriptor/maskpattern-swift.property)*