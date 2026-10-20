# SecurityMessage.KeyType

**Framework**: Accessory Transport Extension  
**Kind**: enum  
**Role**: Enumeration

A type that identifies the key material a security message carries.

**Availability**:
- iOS 26.5+

## Declaration

```swift
enum KeyType
```

#### Overview

Use this enumeration to specify the type of cryptographic key when creating a [`SecurityMessage`](../securitymessage.md) for the key exchange process. The accessory initiates key exchange by sending a message with [`SecurityMessage.KeyType.publicKey`](./keytype-swift.enum/publickey.md). The system responds with a message containing [`SecurityMessage.KeyType.encapsulatedKey`](./keytype-swift.enum/encapsulatedkey.md), which completes the exchange.

## Topics

### Identifying key types
- [SecurityMessage.KeyType.encapsulatedKey](./keytype-swift.enum/encapsulatedkey.md)
  An encapsulated key, sent from the host to the accessory.
- [SecurityMessage.KeyType.publicKey](./keytype-swift.enum/publickey.md)
  A public key, sent from the accessory to the host.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing key material
- [let key: Data](./key.md)
  The key data carried by this message.
- [let keyType: SecurityMessage.KeyType](./keytype-swift.property.md)
  The type of key carried by this message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/securitymessage/keytype-swift.enum)*