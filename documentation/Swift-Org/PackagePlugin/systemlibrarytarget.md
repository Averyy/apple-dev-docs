---
url: "https://docs.swift.org/latest/documentation/packageplugin/systemlibrarytarget"
framework: "Swift-Org/PackagePlugin"
---

# SystemLibraryTarget

**Framework**: Swift-Org/PackagePlugin  
**Kind**: struct  
**Role**: Structure

A target describing a system library that is expected to be present on the host system.

## Declaration

```swift
struct SystemLibraryTarget
```

## Topics

### Inspecting the System Library Target
- [let id: ID](./systemlibrarytarget/id.md)
  Unique identifier for the target.
- [var name: String](./systemlibrarytarget/name.md)
  The name of the target, as defined in the package manifest.
- [let pkgConfig: String?](./systemlibrarytarget/pkgconfig.md)
  The name of the `pkg-config` file, if any, describing the library.
- [var dependencies: [TargetDependency]](./systemlibrarytarget/dependencies.md)
  Any other targets on which this target depends, in the same order as specified in the package manifest.
- [let compilerFlags: [String]](./systemlibrarytarget/compilerflags.md)
  Flags from `pkg-config` to pass to Clang and SwiftC.
- [let linkerFlags: [String]](./systemlibrarytarget/linkerflags.md)
  Flags from `pkg-config` to pass to the platform linker.
- [var directoryURL: URL](./systemlibrarytarget/directoryurl.md)
  The file URL of the target directory in the local file system.
- [var directory: Path](./systemlibrarytarget/directory.md)
  The absolute path of the target directory in the local file system.
### Default Implementations
- [Target Implementations](./systemlibrarytarget/target-implementations.md)

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
- [struct BinaryArtifactTarget](./binaryartifacttarget.md)
  A target describing an artifact that is distributed as a binary.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/systemlibrarytarget)*