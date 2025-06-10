# CMSCertificateChainMode

**Framework**: Security  
**Kind**: enum

Constants that can be set to specify what certificates to include in a signed message.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum CMSCertificateChainMode
```

#### Overview

Use these with the [`CMSEncoderSetCertificateChainMode(_:_:)`](cmsencodersetcertificatechainmode(_:_:).md) function.

## Topics

### Constants
- [CMSCertificateChainMode.none](cmscertificatechainmode/none.md)
  Don’t include any certificates.
- [CMSCertificateChainMode.signerOnly](cmscertificatechainmode/signeronly.md)
  Only include signer certificates.
- [CMSCertificateChainMode.chain](cmscertificatechainmode/chain.md)
  Include the signer certificate chain up to but not including the root certificate.
- [CMSCertificateChainMode.chainWithRoot](cmscertificatechainmode/chainwithroot.md)
  Include the entire signer certificate chain, including the root certificate.
### Enumeration Cases
- [CMSCertificateChainMode.chainWithRootOrFail](cmscertificatechainmode/chainwithrootorfail.md)
### Initializers
- [init?(rawValue: UInt32)](cmscertificatechainmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmscertificatechainmode)*