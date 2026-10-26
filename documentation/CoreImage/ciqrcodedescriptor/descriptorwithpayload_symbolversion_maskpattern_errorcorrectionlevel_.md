# descriptorWithPayload:symbolVersion:maskPattern:errorCorrectionLevel:

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Creates a QR code descriptor for the given payload and parameters.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) descriptorWithPayload:(NSData *) errorCorrectedPayload symbolVersion:(NSInteger) symbolVersion maskPattern:(uint8_t) maskPattern errorCorrectionLevel:(CIQRCodeErrorCorrectionLevel) errorCorrectionLevel;
```

#### Return Value

 An autoreleased [`CIAztecCodeDescriptor`](../ciazteccodedescriptor.md) instance or `nil` if the parameters are invalid

## Parameters

- `errorCorrectedPayload`: The data to encode in the QR code symbol.
- `symbolVersion`: The symbol version, from 1 through 40.
- `maskPattern`: The mask pattern to use in the QR code, from 0 to 7.
- `errorCorrectionLevel`: The QR code’s error correction level: L, M, Q, or H.

## See Also

### Creating a Descriptor
- [init?(payload: Data, symbolVersion: Int, maskPattern: UInt8, errorCorrectionLevel: CIQRCodeDescriptor.ErrorCorrectionLevel)](./init%28payload,symbolversion,maskpattern,errorcorrectionlevel%29.md)
  Initializes a QR code descriptor for the given payload and parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciqrcodedescriptor/descriptorwithpayload:symbolversion:maskpattern:errorcorrectionlevel:)*