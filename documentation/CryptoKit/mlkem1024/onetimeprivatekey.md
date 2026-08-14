# MLKEM1024.OneTimePrivateKey

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
- [init() throws](mlkem1024/onetimeprivatekey/init.md)
  Initializes a random one-time-use private key.
### Instance Properties
- [var publicKey: MLKEM1024.PublicKey](mlkem1024/onetimeprivatekey/publickey.md)
  The corresponding public key.
### Instance Methods
- [func decapsulate<D>(D) throws -> SymmetricKey](mlkem1024/onetimeprivatekey/decapsulate(_:).md)
  Decapsulate a shared secret.
### Type Methods
- [static func generate() throws -> MLKEM1024.OneTimePrivateKey](mlkem1024/onetimeprivatekey/generate.md)
  Generates a new, random one-time-use private key.

## Relationships

### Conforms To
- [KEMOneTimePrivateKey](kemonetimeprivatekey.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mlkem1024/onetimeprivatekey)*