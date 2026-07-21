# SecurityMessage.KeyType

**Framework**: Accessory Transport Extension  
**Kind**: enum

A type that identifies the key material a security message carries.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
enum KeyType
```

#### Overview

Use this enumeration to specify the type of cryptographic key when creating a [`SecurityMessage`](securitymessage.md) for the key exchange process. The accessory initiates key exchange by sending a message with [`SecurityMessage.KeyType.publicKey`](securitymessage/keytype-swift.enum/publickey.md). The system responds with a message containing [`SecurityMessage.KeyType.encapsulatedKey`](securitymessage/keytype-swift.enum/encapsulatedkey.md), which completes the exchange.

## Topics

### Identifying key types
- [SecurityMessage.KeyType.encapsulatedKey](securitymessage/keytype-swift.enum/encapsulatedkey.md)
  An encapsulated key, sent from the host to the accessory.
- [SecurityMessage.KeyType.publicKey](securitymessage/keytype-swift.enum/publickey.md)
  A public key, sent from the accessory to the host.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let key: Data](securitymessage/key.md)
  The key data carried by this message.
- [let keyType: SecurityMessage.KeyType](securitymessage/keytype-swift.property.md)
  The type of key carried by this message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/securitymessage/keytype-swift.enum)*