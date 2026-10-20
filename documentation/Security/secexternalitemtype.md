# SecExternalItemType

**Framework**: Security  
**Kind**: enum  
**Role**: Enumeration

The import item type.

**Availability**:
- macOS 10.0+

## Declaration

```swift
enum SecExternalItemType
```

```c
enum SecExternalItemType : uint32_t;
```

## Topics

### Constants
- [SecExternalItemType.itemTypeUnknown](./secexternalitemtype/itemtypeunknown.md)
  Indicates that the caller does not know the type of information being imported or exported.
- [SecExternalItemType.itemTypePrivateKey](./secexternalitemtype/itemtypeprivatekey.md)
  Indicates a private key.
- [SecExternalItemType.itemTypePublicKey](./secexternalitemtype/itemtypepublickey.md)
  Indicates a public key.
- [SecExternalItemType.itemTypeSessionKey](./secexternalitemtype/itemtypesessionkey.md)
  Indicates a session key.
- [SecExternalItemType.itemTypeCertificate](./secexternalitemtype/itemtypecertificate.md)
  Indicates a certificate.
- [SecExternalItemType.itemTypeAggregate](./secexternalitemtype/itemtypeaggregate.md)
  Indicates a set of certificates or certificates and private keys.
### Initializers
- [init?(rawValue: UInt32)](./secexternalitemtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secexternalitemtype)*