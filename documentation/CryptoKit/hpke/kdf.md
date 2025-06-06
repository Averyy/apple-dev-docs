# HPKE.KDF

**Framework**: Apple CryptoKit  
**Kind**: enum

The key derivation functions to use in HPKE.

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
enum KDF
```

## Topics

### Enumeration Cases
- [HPKE.KDF.HKDF_SHA256](hpke/kdf/hkdf_sha256.md)
  An HMAC-based key derivation function that uses SHA-2 hashing with a 256-bit digest.
- [HPKE.KDF.HKDF_SHA384](hpke/kdf/hkdf_sha384.md)
  An HMAC-based key derivation function that uses SHA-2 hashing with a 384-bit digest.
- [HPKE.KDF.HKDF_SHA512](hpke/kdf/hkdf_sha512.md)
  An HMAC-based key derivation function that uses SHA-2 hashing with a 512-bit digest.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct Ciphersuite](hpke/ciphersuite.md)
  Cipher suites to use in hybrid public key encryption.
- [HPKE.AEAD](hpke/aead.md)
  The authenticated encryption with associated data (AEAD) algorithms to use in HPKE.
- [HPKE.KEM](hpke/kem.md)
  The key encapsulation mechanisms to use in HPKE.
- [HPKE.DHKEM](hpke/dhkem.md)
  A container for Diffie-Hellman key encapsulation mechanisms (KEMs).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpke/kdf)*