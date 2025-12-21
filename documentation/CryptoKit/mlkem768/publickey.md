# MLKEM768.PublicKey

**Framework**: Apple CryptoKit  
**Kind**: struct

A public key you use to encapsulate shared secrets with the Module-Lattice key encapsulation mechanism.

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
struct PublicKey
```

## Topics

### Creating a public key
- [init<D>(rawRepresentation: D) throws](mlkem768/publickey/init(rawrepresentation:).md)
  Initializes a public key from a raw representation.
### Accessing a key’s raw representation
- [var rawRepresentation: Data](mlkem768/publickey/rawrepresentation.md)
  A serialized representation of the public key.
### Encapsulating a shared secret
- [func encapsulate() throws -> KEM.EncapsulationResult](mlkem768/publickey/encapsulate.md)
  Generates and encapsulates a shared secret.

## Relationships

### Conforms To
- [KEMPublicKey](kempublickey.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MLKEM768.PrivateKey](mlkem768/privatekey.md)
  A private key you use to decapsulate shared secrets with the Module-Lattice key encapsulation mechanism.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mlkem768/publickey)*