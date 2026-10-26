---
url: "https://docs.swift.org/latest/documentation/packageplugin/package/directory"
framework: "Swift-Org/PackagePlugin"
---

# directory

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

The absolute path of the package directory in the local file system.

**Availability**:
- SwiftPM - Deprecated in 6.0 (renamed: directoryURL)

## Declaration

```swift
let directory: Path
```

## See Also

### Inspecting Packages
- [let id: ID](./id-swift.property.md)
  The unique identifier for the package.
- [let displayName: String](./displayname.md)
  The name of the package.
- [let toolsVersion: ToolsVersion](./toolsversion.md)
  The tools version specified by the resolved version of the package.
- [let directoryURL: URL](./directoryurl.md)
  The file URL of the package directory in the local file system.
- [let origin: PackageOrigin](./origin.md)
  The origin of the package.
- [let dependencies: [PackageDependency]](./dependencies.md)
  Any dependencies on other packages.
- [var sourceModules: [SourceModuleTarget]](./sourcemodules.md)
- [typealias ID](./id-swift.typealias.md)
  The type that represents a package identifier.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/package/directory)*