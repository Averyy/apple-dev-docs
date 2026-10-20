# P521.KeyAgreement

**Framework**: Apple CryptoKit  
**Kind**: enum  
**Role**: Enumeration

A mechanism used to create a shared secret between two users by performing NIST P-521 elliptic curve Diffie Hellman (ECDH) key exchange.

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
enum KeyAgreement
```

## Topics

### Using keys
- [P521.KeyAgreement.PrivateKey](./keyagreement/privatekey.md)
  A P-521 private key used for key agreement.
- [P521.KeyAgreement.PublicKey](./keyagreement/publickey.md)
  A P-521 public key used for key agreement.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Performing operations
- [P521.Signing](./signing.md)
  A mechanism used to create or verify a cryptographic signature using the NIST P-521 elliptic curve digital signature algorithm (ECDSA).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/p521/keyagreement)*