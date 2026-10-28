---
url: "https://docs.swift.org/latest/documentation/packageplugin/package/displayname"
framework: "Swift-Org/PackagePlugin"
---

# displayName

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

The name of the package.

## Declaration

```swift
let displayName: String
```

## Discussion

Use the name for display purposes only.

## See Also

### Inspecting Packages
- [let id: ID](./id-swift.property.md)
  The unique identifier for the package.
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
- [let directory: Path](./directory.md)
  The absolute path of the package directory in the local file system.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/package/displayname)*