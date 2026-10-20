# nonce

**Framework**: Apple CryptoKit  
**Kind**: property  
**Role**: Instance Property

The nonce used to encrypt the data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var nonce: AES.GCM.Nonce { get }
```

## See Also

### Inspecting the component elements
- [var ciphertext: Data](./ciphertext.md)
  The encrypted data.
- [var tag: Data](./tag.md)
  An authentication tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/aes/gcm/sealedbox/nonce)*