---
url: "https://docs.swift.org/latest/documentation/packageplugin/binaryartifacttarget"
framework: "Swift-Org/PackagePlugin"
---

# BinaryArtifactTarget

**Framework**: Swift-Org/PackagePlugin  
**Kind**: struct  
**Role**: Structure

A target describing an artifact that is distributed as a binary.

## Declaration

```swift
struct BinaryArtifactTarget
```

#### Overview

For example, a library or executable.

## Topics

### Inspecting the Target
- [let id: ID](./binaryartifacttarget/id.md)
  Unique identifier for the target.
- [let name: String](./binaryartifacttarget/name.md)
  The name of the target, as defined in the package manifest.
- [let kind: Kind](./binaryartifacttarget/kind-swift.property.md)
  The kind of binary artifact.
- [let origin: Origin](./binaryartifacttarget/origin-swift.property.md)
  The original source of the binary artifact.
- [let artifactURL: URL](./binaryartifacttarget/artifacturl.md)
  The file URL of the location of the binary artifact in the local file system.
- [let dependencies: [TargetDependency]](./binaryartifacttarget/dependencies.md)
  Any other targets on which this target depends, in the same order as specified in the package manifest.
- [let directoryURL: URL](./binaryartifacttarget/directoryurl.md)
  The file URL of the target directory in the local file system.
- [BinaryArtifactTarget.Kind](./binaryartifacttarget/kind-swift.enum.md)
  A kind of binary artifact.
- [BinaryArtifactTarget.Origin](./binaryartifacttarget/origin-swift.enum.md)
  The original location of a binary artifact.
- [let artifact: Path](./binaryartifacttarget/artifact.md)
  The path location of the binary artifact in the local file system.
- [let directory: Path](./binaryartifacttarget/directory.md)
  The absolute path of the target directory in the local file system.
### Default Implementations
- [Target Implementations](./binaryartifacttarget/target-implementations.md)

## Relationships

### Conforms To
- [Target](./target.md)

## See Also

### Inspecting Package Targets
- [protocol Target](./target.md)
  A single target defined in a package.
- [enum TargetDependency](./targetdependency.md)
  A dependency of a target on a product or on another target.
- [protocol SourceModuleTarget](./sourcemoduletarget.md)
  A target consisting of a source code module.
- [enum ModuleKind](./modulekind.md)
  The kind of module.
- [struct SwiftSourceModuleTarget](./swiftsourcemoduletarget.md)
  A target consisting of a source code module compiled using Swift.
- [struct ClangSourceModuleTarget](./clangsourcemoduletarget.md)
  A target consisting of a source code module compiled using Clang.
- [struct SystemLibraryTarget](./systemlibrarytarget.md)
  A target describing a system library that is expected to be present on the host system.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/binaryartifacttarget)*