# MLKEM1024.OneTimePrivateKey

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct OneTimePrivateKey
```

## Topics

### Initializers
- [init() throws](./onetimeprivatekey/init%28%29.md)
  Initializes a random one-time-use private key.
### Instance Properties
- [var publicKey: MLKEM1024.PublicKey](./onetimeprivatekey/publickey.md)
  The corresponding public key.
### Instance Methods
- [func decapsulate<D>(D) throws -> SymmetricKey](./onetimeprivatekey/decapsulate%28_%29.md)
  Decapsulate a shared secret.
### Type Methods
- [static func generate() throws -> MLKEM1024.OneTimePrivateKey](./onetimeprivatekey/generate%28%29.md)
  Generates a new, random one-time-use private key.

## Relationships

### Conforms To
- [KEMOneTimePrivateKey](../kemonetimeprivatekey.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mlkem1024/onetimeprivatekey)*