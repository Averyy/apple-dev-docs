# KEMPrivateKey

**Framework**: Apple CryptoKit  
**Kind**: protocol

The private key for a key encapsulation mechanism.

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
  The associated public key.
### Instance Methods
- [func decapsulate(Data) throws -> SymmetricKey](kemprivatekey/decapsulate(_:).md)
  Recovers a shared secret from an encapsulated representation.
### Type Methods
- [static func generate() throws -> Self](kemprivatekey/generate.md)
  Generates a new random private key.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Inherited By
- [HPKEKEMPrivateKey](hpkekemprivatekey.md)
- [HPKEKEMPrivateKeyGeneration](hpkekemprivatekeygeneration.md)
### Conforming Types
- [MLKEM1024.PrivateKey](mlkem1024/privatekey.md)
- [MLKEM768.PrivateKey](mlkem768/privatekey.md)
- [SecureEnclave.MLKEM1024.PrivateKey](secureenclave/mlkem1024/privatekey.md)
- [SecureEnclave.MLKEM768.PrivateKey](secureenclave/mlkem768/privatekey.md)
- [XWingMLKEM768X25519.PrivateKey](xwingmlkem768x25519/privatekey.md)

## See Also

- [protocol KEMPublicKey](kempublickey.md)
  The public key for a key encapsulation mechanism.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/kemprivatekey)*