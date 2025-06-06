# SecureEnclave.P256.Signing.PrivateKey

**Framework**: Apple CryptoKit  
**Kind**: struct

A P-256 private key used for signing.

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
struct PrivateKey
```

## Topics

### Creating a private key
- [init(dataRepresentation: Data) throws](secureenclave/p256/signing/privatekey/init(datarepresentation:).md)
  Creates a P-256 private key for signing from the specified data representation.
- [init(dataRepresentation: Data, authenticationContext: LAContext?) throws](secureenclave/p256/signing/privatekey/init(datarepresentation:authenticationcontext:).md)
  Creates a P-256 private key for signing from a data representation of the key with the given authentication context.
- [init(compactRepresentable: Bool, accessControl: SecAccessControl) throws](secureenclave/p256/signing/privatekey/init(compactrepresentable:accesscontrol:).md)
  Creates a P-256 private key for signing with the specified access control.
- [init(compactRepresentable: Bool, accessControl: SecAccessControl, authenticationContext: LAContext?) throws](secureenclave/p256/signing/privatekey/init(compactrepresentable:accesscontrol:authenticationcontext:).md)
  Creates a P-256 private key for signing with the specified access control.
### Representing the key
- [let dataRepresentation: Data](secureenclave/p256/signing/privatekey/datarepresentation.md)
  A data representation of the private key.
### Getting the public key
- [let publicKey: P256.Signing.PublicKey](secureenclave/p256/signing/privatekey/publickey.md)
  The corresponding public key.
### Generating a signature
- [func signature<D>(for: D) throws -> P256.Signing.ECDSASignature](secureenclave/p256/signing/privatekey/signature(for:)-3xogs.md)
  Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the digest you provide over the P-256 elliptic curve.
- [func signature<D>(for: D) throws -> P256.Signing.ECDSASignature](secureenclave/p256/signing/privatekey/signature(for:)-76j0u.md)
  Generates an elliptic curve digital signature algorithm (ECDSA) signature of the given data over the P-256 elliptic curve, using SHA-256 as the hash function.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/p256/signing/privatekey)*