# XWingMLKEM768X25519.PublicKey

**Framework**: Apple CryptoKit  
**Kind**: struct

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

### Creating and comparing public keys
- [init<D>(dataRepresentation: D) throws](xwingmlkem768x25519/publickey/init(datarepresentation:).md)
### Accessing a key’s raw representation
- [var rawRepresentation: Data](xwingmlkem768x25519/publickey/rawrepresentation.md)
### Accessing the corresponding private key type
- [XWingMLKEM768X25519.PublicKey.HPKEEphemeralPrivateKey](xwingmlkem768x25519/publickey/hpkeephemeralprivatekey.md)
  The type of the ephemeral private key associated with this public key.
### Default Implementations
- [HPKEKEMPublicKey Implementations](xwingmlkem768x25519/publickey/hpkekempublickey-implementations.md)
- [HPKEPublicKeySerialization Implementations](xwingmlkem768x25519/publickey/hpkepublickeyserialization-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [HPKEKEMPublicKey](hpkekempublickey.md)
- [HPKEPublicKeySerialization](hpkepublickeyserialization.md)
- [KEMPublicKey](kempublickey.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [XWingMLKEM768X25519.PrivateKey](xwingmlkem768x25519/privatekey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/xwingmlkem768x25519/publickey)*