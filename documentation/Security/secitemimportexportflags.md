# SecItemImportExportFlags

**Framework**: Security  
**Kind**: struct  
**Role**: Structure

The import and export function flags.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct SecItemImportExportFlags
```

```c
enum SecItemImportExportFlags : uint32_t;
```

## Overview

Use an instance of this structure a the flags input to the [`SecItemImport(_:_:_:_:_:_:_:_:)`](./secitemimport%28_,_,_,_,_,_,_,_%29.md) and [`SecItemExport(_:_:_:_:_:)`](./secitemexport%28_,_,_,_,_%29.md) functions.

## Topics

### Initializers
- [init(rawValue: UInt32)](./secitemimportexportflags/init%28rawvalue%29.md)
  Initialize an item import/export flag structure.
### Constants
- [static var pemArmour: SecItemImportExportFlags](./secitemimportexportflags/pemarmour.md)
  A flag that indicates the exported data should have PEM armor.

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

*[View on Apple Developer](https://developer.apple.com/documentation/security/secitemimportexportflags)*