# maskPattern

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) uint8_t maskPattern;
```

#### Discussion

QR Codes support eight data mask patterns, which are used to avoid large black or large white areas inside the symbol body. Valid values range from 0 to 7.

## See Also

### Examining a Descriptor
- [var errorCorrectedPayload: Data](./errorcorrectedpayload-swift.property.md)
  The error-corrected codeword payload that comprises the QR code symbol.
- [var symbolVersion: Int](./symbolversion-swift.property.md)
  The version of the QR code which corresponds to the size of the QR code symbol.
- [var errorCorrectionLevel: CIQRCodeDescriptor.ErrorCorrectionLevel](./errorcorrectionlevel-swift.property.md)
  The error correction level of the QR code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciqrcodedescriptor/maskpattern-swift.property)*