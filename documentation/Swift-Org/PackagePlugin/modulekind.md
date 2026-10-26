---
url: "https://docs.swift.org/latest/documentation/packageplugin/modulekind"
framework: "Swift-Org/PackagePlugin"
---

# ModuleKind

**Framework**: Swift-Org/PackagePlugin  
**Kind**: enum  
**Role**: Enumeration

The kind of module.

## Declaration

```swift
enum ModuleKind
```

## Topics

### Kinds of Modules
- [ModuleKind.executable](./modulekind/executable.md)
  A module that contains code for an executable’s main module.
- [ModuleKind.test](./modulekind/test.md)
  A module that contains unit tests.
- [ModuleKind.generic](./modulekind/generic.md)
  A module that contains generic code (not a test nor an executable).
- [ModuleKind.macro](./modulekind/macro.md)
  A module that contains code for a macro.
- [ModuleKind.snippet](./modulekind/snippet.md)
  A module that contains code for a snippet.
### Default Implementations
- [Equatable Implementations](./modulekind/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable

## See Also

### Inspecting Package Targets
- [protocol Target](./target.md)
  A single target defined in a package.
- [enum TargetDependency](./targetdependency.md)
  A dependency of a target on a product or on another target.
- [protocol SourceModuleTarget](./sourcemoduletarget.md)
  A target consisting of a source code module.
- [struct SwiftSourceModuleTarget](./swiftsourcemoduletarget.md)
  A target consisting of a source code module compiled using Swift.
- [struct ClangSourceModuleTarget](./clangsourcemoduletarget.md)
  A target consisting of a source code module compiled using Clang.
- [struct BinaryArtifactTarget](./binaryartifacttarget.md)
  A target describing an artifact that is distributed as a binary.
- [struct SystemLibraryTarget](./systemlibrarytarget.md)
  A target describing a system library that is expected to be present on the host system.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/modulekind)*