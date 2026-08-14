# MLKEM768.OneTimePrivateKey

**Framework**: Apple CryptoKit  
**Kind**: struct

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct OneTimePrivateKey
```

## Topics

### Initializers
- [init() throws](mlkem768/onetimeprivatekey/init.md)
  Initializes a random one-time-use private key.
### Instance Properties
- [var publicKey: MLKEM768.PublicKey](mlkem768/onetimeprivatekey/publickey.md)
  The corresponding public key.
### Instance Methods
- [func decapsulate<D>(D) throws -> SymmetricKey](mlkem768/onetimeprivatekey/decapsulate(_:).md)
  Decapsulate a shared secret.
### Type Methods
- [static func generate() throws -> MLKEM768.OneTimePrivateKey](mlkem768/onetimeprivatekey/generate.md)
  Generates a new, random one-time-use private key.

## Relationships

### Conforms To
- [KEMOneTimePrivateKey](kemonetimeprivatekey.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mlkem768/onetimeprivatekey)*