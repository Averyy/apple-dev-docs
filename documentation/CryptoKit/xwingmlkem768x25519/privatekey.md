# XWingMLKEM768X25519.PrivateKey

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
struct PrivateKey
```

## Topics

### Creating a private key
- [init<D>(integrityCheckedRepresentation: D) throws](./privatekey/init%28integritycheckedrepresentation%29.md)
- [init<D>(seedRepresentation: D, publicKey: XWingMLKEM768X25519.PublicKey?) throws](./privatekey/init%28seedrepresentation,publickey%29.md)
### Inspecting a private key’s properties
- [var integrityCheckedRepresentation: Data](./privatekey/integritycheckedrepresentation.md)
- [var seedRepresentation: Data](./privatekey/seedrepresentation.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Escapable](../../Swift/escapable.md)
- [HPKEKEMPrivateKey](../hpkekemprivatekey.md)
- [HPKEKEMPrivateKeyGeneration](../hpkekemprivatekeygeneration.md)
- [KEMPrivateKey](../kemprivatekey.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Keys
- [XWingMLKEM768X25519.PublicKey](./publickey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/xwingmlkem768x25519/privatekey)*