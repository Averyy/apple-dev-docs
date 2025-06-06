# ASAuthorizationProviderExtensionEncryptionAlgorithm

**Framework**: Authentication Services  
**Kind**: struct

**Availability**:
- macOS 15.0+

## Declaration

```swift
struct ASAuthorizationProviderExtensionEncryptionAlgorithm
```

## Topics

### Initializers
- [init(NSNumber)](asauthorizationproviderextensionencryptionalgorithm/init(_:).md)
- [init(rawValue: NSNumber)](asauthorizationproviderextensionencryptionalgorithm/init(rawvalue:).md)
### Type Properties
- [static let ecdhe_A256GCM: ASAuthorizationProviderExtensionEncryptionAlgorithm](asauthorizationproviderextensionencryptionalgorithm/ecdhe_a256gcm.md)
  A encryption algorithm that uses NIST P-256 elliptic curve key agreement, ConcatKDF key derivation with a 256-bit digest, and the Advanced Encryption Standard cipher in Galois/Counter Mode with a key length of 256 bits.
- [static let hpke_Curve25519_SHA256_ChachaPoly: ASAuthorizationProviderExtensionEncryptionAlgorithm](asauthorizationproviderextensionencryptionalgorithm/hpke_curve25519_sha256_chachapoly.md)
  A cipher suite for HPKE that uses X25519 elliptic curve key agreement, SHA-2 key derivation with a 256-bit digest, and the ChaCha20 stream cipher with the Poly1305 message authentication code.
- [static let hpke_P256_SHA256_AES_GCM_256: ASAuthorizationProviderExtensionEncryptionAlgorithm](asauthorizationproviderextensionencryptionalgorithm/hpke_p256_sha256_aes_gcm_256.md)
  A cipher suite for HPKE that uses NIST P-256 elliptic curve key agreement, SHA-2 key derivation with a 256-bit digest, and the Advanced Encryption Standard cipher in Galois/Counter Mode with a key length of 256 bits.
- [static let hpke_P384_SHA384_AES_GCM_256: ASAuthorizationProviderExtensionEncryptionAlgorithm](asauthorizationproviderextensionencryptionalgorithm/hpke_p384_sha384_aes_gcm_256.md)
  A cipher suite that you use for HPKE using NIST P-384 elliptic curve key agreement, SHA-2 key derivation with a 384-bit digest, and the Advanced Encryption Standard cipher in Galois/Counter Mode with a key length of 256 bits.

## Relationships

### Conforms To
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationproviderextensionencryptionalgorithm)*