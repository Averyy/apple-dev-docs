# HPKEKEMPrivateKey

**Framework**: Apple CryptoKit  
**Kind**: protocol

A type that represents the private key in HPKE.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 1.0+
- watchOS 26.0+ (Beta)

## Declaration

```swift
@preconcurrency
protocol HPKEKEMPrivateKey : KEMPrivateKey where Self.PublicKey : HPKEKEMPublicKey
```

## Relationships

### Inherits From
- [KEMPrivateKey](kemprivatekey.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Inherited By
- [HPKEKEMPrivateKeyGeneration](hpkekemprivatekeygeneration.md)
### Conforming Types
- [XWingMLKEM768X25519.PrivateKey](xwingmlkem768x25519/privatekey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpkekemprivatekey)*