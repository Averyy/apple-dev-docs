# XWingMLKEM768X25519.PrivateKey

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
struct PrivateKey
```

## Topics

### Creating a private key
- [init<D>(integrityCheckedRepresentation: D) throws](xwingmlkem768x25519/privatekey/init(integritycheckedrepresentation:).md)
- [init<D>(seedRepresentation: D, publicKey: XWingMLKEM768X25519.PublicKey?) throws](xwingmlkem768x25519/privatekey/init(seedrepresentation:publickey:).md)
### Inspecting a private key’s properties
- [var dataRepresentation: Data](xwingmlkem768x25519/privatekey/datarepresentation.md)
- [var integrityCheckedRepresentation: Data](xwingmlkem768x25519/privatekey/integritycheckedrepresentation.md)
- [var seedRepresentation: Data](xwingmlkem768x25519/privatekey/seedrepresentation.md)
### Initializers
- [init<D>(bytes: D) throws](xwingmlkem768x25519/privatekey/init(bytes:).md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [HPKEKEMPrivateKey](hpkekemprivatekey.md)
- [HPKEKEMPrivateKeyGeneration](hpkekemprivatekeygeneration.md)
- [KEMPrivateKey](kemprivatekey.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [XWingMLKEM768X25519.PublicKey](xwingmlkem768x25519/publickey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/xwingmlkem768x25519/privatekey)*