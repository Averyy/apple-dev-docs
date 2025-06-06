# MTRCertificateInfo

**Framework**: Matter  
**Kind**: class

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

## Topics

### Initializers
- [init?(tlvBytes: Data)](mtrcertificateinfo/init(tlvbytes:).md)
### Instance Properties
- [var issuer: MTRDistinguishedNameInfo](mtrcertificateinfo/issuer.md)
- [var notAfter: Date](mtrcertificateinfo/notafter.md)
- [var notBefore: Date](mtrcertificateinfo/notbefore.md)
- [var subject: MTRDistinguishedNameInfo](mtrcertificateinfo/subject.md)
- [var publicKeyData: Data?](mtrcertificateinfo/publickeydata.md)
  Public key data for this certificate

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrcertificateinfo)*