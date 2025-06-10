# MLKEM768.PrivateKey

**Framework**: Apple CryptoKit  
**Kind**: struct

A private key you use to decapsulate shared secrets with the Module-Lattice key encapsulation mechanism.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct PrivateKey
```

## Topics

### Creating a private key
- [static func generate() throws -> MLKEM768.PrivateKey](mlkem768/privatekey/generate.md)
  Generates a new, random private key.
- [init() throws](mlkem768/privatekey/init.md)
  Initializes a random private key.
- [init<D>(integrityCheckedRepresentation: D) throws](mlkem768/privatekey/init(integritycheckedrepresentation:).md)
  Initializes a private key from an integrity-checked representation.
- [init<D>(seedRepresentation: D, publicKey: MLKEM768.PublicKey?) throws](mlkem768/privatekey/init(seedrepresentation:publickey:).md)
  Initializes a private key from a seed representation and optional public key.
### Inspecting a private key’s properties
- [var integrityCheckedRepresentation: Data](mlkem768/privatekey/integritycheckedrepresentation.md)
  An integrity-checked representation of the private key.
- [var publicKey: MLKEM768.PublicKey](mlkem768/privatekey/publickey.md)
  The corresponding public key.
- [var seedRepresentation: Data](mlkem768/privatekey/seedrepresentation.md)
  The private key’s seed representation.
### Decapsulating shared secrets
- [func decapsulate<D>(D) throws -> SymmetricKey](mlkem768/privatekey/decapsulate(_:).md)
  Decapsulated a shared secret.

## Relationships

### Conforms To
- [KEMPrivateKey](kemprivatekey.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MLKEM768.PublicKey](mlkem768/publickey.md)
  A public key you use to encapsulate shared secrets with the Module-Lattice key encapsulation mechanism.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mlkem768/privatekey)*