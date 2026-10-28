# symbolDescriptor

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

An abstract representation of a QR Code symbol.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var symbolDescriptor: CIQRCodeDescriptor? { get }
```

```objc
@property (readonly, nullable) CIQRCodeDescriptor * symbolDescriptor;
```

## Discussion

The property is a [`CIQRCodeDescriptor`](../ciqrcodedescriptor.md) instance that contains the payload, symbol version, mask pattern, and error correction level, so the QR Code can be reproduced.

## See Also

### Decoding a Detected Barcode
- [var messageString: String?](./messagestring.md)
  The string decoded from the detected barcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/symboldescriptor-swift.property)*