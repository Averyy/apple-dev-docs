# SecCodeSignatureFlags

**Framework**: Security  
**Kind**: struct

Specify option flags that can be embedded in a code signature during signing and that govern the use of the signature.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct SecCodeSignatureFlags
```

#### Overview

Some of these flags can be set through the `codesign(1)` command’s `--options` argument and some are set implicitly based on signing circumstances. The flags here appear as the value associated with the [`kSecCodeInfoFlags`](kseccodeinfoflags.md) key in the signing information dictionary. See [`Signing Information Dictionary Keys`](signing-information-dictionary-keys.md).

## Topics

### Initializers
- [init(rawValue: UInt32)](seccodesignatureflags/init(rawvalue:).md)
### Constants
- [static var host: SecCodeSignatureFlags](seccodesignatureflags/host.md)
  May host guest code.
- [static var adhoc: SecCodeSignatureFlags](seccodesignatureflags/adhoc.md)
  Must be used without a signing identity.
- [static var forceHard: SecCodeSignatureFlags](seccodesignatureflags/forcehard.md)
  Always set the [`hard`](seccodestatus/hard.md) status flag on launch.
- [static var forceKill: SecCodeSignatureFlags](seccodesignatureflags/forcekill.md)
  Always set the termination status flag on launch.
- [static var forceExpiration: SecCodeSignatureFlags](seccodesignatureflags/forceexpiration.md)
  Always set the [`considerExpiration`](seccsflags/considerexpiration.md) flag when validating the code.
- [static var enforcement: SecCodeSignatureFlags](seccodesignatureflags/enforcement.md)
  Enforce code signing.
- [static var libraryValidation: SecCodeSignatureFlags](seccodesignatureflags/libraryvalidation.md)
  Require library validation.
- [static var restrict: SecCodeSignatureFlags](seccodesignatureflags/restrict.md)
  Restrict dyld loading.
- [static var runtime: SecCodeSignatureFlags](seccodesignatureflags/runtime.md)
  Apply runtime hardening policies as required by the hardened runtime version.
### Type Properties
- [static var linkerSigned: SecCodeSignatureFlags](seccodesignatureflags/linkersigned.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccodesignatureflags)*