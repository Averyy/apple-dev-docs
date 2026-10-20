# MLKEM768.PrivateKey

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

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
- [static func generate() throws -> MLKEM768.PrivateKey](./privatekey/generate%28%29.md)
  Generates a new, random private key.
- [init() throws](./privatekey/init%28%29.md)
  Initializes a random private key.
- [init<D>(integrityCheckedRepresentation: D) throws](./privatekey/init%28integritycheckedrepresentation%29.md)
  Initializes a private key from an integrity-checked representation.
- [init<D>(seedRepresentation: D, publicKey: MLKEM768.PublicKey?) throws](./privatekey/init%28seedrepresentation,publickey%29.md)
  Initializes a private key from a seed representation and optional public key.
### Inspecting a private key’s properties
- [var integrityCheckedRepresentation: Data](./privatekey/integritycheckedrepresentation.md)
  An integrity-checked representation of the private key.
- [var publicKey: MLKEM768.PublicKey](./privatekey/publickey.md)
  The corresponding public key.
- [var seedRepresentation: Data](./privatekey/seedrepresentation.md)
  The private key’s seed representation.
### Decapsulating shared secrets
- [func decapsulate<D>(D) throws -> SymmetricKey](./privatekey/decapsulate%28_%29.md)
  Decapsulate a shared secret.

## Relationships

### Conforms To
- [KEMPrivateKey](../kemprivatekey.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Keys
- [MLKEM768.PublicKey](./publickey.md)
  A public key you use to encapsulate shared secrets with the Module-Lattice key encapsulation mechanism.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mlkem768/privatekey)*