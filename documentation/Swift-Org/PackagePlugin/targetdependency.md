---
url: "https://docs.swift.org/latest/documentation/packageplugin/targetdependency"
framework: "Swift-Org/PackagePlugin"
---

# TargetDependency

**Framework**: Swift-Org/PackagePlugin  
**Kind**: enum  
**Role**: Enumeration

A dependency of a target on a product or on another target.

## Declaration

```swift
enum TargetDependency
```

## Topics

### Target Dependencies
- [TargetDependency.product(_:)](./targetdependency/product%28_%29.md)
  A dependency on a product in another package.
- [TargetDependency.target(_:)](./targetdependency/target%28_%29.md)
  A dependency on a target in the same package.

## See Also

### Inspecting Package Targets
- [protocol Target](./target.md)
  A single target defined in a package.
- [protocol SourceModuleTarget](./sourcemoduletarget.md)
  A target consisting of a source code module.
- [enum ModuleKind](./modulekind.md)
  The kind of module.
- [struct SwiftSourceModuleTarget](./swiftsourcemoduletarget.md)
  A target consisting of a source code module compiled using Swift.
- [struct ClangSourceModuleTarget](./clangsourcemoduletarget.md)
  A target consisting of a source code module compiled using Clang.
- [struct BinaryArtifactTarget](./binaryartifacttarget.md)
  A target describing an artifact that is distributed as a binary.
- [struct SystemLibraryTarget](./systemlibrarytarget.md)
  A target describing a system library that is expected to be present on the host system.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/targetdependency)*