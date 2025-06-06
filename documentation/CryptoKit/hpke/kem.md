# HPKE.KEM

**Framework**: Apple CryptoKit  
**Kind**: enum

The key encapsulation mechanisms to use in HPKE.

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
enum KEM
```

## Topics

### Enumeration Cases
- [HPKE.KEM.Curve25519_HKDF_SHA256](hpke/kem/curve25519_hkdf_sha256.md)
  A key encapsulation mechanism using X25519 elliptic curve key agreement and SHA-2 hashing with a 256-bit digest.
- [HPKE.KEM.P256_HKDF_SHA256](hpke/kem/p256_hkdf_sha256.md)
  A key encapsulation mechanism using NIST P-256 elliptic curve key agreement and SHA-2 hashing with a 256-bit digest.
- [HPKE.KEM.P384_HKDF_SHA384](hpke/kem/p384_hkdf_sha384.md)
  A key encapsulation mechanism using NIST P-384 elliptic curve key agreement and SHA-2 hashing with a 384-bit digest.
- [HPKE.KEM.P521_HKDF_SHA512](hpke/kem/p521_hkdf_sha512.md)
  A key encapsulation mechanism using NIST P-521 elliptic curve key agreement and SHA-2 hashing with a 512-bit digest.

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
- [HPKE.KDF](hpke/kdf.md)
  The key derivation functions to use in HPKE.
- [HPKE.DHKEM](hpke/dhkem.md)
  A container for Diffie-Hellman key encapsulation mechanisms (KEMs).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpke/kem)*