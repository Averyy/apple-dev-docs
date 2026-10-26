---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/buildresult/builtartifact/kind-swift.enum"
framework: "Swift-Org/PackagePlugin"
---

# PackageManager.BuildResult.BuiltArtifact.Kind

**Framework**: Swift-Org/PackagePlugin  
**Kind**: enum  
**Role**: Enumeration

The kind of artifact built.

## Declaration

```swift
enum Kind
```

#### Overview

The specific file formats may vary from platform to platform. For example, on macOS  a dynamic library may in fact be built as a framework.

## Topics

### Enumeration Cases
- [PackageManager.BuildResult.BuiltArtifact.Kind.dynamicLibrary](./kind-swift.enum/dynamiclibrary.md)
- [PackageManager.BuildResult.BuiltArtifact.Kind.executable](./kind-swift.enum/executable.md)
- [PackageManager.BuildResult.BuiltArtifact.Kind.staticLibrary](./kind-swift.enum/staticlibrary.md)
### Initializers
- [init?(rawValue: String)](./kind-swift.enum/init%28rawvalue%29.md)
### Default Implementations
- [Equatable Implementations](./kind-swift.enum/equatable-implementations.md)
- [RawRepresentable Implementations](./kind-swift.enum/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.RawRepresentable

## See Also

### Inspecting a Build Artifact
- [var kind: Kind](./kind-swift.property.md)
  The kind of artifact built.
- [var url: URL](./url.md)
  The file URL of the built artifact in the local file system.
- [var path: Path](./path.md)
  Full path of the built artifact in the local file system.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/buildresult/builtartifact/kind-swift.enum)*