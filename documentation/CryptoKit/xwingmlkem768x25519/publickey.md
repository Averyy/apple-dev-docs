# XWingMLKEM768X25519.PublicKey

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

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
- [var rawRepresentation: Data](./publickey/rawrepresentation.md)
### Accessing the corresponding private key type
- [XWingMLKEM768X25519.PublicKey.HPKEEphemeralPrivateKey](./publickey/hpkeephemeralprivatekey.md)
  The type of the ephemeral private key associated with this public key.
### Initializers
- [init<D>(rawRepresentation: D) throws](./publickey/init%28rawrepresentation%29.md)
### Default Implementations
- [HPKEKEMPublicKey Implementations](./publickey/hpkekempublickey-implementations.md)
- [HPKEPublicKeySerialization Implementations](./publickey/hpkepublickeyserialization-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Escapable](../../Swift/escapable.md)
- [HPKEKEMPublicKey](../hpkekempublickey.md)
- [HPKEPublicKeySerialization](../hpkepublickeyserialization.md)
- [KEMPublicKey](../kempublickey.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Keys
- [XWingMLKEM768X25519.PrivateKey](./privatekey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/xwingmlkem768x25519/publickey)*