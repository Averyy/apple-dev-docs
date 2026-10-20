# aead

**Framework**: Apple CryptoKit  
**Kind**: property  
**Role**: Instance Property

The authenticated encryption with additional data (AEAD) algorithm for encrypting and decrypting messages.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
let aead: HPKE.AEAD
```

## See Also

### Inspecting a cipher suite
- [let kdf: HPKE.KDF](./kdf.md)
  The key derivation function (KDF) for deriving the symmetric key.
- [let kem: HPKE.KEM](./kem.md)
  The key encapsulation mechanism (KEM) for encapsulating the symmetric key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpke/ciphersuite/aead)*