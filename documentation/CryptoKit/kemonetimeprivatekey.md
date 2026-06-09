# KEMOneTimePrivateKey

**Framework**: Apple CryptoKit  
**Kind**: protocol

A one-time private key for a key encapsulation mechanism, which can only decapsulate once but it does so faster.

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
@preconcurrency
protocol KEMOneTimePrivateKey : Sendable, ~Copyable
```

## Topics

### Associated Types
- [associatedtype PublicKey : KEMPublicKey](kemonetimeprivatekey/publickey-swift.associatedtype.md)
### Instance Properties
- [var publicKey: Self.PublicKey](kemonetimeprivatekey/publickey-swift.property.md)
  The associated public key.
### Instance Methods
- [func decapsulate(Data) throws -> SymmetricKey](kemonetimeprivatekey/decapsulate(_:).md)
  Recovers a shared secret from an encapsulated representation.
### Type Methods
- [static func generate() throws -> Self](kemonetimeprivatekey/generate.md)
  Generates a new random private key.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [MLKEM1024.OneTimePrivateKey](mlkem1024/onetimeprivatekey.md)
- [MLKEM768.OneTimePrivateKey](mlkem768/onetimeprivatekey.md)
- [XWingMLKEM768X25519.OneTimePrivateKey](xwingmlkem768x25519/onetimeprivatekey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/kemonetimeprivatekey)*