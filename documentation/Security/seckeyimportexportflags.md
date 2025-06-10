# SecKeyImportExportFlags

**Framework**: Security  
**Kind**: struct

The import/export parameter structure flags.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct SecKeyImportExportFlags
```

#### Overview

Use an instance of this structure to set the [`flags`](secitemimportexportkeyparameters/flags.md) property in the [`SecItemImportExportKeyParameters`](secitemimportexportkeyparameters.md) import/export structure.

## Topics

### Initializers
- [init(rawValue: UInt32)](seckeyimportexportflags/init(rawvalue:).md)
  Initialize a key import/export flag structure.
### Constants
- [static var importOnlyOne: SecKeyImportExportFlags](seckeyimportexportflags/importonlyone.md)
  A flag that you set to prevent importing more than one private key.
- [static var securePassphrase: SecKeyImportExportFlags](seckeyimportexportflags/securepassphrase.md)
  A flag that indicates the user should be prompted for a passphrase on import or export.
- [static var noAccessControl: SecKeyImportExportFlags](seckeyimportexportflags/noaccesscontrol.md)
  A flag that indicates imported private keys have no access object attached to them.

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

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeyimportexportflags)*