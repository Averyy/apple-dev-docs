# SecureEnclave.P256.KeyAgreement.PrivateKey

**Framework**: Apple CryptoKit  
**Kind**: struct

A P-256 private key used for key agreement.

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
- [init(dataRepresentation: Data) throws](secureenclave/p256/keyagreement/privatekey/init(datarepresentation:).md)
  Creates a P-256 private key for key agreement from the specified data representation.
- [init(dataRepresentation: Data, authenticationContext: LAContext?) throws](secureenclave/p256/keyagreement/privatekey/init(datarepresentation:authenticationcontext:).md)
  Creates a P-256 private key for key agreement from a data representation of the key with the given authentication context.
- [init(compactRepresentable: Bool, accessControl: SecAccessControl) throws](secureenclave/p256/keyagreement/privatekey/init(compactrepresentable:accesscontrol:).md)
  Creates a P-256 private key for key agreement with the specified access control.
- [init(compactRepresentable: Bool, accessControl: SecAccessControl, authenticationContext: LAContext?) throws](secureenclave/p256/keyagreement/privatekey/init(compactrepresentable:accesscontrol:authenticationcontext:).md)
  Creates a P-256 private key for key agreement with the specified access control.
### Representing the key
- [let dataRepresentation: Data](secureenclave/p256/keyagreement/privatekey/datarepresentation.md)
  A data representation of the private key.
### Finding the public key
- [let publicKey: P256.KeyAgreement.PublicKey](secureenclave/p256/keyagreement/privatekey/publickey.md)
  The corresponding public key.
### Creating a shared secret
- [func sharedSecretFromKeyAgreement(with: P256.KeyAgreement.PublicKey) throws -> SharedSecret](secureenclave/p256/keyagreement/privatekey/sharedsecretfromkeyagreement(with:).md)
  Computes a shared secret with the provided public key from another party.
- [struct SharedSecret](sharedsecret.md)
  A key agreement result from which you can derive a symmetric cryptographic key.
### Default Implementations
- [DiffieHellmanKeyAgreement Implementations](secureenclave/p256/keyagreement/privatekey/diffiehellmankeyagreement-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [DiffieHellmanKeyAgreement](diffiehellmankeyagreement.md)
- [HPKEDiffieHellmanPrivateKey](hpkediffiehellmanprivatekey.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/p256/keyagreement/privatekey)*