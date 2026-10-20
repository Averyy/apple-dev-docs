# SecureEnclave.P256.KeyAgreement.PrivateKey

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

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
- [init(dataRepresentation: Data, authenticationContext: LAContext?) throws](./privatekey/init%28datarepresentation,authenticationcontext%29.md)
  Creates a P-256 private key for key agreement from a data representation of the key with the given authentication context.
- [init(compactRepresentable: Bool, accessControl: SecAccessControl, authenticationContext: LAContext?) throws](./privatekey/init%28compactrepresentable,accesscontrol,authenticationcontext%29.md)
  Creates a P-256 private key for key agreement with the specified access control.
### Representing the key
- [let dataRepresentation: Data](./privatekey/datarepresentation.md)
  A data representation of the private key.
### Finding the public key
- [let publicKey: P256.KeyAgreement.PublicKey](./privatekey/publickey.md)
  The corresponding public key.
### Creating a shared secret
- [func sharedSecretFromKeyAgreement(with: P256.KeyAgreement.PublicKey) throws -> SharedSecret](./privatekey/sharedsecretfromkeyagreement%28with%29.md)
  Computes a shared secret with the provided public key from another party.
- [struct SharedSecret](../../../sharedsecret.md)
  A key agreement result from which you can derive a symmetric cryptographic key.
### Initializers
- [init(compactRepresentable: Bool, accessControl: SecAccessControl) throws](./privatekey/init%28compactrepresentable,accesscontrol%29.md)
  Creates a P-256 private key for key agreement with the specified access control.
- [init(dataRepresentation: Data) throws](./privatekey/init%28datarepresentation%29.md)
  Creates a P-256 private key for key agreement from the specified data representation.
### Default Implementations
- [DiffieHellmanKeyAgreement Implementations](./privatekey/diffiehellmankeyagreement-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../../../Swift/copyable.md)
- [DiffieHellmanKeyAgreement](../../../diffiehellmankeyagreement.md)
- [Escapable](../../../../Swift/escapable.md)
- [HPKEDiffieHellmanPrivateKey](../../../hpkediffiehellmanprivatekey.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/p256/keyagreement/privatekey)*