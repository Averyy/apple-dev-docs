# SecureEnclave.P256.KeyAgreement

**Framework**: Apple CryptoKit  
**Kind**: enum  
**Role**: Enumeration

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
- [SecureEnclave.P256.KeyAgreement.PrivateKey](./keyagreement/privatekey.md)
  A P-256 private key used for key agreement.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Performing operations
- [SecureEnclave.P256.Signing](./signing.md)
  A mechanism used to create or verify a cryptographic signature using the NIST P-256 elliptic curve digital signature algorithm (ECDSA) within the Secure Enclave.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/p256/keyagreement)*