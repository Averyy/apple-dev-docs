# errorCorrectedPayload

**Framework**: Core Image  
**Kind**: property

The error-corrected codeword payload that comprises the QR code symbol.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var errorCorrectedPayload: Data { get }
```

#### Discussion

QR Codes are formally specified in ISO/IEC 18004:2006(E). Section 6.4.10 “Bitstream to codeword conversion” specifies the set of 8-bit codewords in the symbol immediately prior to splitting the message into blocks and applying error correction.

During decode, error correction is applied and if successful, the message is re-ordered to the state immediately following “Bitstream to codeword conversion.”

The `errorCorrectedPayload` corresponds to this sequence of 8-bit codewords.

## See Also

- [var symbolVersion: Int](ciqrcodedescriptor/symbolversion-swift.property.md)
  The version of the QR code which corresponds to the size of the QR code symbol.
- [var maskPattern: UInt8](ciqrcodedescriptor/maskpattern-swift.property.md)
  The data mask pattern for the QR code symbol.
- [var errorCorrectionLevel: CIQRCodeDescriptor.ErrorCorrectionLevel](ciqrcodedescriptor/errorcorrectionlevel-swift.property.md)
  The error correction level of the QR code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciqrcodedescriptor/errorcorrectedpayload-swift.property)*