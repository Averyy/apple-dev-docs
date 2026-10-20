# MTROperationalCSRInfo

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
class MTROperationalCSRInfo
```

```objc
@interface MTROperationalCSRInfo : NSObject
```

## Topics

### Initializers
- [init(csr: Data, csrNonce: Data, csrElementsTLV: Data, attestationSignature: Data)](./mtroperationalcsrinfo/init%28csr,csrnonce,csrelementstlv,attestationsignature%29-69823.md)
- [init?(csrElementsTLV: Data, attestationSignature: Data)](./mtroperationalcsrinfo/init%28csrelementstlv,attestationsignature%29-pboh.md)
- [init?(csrNonce: Data, csrElementsTLV: Data, attestationSignature: Data)](./mtroperationalcsrinfo/init%28csrnonce,csrelementstlv,attestationsignature%29-82w0o.md)
- [init?(csrResponseParams: MTROperationalCredentialsClusterCSRResponseParams)](./mtroperationalcsrinfo/init%28csrresponseparams%29-86yeg.md)
- [init(CSR: Data, csrNonce: Data, csrElementsTLV: Data, attestationSignature: Data)](./mtroperationalcsrinfo/init%28csr,csrnonce,csrelementstlv,attestationsignature%29-2l26j.md)
- [init?(CSRElementsTLV: Data, attestationSignature: Data)](./mtroperationalcsrinfo/init%28csrelementstlv,attestationsignature%29-73sbs.md)
- [init?(CSRNonce: Data, csrElementsTLV: Data, attestationSignature: Data)](./mtroperationalcsrinfo/init%28csrnonce,csrelementstlv,attestationsignature%29-7tep6.md)
- [init?(CSRResponseParams: MTROperationalCredentialsClusterCSRResponseParams)](./mtroperationalcsrinfo/init%28csrresponseparams%29-3o8qo.md)
### Instance Properties
- [var attestationSignature: Data](./mtroperationalcsrinfo/attestationsignature.md)
- [var csr: Data](./mtroperationalcsrinfo/csr.md)
- [var csrElementsTLV: Data](./mtroperationalcsrinfo/csrelementstlv.md)
- [var csrNonce: Data](./mtroperationalcsrinfo/csrnonce.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtroperationalcsrinfo)*