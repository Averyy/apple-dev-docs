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
- [static var useClassicalSignature: SecCSFlags](seccsflags/useclassicalsignature.md)
- [static var usePostQuantumSignature: SecCSFlags](seccsflags/usepostquantumsignature.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccsflags)*