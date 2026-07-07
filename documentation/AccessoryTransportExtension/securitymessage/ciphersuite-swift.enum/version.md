# SecurityMessage.CipherSuite.Version

**Framework**: Accessory Transport Extension  
**Kind**: enum

A version of the cipher suite protocol.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
enum Version
```

#### Overview

The version determines the format of the protocol information string that the system uses for HPKE key derivation. Use [`SecurityMessage.CipherSuite.Version.version1`](securitymessage/ciphersuite-swift.enum/version/version1.md) when creating security messages. On your accessory, format the protocol information as `{cipherSuite}-Version1-{identifier}` when deriving HPKE keys.

## Topics

### Identifying protocol versions
- [SecurityMessage.CipherSuite.Version.version1](securitymessage/ciphersuite-swift.enum/version/version1.md)
  Version 1 of the cipher suite protocol.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/securitymessage/ciphersuite-swift.enum/version)*