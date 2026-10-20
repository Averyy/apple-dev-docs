# init(nonce:ciphertext:tag:)

**Framework**: Apple CryptoKit  
**Kind**: init  
**Role**: Initializer

Creates a sealed box from the given tag, nonce, and ciphertext.

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
init<C, T>(nonce: AES.GCM.Nonce, ciphertext: C, tag: T) throws where C : DataProtocol, T : DataProtocol
```

## Parameters

- `nonce`: The nonce.
- `ciphertext`: The encrypted data.
- `tag`: The authentication tag.

## See Also

### Creating the sealed box
- [init<D>(combined: D) throws](./init%28combined%29.md)
  Creates a sealed box from the combined bytes of an authentication tag, nonce, and encrypted data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/aes/gcm/sealedbox/init(nonce:ciphertext:tag:))*