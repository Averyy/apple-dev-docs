---
url: "https://docs.swift.org/latest/documentation/packageplugin/package/toolsversion"
framework: "Swift-Org/PackagePlugin"
---

# toolsVersion

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

The tools version specified by the resolved version of the package.

## Declaration

```swift
let toolsVersion: ToolsVersion
```

## Discussion

Behavior is often gated on the tools version to make sure older packages continue to work as intended.

## See Also

### Inspecting Packages
- [let id: ID](./id-swift.property.md)
  The unique identifier for the package.
- [let displayName: String](./displayname.md)
  The name of the package.
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/package/toolsversion)*