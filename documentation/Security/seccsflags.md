# SecCSFlags

**Framework**: Security  
**Kind**: struct  
**Role**: Structure

Values that can be used in the `flags` parameter to most code signing functions.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct SecCSFlags
```

```c
enum SecCSFlags : uint32_t;
```

#### Overview

All of the bits in the [`SecCSFlags`](./seccsflags.md) enumeration are reserved by Apple. If you set any bits not defined here, the behavior is undefined.

## Topics

### Initializers
- [init(rawValue: UInt32)](./seccsflags/init%28rawvalue%29.md)
### Constants
- [static var considerExpiration: SecCSFlags](./seccsflags/considerexpiration.md)
  Consider expired certificates invalid.
- [static var enforceRevocationChecks: SecCSFlags](./seccsflags/enforcerevocationchecks.md)
- [static var checkTrustedAnchors: SecCSFlags](./seccsflags/checktrustedanchors.md)
- [static var noNetworkAccess: SecCSFlags](./seccsflags/nonetworkaccess.md)
- [static var reportProgress: SecCSFlags](./seccsflags/reportprogress.md)
- [static var quickCheck: SecCSFlags](./seccsflags/quickcheck.md)
- [kSecCSDefaultFlags](./seccsflags/kseccsdefaultflags.md)
  No flags (use the default behavior).
### Type Properties
- [static var applyEmbeddedPolicy: SecCSFlags](./seccsflags/applyembeddedpolicy.md)
- [static var matchGuestRequirementInKernel: SecCSFlags](./seccsflags/matchguestrequirementinkernel.md)
- [static var stripDisallowedXattrs: SecCSFlags](./seccsflags/stripdisallowedxattrs.md)
- [static var useClassicalSignature: SecCSFlags](./seccsflags/useclassicalsignature.md)
- [static var usePostQuantumSignature: SecCSFlags](./seccsflags/usepostquantumsignature.md)
### Enumeration Cases
- [kSecCSUseSignature1](./seccsflags/kseccsusesignature1.md)
- [kSecCSUseSignature2](./seccsflags/kseccsusesignature2.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccsflags)*