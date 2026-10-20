# MTRCertificateInfo

**Framework**: Matter  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
class MTRCertificateInfo
```

```objc
@interface MTRCertificateInfo : NSObject
```

## Topics

### Initializers
- [init?(tlvBytes: Data)](./mtrcertificateinfo/init%28tlvbytes%29-56yg9.md)
- [init?(TLVBytes: Data)](./mtrcertificateinfo/init%28tlvbytes%29-9fmvz.md)
### Instance Properties
- [var issuer: MTRDistinguishedNameInfo](./mtrcertificateinfo/issuer.md)
- [var notAfter: Date](./mtrcertificateinfo/notafter.md)
- [var notBefore: Date](./mtrcertificateinfo/notbefore.md)
- [var subject: MTRDistinguishedNameInfo](./mtrcertificateinfo/subject.md)
- [var publicKeyData: Data?](./mtrcertificateinfo/publickeydata.md)
  Public key data for this certificate

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcertificateinfo)*