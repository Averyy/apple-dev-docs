# SecCSFlags

**Framework**: Security  
**Kind**: struct

Values that can be used in the `flags` parameter to most code signing functions.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct SecCSFlags
```

#### Overview

All of the bits in the [`SecCSFlags`](seccsflags.md) enumeration are reserved by Apple. If you set any bits not defined here, the behavior is undefined.

## Topics

### Initializers
- [init(rawValue: UInt32)](seccsflags/init(rawvalue:).md)
### Constants
- [static var considerExpiration: SecCSFlags](seccsflags/considerexpiration.md)
  Consider expired certificates invalid.
- [static var enforceRevocationChecks: SecCSFlags](seccsflags/enforcerevocationchecks.md)
- [static var checkTrustedAnchors: SecCSFlags](seccsflags/checktrustedanchors.md)
- [static var noNetworkAccess: SecCSFlags](seccsflags/nonetworkaccess.md)
- [static var reportProgress: SecCSFlags](seccsflags/reportprogress.md)
- [static var quickCheck: SecCSFlags](seccsflags/quickcheck.md)
### Type Properties
- [static var applyEmbeddedPolicy: SecCSFlags](seccsflags/applyembeddedpolicy.md)
- [static var matchGuestRequirementInKernel: SecCSFlags](seccsflags/matchguestrequirementinkernel.md)
- [static var stripDisallowedXattrs: SecCSFlags](seccsflags/stripdisallowedxattrs.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccsflags)*