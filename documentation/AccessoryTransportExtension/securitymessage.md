# SecurityMessage

**Framework**: Accessory Transport Extension  
**Kind**: struct

A message carrying key material used to negotiate a secure channel between a host and an accessory.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)

## Declaration

```swift
struct SecurityMessage
```

## Topics

### Initializers
- [init(keyType: SecurityMessage.KeyType, cipherSuite: SecurityMessage.CipherSuite, version: SecurityMessage.CipherSuite.Version, key: Data, supportedTransports: [AccessoryTransport], identifier: String?)](securitymessage/init(keytype:ciphersuite:version:key:supportedtransports:identifier:).md)
  Creates a security message.
### Instance Properties
- [let cipherSuite: SecurityMessage.CipherSuite](securitymessage/ciphersuite-swift.property.md)
  The cipher suite used for key exchange.
- [let identifier: String?](securitymessage/identifier.md)
  An identifier used to derive HPKE keys.
- [let key: Data](securitymessage/key.md)
  The key data carried by this message.
- [let keyType: SecurityMessage.KeyType](securitymessage/keytype-swift.property.md)
  The type of key carried by this message.
- [let supportedTransports: [AccessoryTransport]](securitymessage/supportedtransports.md)
  The supported transports to send sensitive information. Default is `Bluetooth`.
- [let version: SecurityMessage.CipherSuite.Version](securitymessage/version.md)
  The cipher suite version.
### Enumerations
- [SecurityMessage.CipherSuite](securitymessage/ciphersuite-swift.enum.md)
  A cryptographic cipher suite used during key exchange.
- [SecurityMessage.KeyType](securitymessage/keytype-swift.enum.md)
  Identifies the type of key carried by a [`SecurityMessage`](securitymessage.md).

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/securitymessage)*