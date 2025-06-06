# SecureEnclave.P256.KeyAgreement

**Framework**: Apple CryptoKit  
**Kind**: enum

A mechanism used to create a shared secret between two users by performing NIST P-256 elliptic curve Diffie Hellman (ECDH) key exchange within the Secure Enclave.

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
- [SecureEnclave.P256.KeyAgreement.PrivateKey](secureenclave/p256/keyagreement/privatekey.md)
  A P-256 private key used for key agreement.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [SecureEnclave.P256.Signing](secureenclave/p256/signing.md)
  A mechanism used to create or verify a cryptographic signature using the NIST P-256 elliptic curve digital signature algorithm (ECDSA) within the Secure Enclave.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/p256/keyagreement)*