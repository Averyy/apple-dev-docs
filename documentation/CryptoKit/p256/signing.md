# P256.Signing

**Framework**: Apple CryptoKit  
**Kind**: enum

A mechanism used to create or verify a cryptographic signature using the NIST P-256 elliptic curve digital signature algorithm (ECDSA).

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
enum Signing
```

## Topics

### Using keys
- [P256.Signing.PrivateKey](p256/signing/privatekey.md)
  A P-256 private key used to create cryptographic signatures.
- [P256.Signing.PublicKey](p256/signing/publickey.md)
  A P-256 public key used to verify cryptographic signatures.
### Structures
- [P256.Signing.ECDSASignature](p256/signing/ecdsasignature.md)
  A P-256 elliptic curve digital signature algorithm (ECDSA) signature.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [P256.KeyAgreement](p256/keyagreement.md)
  A mechanism used to create a shared secret between two users by performing NIST P-256 elliptic curve Diffie Hellman (ECDH) key exchange.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p256/signing)*