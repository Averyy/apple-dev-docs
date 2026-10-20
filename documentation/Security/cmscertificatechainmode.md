# CMSCertificateChainMode

**Framework**: Security  
**Kind**: enum  
**Role**: Enumeration

Constants that can be set to specify what certificates to include in a signed message.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum CMSCertificateChainMode
```

```c
enum CMSCertificateChainMode : uint32_t;
```

#### Overview

Use these with the [`CMSEncoderSetCertificateChainMode(_:_:)`](./cmsencodersetcertificatechainmode%28_,_%29.md) function.

## Topics

### Constants
- [CMSCertificateChainMode.none](./cmscertificatechainmode/none.md)
  Don’t include any certificates.
- [CMSCertificateChainMode.signerOnly](./cmscertificatechainmode/signeronly.md)
  Only include signer certificates.
- [CMSCertificateChainMode.chain](./cmscertificatechainmode/chain.md)
  Include the signer certificate chain up to but not including the root certificate.
- [CMSCertificateChainMode.chainWithRoot](./cmscertificatechainmode/chainwithroot.md)
  Include the entire signer certificate chain, including the root certificate.
### Enumeration Cases
- [CMSCertificateChainMode.chainWithRootOrFail](./cmscertificatechainmode/chainwithrootorfail.md)
### Initializers
- [init?(rawValue: UInt32)](./cmscertificatechainmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cmscertificatechainmode)*