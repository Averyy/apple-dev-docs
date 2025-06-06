# KEMPrivateKey

**Framework**: Apple CryptoKit  
**Kind**: protocol

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@preconcurrency
protocol KEMPrivateKey : Sendable
```

## Topics

### Associated Types
- [associatedtype PublicKey : KEMPublicKey](kemprivatekey/publickey-swift.associatedtype.md)
### Instance Properties
- [var publicKey: Self.PublicKey](kemprivatekey/publickey-swift.property.md)
  Returns the associated public key
### Instance Methods
- [func decapsulate(Data) throws -> SymmetricKey](kemprivatekey/decapsulate(_:).md)
  Decapsulates the encapsulated shared secret
### Type Methods
- [static func generate() throws -> Self](kemprivatekey/generate.md)
  Generate a new random Private Key

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/kemprivatekey)*