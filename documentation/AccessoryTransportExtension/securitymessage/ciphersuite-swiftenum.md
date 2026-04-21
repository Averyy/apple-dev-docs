# SecurityMessage.CipherSuite

**Framework**: Accessory Transport Extension  
**Kind**: enum

A cryptographic cipher suite used during key exchange.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)
- Mac Catalyst 26.5+ (Beta)

## Declaration

```swift
enum CipherSuite
```

## Topics

### Enumeration Cases
- [SecurityMessage.CipherSuite.p256](securitymessage/ciphersuite-swift.enum/p256.md)
  A cipher suite using NIST P-256 elliptic curve cryptography.
- [SecurityMessage.CipherSuite.xWing](securitymessage/ciphersuite-swift.enum/xwing.md)
  A cipher suite providing XWing hybrid post-quantum key encapsulation.
### Enumerations
- [SecurityMessage.CipherSuite.Version](securitymessage/ciphersuite-swift.enum/version.md)
  Version of cipher suite used.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let cipherSuite: SecurityMessage.CipherSuite](securitymessage/ciphersuite-swift.property.md)
  The cipher suite used for key exchange.
- [let version: SecurityMessage.CipherSuite.Version](securitymessage/version.md)
  The cipher suite version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/securitymessage/ciphersuite-swift.enum)*