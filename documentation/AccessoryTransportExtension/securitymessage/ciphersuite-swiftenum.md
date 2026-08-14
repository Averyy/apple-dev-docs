# SecurityMessage.CipherSuite

**Framework**: Accessory Transport Extension  
**Kind**: enum

A cryptographic cipher suite for key exchange.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
enum CipherSuite
```

#### Overview

Choose a cipher suite based on your accessory’s capabilities and the transport methods it supports. Use [`SecurityMessage.CipherSuite.xWing`](securitymessage/ciphersuite-swift.enum/xwing.md) for post-quantum security, which is required for [`AccessoryTransport.internet`](accessorytransport/internet.md) and [`AccessoryTransport.localNetwork`](accessorytransport/localnetwork.md) transports. Use [`SecurityMessage.CipherSuite.p256`](securitymessage/ciphersuite-swift.enum/p256.md) as a fallback option for Bluetooth-only accessories that don’t support xWing.

## Topics

### Identifying cipher suite types
- [SecurityMessage.CipherSuite.p256](securitymessage/ciphersuite-swift.enum/p256.md)
  A cipher suite that uses NIST P-256 elliptic curve cryptography.
- [SecurityMessage.CipherSuite.xWing](securitymessage/ciphersuite-swift.enum/xwing.md)
  A cipher suite that provides xWing hybrid post-quantum key encapsulation.
### Determining protocol versions
- [SecurityMessage.CipherSuite.Version](securitymessage/ciphersuite-swift.enum/version.md)
  A version of the cipher suite protocol.

## Relationships

### Conforms To
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let cipherSuite: SecurityMessage.CipherSuite](securitymessage/ciphersuite-swift.property.md)
  The cipher suite used for key exchange.
- [let version: SecurityMessage.CipherSuite.Version](securitymessage/version.md)
  The cipher suite version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/securitymessage/ciphersuite-swift.enum)*