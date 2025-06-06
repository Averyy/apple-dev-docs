# MTROperationalCSRInfo

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
class MTROperationalCSRInfo
```

## Topics

### Initializers
- [init(csr: Data, csrNonce: Data, csrElementsTLV: Data, attestationSignature: Data)](mtroperationalcsrinfo/init(csr:csrnonce:csrelementstlv:attestationsignature:).md)
- [init?(csrElementsTLV: Data, attestationSignature: Data)](mtroperationalcsrinfo/init(csrelementstlv:attestationsignature:).md)
- [init?(csrNonce: Data, csrElementsTLV: Data, attestationSignature: Data)](mtroperationalcsrinfo/init(csrnonce:csrelementstlv:attestationsignature:).md)
- [init?(csrResponseParams: MTROperationalCredentialsClusterCSRResponseParams)](mtroperationalcsrinfo/init(csrresponseparams:).md)
### Instance Properties
- [var attestationSignature: Data](mtroperationalcsrinfo/attestationsignature.md)
- [var csr: Data](mtroperationalcsrinfo/csr.md)
- [var csrElementsTLV: Data](mtroperationalcsrinfo/csrelementstlv.md)
- [var csrNonce: Data](mtroperationalcsrinfo/csrnonce.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtroperationalcsrinfo)*