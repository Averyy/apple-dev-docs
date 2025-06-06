# HPKE.AEAD

**Framework**: Apple CryptoKit  
**Kind**: enum

The authenticated encryption with associated data (AEAD) algorithms to use in HPKE.

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
enum AEAD
```

## Topics

### Enumeration Cases
- [HPKE.AEAD.AES_GCM_128](hpke/aead/aes_gcm_128.md)
  An Advanced Encryption Standard cipher in Galois/Counter Mode with a key length of 128 bits.
- [HPKE.AEAD.AES_GCM_256](hpke/aead/aes_gcm_256.md)
  An Advanced Encryption Standard cipher in Galois/Counter Mode with a key length of 256 bits.
- [HPKE.AEAD.chaChaPoly](hpke/aead/chachapoly.md)
  A ChaCha20 stream cipher with the Poly1305 message authentication code.
- [HPKE.AEAD.exportOnly](hpke/aead/exportonly.md)
  An export-only mode.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct Ciphersuite](hpke/ciphersuite.md)
  Cipher suites to use in hybrid public key encryption.
- [HPKE.KDF](hpke/kdf.md)
  The key derivation functions to use in HPKE.
- [HPKE.KEM](hpke/kem.md)
  The key encapsulation mechanisms to use in HPKE.
- [HPKE.DHKEM](hpke/dhkem.md)
  A container for Diffie-Hellman key encapsulation mechanisms (KEMs).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpke/aead)*