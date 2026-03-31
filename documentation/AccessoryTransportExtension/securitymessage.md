# SecurityMessage

**Framework**: Accessory Transport Extension  
**Kind**: enum

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
enum SecurityMessage
```

## Topics

### Structures
- [SecurityMessage.KeyMaterial](securitymessage/keymaterial.md)
### Enumeration Cases
- [SecurityMessage.encapsulatedKey(_:)](securitymessage/encapsulatedkey(_:).md)
  [Step 4] Accessory -> Host: encapsulated key reply after receiving host public and encapsulated key.
- [case keyExchange(keyMaterial: SecurityMessage.KeyMaterial)](securitymessage/keyexchange(keymaterial:).md)
  [Step 3] Host -> Extension: after receiving accessory ciphersuite and public key from extension.
- [case keyReply(ciphersuite: SecurityMessage.CipherSuite, publicKey: Data)](securitymessage/keyreply(ciphersuite:publickey:).md)
  [Step 2] Extension -> Host: reply to `keyRequest` event.
- [SecurityMessage.keyRequest](securitymessage/keyrequest.md)
  [Step 1] Host -> Extension: initiates key exchange with accessory.
### Enumerations
- [SecurityMessage.CipherSuite](securitymessage/ciphersuite.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/securitymessage)*