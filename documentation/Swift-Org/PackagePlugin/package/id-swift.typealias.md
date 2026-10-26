---
url: "https://docs.swift.org/latest/documentation/packageplugin/package/id-swift.typealias"
framework: "Swift-Org/PackagePlugin"
---

# Package.ID

**Framework**: Swift-Org/PackagePlugin  
**Kind**: typealias  
**Role**: Type Alias

The type that represents a package identifier.

## Declaration

```swift
typealias ID = String
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
- [let directory: Path](./directory.md)
  The absolute path of the package directory in the local file system.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/package/id-swift.typealias)*