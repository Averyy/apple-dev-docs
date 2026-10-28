# SecurityMessage.CipherSuite.Version

**Framework**: Accessory Transport Extension  
**Kind**: enum  
**Role**: Enumeration

A version of the cipher suite protocol.

**Availability**:
- iOS 26.5+

## Declaration

```swift
enum Version
```

## Overview

The version determines the format of the protocol information string that the system uses for HPKE key derivation. Use [`SecurityMessage.CipherSuite.Version.version1`](./version/version1.md) when creating security messages. On your accessory, format the protocol information as `{cipherSuite}-Version1-{identifier}` when deriving HPKE keys.

## Topics

### Identifying protocol versions
- [SecurityMessage.CipherSuite.Version.version1](./version/version1.md)
  Version 1 of the cipher suite protocol.

## Relationships

### Conforms To
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/securitymessage/ciphersuite-swift.enum/version)*