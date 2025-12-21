# XWingMLKEM768X25519.PublicKey

**Framework**: Apple CryptoKit  
**Kind**: struct

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
struct PublicKey
```

## Topics

### Accessing a key’s raw representation
- [var rawRepresentation: Data](xwingmlkem768x25519/publickey/rawrepresentation.md)
### Accessing the corresponding private key type
- [XWingMLKEM768X25519.PublicKey.HPKEEphemeralPrivateKey](xwingmlkem768x25519/publickey/hpkeephemeralprivatekey.md)
  The type of the ephemeral private key associated with this public key.
### Initializers
- [init<D>(rawRepresentation: D) throws](xwingmlkem768x25519/publickey/init(rawrepresentation:).md)
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