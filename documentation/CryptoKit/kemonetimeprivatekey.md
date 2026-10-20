# KEMOneTimePrivateKey

**Framework**: Apple CryptoKit  
**Kind**: protocol  
**Role**: Protocol

A one-time private key for a key encapsulation mechanism, which can only decapsulate once but it does so faster.

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
@preconcurrency
protocol KEMOneTimePrivateKey : Sendable, ~Copyable
```

## Topics

### Associated Types
- [associatedtype PublicKey : KEMPublicKey](./kemonetimeprivatekey/publickey-swift.associatedtype.md)
### Instance Properties
- [var publicKey: Self.PublicKey](./kemonetimeprivatekey/publickey-swift.property.md)
  The associated public key.
### Instance Methods
- [func decapsulate(Data) throws -> SymmetricKey](./kemonetimeprivatekey/decapsulate%28_%29.md)
  Recovers a shared secret from an encapsulated representation.
### Type Methods
- [static func generate() throws -> Self](./kemonetimeprivatekey/generate%28%29.md)
  Generates a new random private key.

## Relationships

### Inherits From
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Conforming Types
- [MLKEM1024.OneTimePrivateKey](./mlkem1024/onetimeprivatekey.md)
- [MLKEM768.OneTimePrivateKey](./mlkem768/onetimeprivatekey.md)
- [XWingMLKEM768X25519.OneTimePrivateKey](./xwingmlkem768x25519/onetimeprivatekey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/kemonetimeprivatekey)*