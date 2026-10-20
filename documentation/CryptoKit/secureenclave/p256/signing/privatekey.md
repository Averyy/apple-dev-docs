# SecureEnclave.P256.Signing.PrivateKey

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

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
- [init(dataRepresentation: Data, authenticationContext: LAContext?) throws](./privatekey/init%28datarepresentation,authenticationcontext%29.md)
  Creates a P-256 private key for signing from a data representation of the key with the given authentication context.
- [init(compactRepresentable: Bool, accessControl: SecAccessControl, authenticationContext: LAContext?) throws](./privatekey/init%28compactrepresentable,accesscontrol,authenticationcontext%29.md)
  Creates a P-256 private key for signing with the specified access control.
### Representing the key
- [let dataRepresentation: Data](./privatekey/datarepresentation.md)
  A data representation of the private key.
### Getting the public key
- [let publicKey: P256.Signing.PublicKey](./privatekey/publickey.md)
  The corresponding public key.
### Generating a signature
- [func signature<D>(for: D) throws -> P256.Signing.ECDSASignature](./privatekey/signature%28for%29-3xogs.md)
  Generates an Elliptic Curve Digital Signature Algorithm (ECDSA) signature of the digest you provide over the P-256 elliptic curve.
- [func signature<D>(for: D) throws -> P256.Signing.ECDSASignature](./privatekey/signature%28for%29-76j0u.md)
  Generates an elliptic curve digital signature algorithm (ECDSA) signature of the given data over the P-256 elliptic curve, using SHA-256 as the hash function.
### Initializers
- [init(compactRepresentable: Bool, accessControl: SecAccessControl) throws](./privatekey/init%28compactrepresentable,accesscontrol%29.md)
  Creates a P-256 private key for signing with the specified access control.
- [init(dataRepresentation: Data) throws](./privatekey/init%28datarepresentation%29.md)
  Creates a P-256 private key for signing from the specified data representation.

## Relationships

### Conforms To
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/p256/signing/privatekey)*