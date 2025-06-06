# SecTrustOptionFlags

**Framework**: Security  
**Kind**: struct

The option flags used to condition a trust evaluation.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct SecTrustOptionFlags
```

#### Overview

Use these flags in calls to the [`SecTrustSetOptions(_:_:)`](sectrustsetoptions(_:_:).md) function.

## Topics

### Initializers
- [init(rawValue: UInt32)](sectrustoptionflags/init(rawvalue:).md)
  Initializes a trust option flags structure.
### Flags
- [static var allowExpired: SecTrustOptionFlags](sectrustoptionflags/allowexpired.md)
  Allow expired certificates (except for the root certificate).
- [static var leafIsCA: SecTrustOptionFlags](sectrustoptionflags/leafisca.md)
  Allow CA certificates as leaf certificates.
- [static var fetchIssuerFromNet: SecTrustOptionFlags](sectrustoptionflags/fetchissuerfromnet.md)
  Allow network downloads of CA certificates.
- [static var allowExpiredRoot: SecTrustOptionFlags](sectrustoptionflags/allowexpiredroot.md)
  Allow expired root certificates.
- [static var requireRevPerCert: SecTrustOptionFlags](sectrustoptionflags/requirerevpercert.md)
  Require a positive revocation check for each certificate.
- [static var useTrustSettings: SecTrustOptionFlags](sectrustoptionflags/usetrustsettings.md)
  Use TrustSettings instead of anchors.
- [static var implicitAnchors: SecTrustOptionFlags](sectrustoptionflags/implicitanchors.md)
  Treat properly self-signed certificates as anchors implicitly.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustoptionflags)*