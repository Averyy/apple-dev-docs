# HPKE.KDF

**Framework**: Apple CryptoKit  
**Kind**: enum  
**Role**: Enumeration

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
- [HPKE.KDF.HKDF_SHA256](./kdf/hkdf_sha256.md)
  An HMAC-based key derivation function that uses SHA-2 hashing with a 256-bit digest.
- [HPKE.KDF.HKDF_SHA384](./kdf/hkdf_sha384.md)
  An HMAC-based key derivation function that uses SHA-2 hashing with a 384-bit digest.
- [HPKE.KDF.HKDF_SHA512](./kdf/hkdf_sha512.md)
  An HMAC-based key derivation function that uses SHA-2 hashing with a 512-bit digest.

## Relationships

### Conforms To
- [CaseIterable](../../Swift/caseiterable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Choosing cryptographic algorithms
- [struct Ciphersuite](./ciphersuite.md)
  Cipher suites to use in hybrid public key encryption (HPKE).
- [HPKE.AEAD](./aead.md)
  The authenticated encryption with associated data (AEAD) algorithms to use in HPKE.
- [HPKE.KEM](./kem.md)
  The key encapsulation mechanisms to use in HPKE.
- [HPKE.DHKEM](./dhkem.md)
  A container for Diffie-Hellman key encapsulation mechanisms (KEMs).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpke/kdf)*