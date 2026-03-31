# SecurityMessage.KeyMaterial

**Framework**: Accessory Transport Extension  
**Kind**: struct

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
struct KeyMaterial
```

## Topics

### Instance Properties
- [let ciphersuite: SecurityMessage.CipherSuite](securitymessage/keymaterial/ciphersuite.md)
  HPKE ciphersuite used for key exchange.
- [var encapsulatedKey: Data](securitymessage/keymaterial/encapsulatedkey.md)
  Encapsulated key data.
- [let identifier: String](securitymessage/keymaterial/identifier.md)
  Identifier used to derive HPKE keys.
- [let publicKey: Data](securitymessage/keymaterial/publickey.md)
  Public key data.
- [let version: SecurityMessage.CipherSuite.Version](securitymessage/keymaterial/version.md)
  Ciphersuite protocol version.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/securitymessage/keymaterial)*