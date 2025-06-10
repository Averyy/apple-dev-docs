# integrityCheckedRepresentation

**Framework**: Apple CryptoKit  
**Kind**: property

The integrity-checked data representation of the private key.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var integrityCheckedRepresentation: Data { get }
```

#### Discussion

This representation is 64 bytes long, and contains the seed and a hash of the public key.

## See Also

- [var publicKey: MLDSA65.PublicKey](mldsa65/privatekey/publickey.md)
  The associated public key.
- [var seedRepresentation: Data](mldsa65/privatekey/seedrepresentation.md)
  The seed representation of the private key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mldsa65/privatekey/integritycheckedrepresentation)*