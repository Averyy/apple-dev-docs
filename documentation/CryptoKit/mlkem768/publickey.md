# MLKEM768.PublicKey

**Framework**: Apple CryptoKit  
**Kind**: struct

A public key you use to encapsulate shared secrets with the Module-Lattice key encapsulation mechanism.

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