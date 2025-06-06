# SecItemImportExportFlags

**Framework**: Security  
**Kind**: struct

The import and export function flags.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct SecItemImportExportFlags
```

#### Overview

Use an instance of this structure a the flags input to the [`SecItemImport(_:_:_:_:_:_:_:_:)`](secitemimport(_:_:_:_:_:_:_:_:).md) and [`SecItemExport(_:_:_:_:_:)`](secitemexport(_:_:_:_:_:).md) functions.

## Topics

### Initializers
- [init(rawValue: UInt32)](secitemimportexportflags/init(rawvalue:).md)
  Initialize an item import/export flag structure.
### Constants
- [static var pemArmour: SecItemImportExportFlags](secitemimportexportflags/pemarmour.md)
  A flag that indicates the exported data should have PEM armor.

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

*[View on Apple Developer](https://developer.apple.com/documentation/security/secitemimportexportflags)*