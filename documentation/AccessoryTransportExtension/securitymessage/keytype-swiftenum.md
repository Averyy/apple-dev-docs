# SecurityMessage.KeyType

**Framework**: Accessory Transport Extension  
**Kind**: enum

Identifies the type of key carried by a [`SecurityMessage`](securitymessage.md).

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)
- Mac Catalyst 26.5+ (Beta)

## Declaration

```swift
enum KeyType
```

## Topics

### Enumeration Cases
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