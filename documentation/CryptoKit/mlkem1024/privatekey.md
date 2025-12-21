# MLKEM1024.PrivateKey

**Framework**: Apple CryptoKit  
**Kind**: struct

A private key you use to decapsulate shared secrets with the Module-Lattice key encapsulation mechanism.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct PrivateKey
```

## Topics

### Creating a private key
- [static func generate() throws -> MLKEM1024.PrivateKey](mlkem1024/privatekey/generate.md)
  Generates a new, random private key.
- [init() throws](mlkem1024/privatekey/init.md)
  Initializes a random private key.
- [init<D>(integrityCheckedRepresentation: D) throws](mlkem1024/privatekey/init(integritycheckedrepresentation:).md)
  Initializes a private key from an integrity-checked representation.
- [init<D>(seedRepresentation: D, publicKey: MLKEM1024.PublicKey?) throws](mlkem1024/privatekey/init(seedrepresentation:publickey:).md)
  Initializes a private key from a seed representation and optional public key.
### Inspecting a private key’s properties
- [var integrityCheckedRepresentation: Data](mlkem1024/privatekey/integritycheckedrepresentation.md)
  An integrity-checked representation of the private key.
- [var publicKey: MLKEM1024.PublicKey](mlkem1024/privatekey/publickey.md)
  The corresponding public key.
- [var seedRepresentation: Data](mlkem1024/privatekey/seedrepresentation.md)
  The private key’s seed representation.
### Decapsulating shared secrets
- [func decapsulate<D>(D) throws -> SymmetricKey](mlkem1024/privatekey/decapsulate(_:).md)
  Decapsulated a shared secret.

## Relationships

### Conforms To
- [KEMPrivateKey](kemprivatekey.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MLKEM1024.PublicKey](mlkem1024/publickey.md)
  A public key you use to encapsulate shared secrets with the Module-Lattice key encapsulation mechanism.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mlkem1024/privatekey)*