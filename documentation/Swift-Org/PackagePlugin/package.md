---
url: "https://docs.swift.org/latest/documentation/packageplugin/package"
framework: "Swift-Org/PackagePlugin"
---

# Package

**Framework**: Swift-Org/PackagePlugin  
**Kind**: struct  
**Role**: Structure

A single package in a graph of packages.

## Declaration

```swift
struct Package
```

## Overview

The package can either be the root package, or a dependency.

## Topics

### Inspecting Packages
- [let id: ID](./package/id-swift.property.md)
  The unique identifier for the package.
- [let displayName: String](./package/displayname.md)
  The name of the package.
- [let toolsVersion: ToolsVersion](./package/toolsversion.md)
  The tools version specified by the resolved version of the package.
- [let directoryURL: URL](./package/directoryurl.md)
  The file URL of the package directory in the local file system.
- [let origin: PackageOrigin](./package/origin.md)
  The origin of the package.
- [let dependencies: [PackageDependency]](./package/dependencies.md)
  Any dependencies on other packages.
- [var sourceModules: [SourceModuleTarget]](./package/sourcemodules.md)
- [typealias ID](./package/id-swift.typealias.md)
  The type that represents a package identifier.
- [let directory: Path](./package/directory.md)
  The absolute path of the package directory in the local file system.
### Inspecting Package Targets
- [let targets: [Target]](./package/targets.md)
  Any regular targets defined in this packagewith the exception of plugin targets.
- [func targets(named: [String]) throws -> [Target]](./package/targets%28named%29.md)
  The list of targets matching the given names.
- [func targets<T>(ofType: T.Type) -> [T]](./package/targets%28oftype%29.md)
  The targets in this package that conform to a specific type.
### Inspecting Package Products
- [let products: [Product]](./package/products.md)
  Any regular products defined in this package, with the exception of plugin products.
- [func products(named: [String]) throws -> [Product]](./package/products%28named%29.md)
  The list of products matching the given names.
- [func products<T>(ofType: T.Type) -> [T]](./package/products%28oftype%29.md)
  The products in this package that conform to a specific type.

## See Also

### Inspecting the Package Representation
- [struct ToolsVersion](./toolsversion.md)
  A version of Swift package manager on whose semantics a package relies.
- [enum PackageOrigin](./packageorigin.md)
  The origin of a package.
- [struct PackageDependency](./packagedependency.md)
  A resolved dependency of a package.
- [protocol Product](./product.md)
  A single product defined in a package.
- [struct ExecutableProduct](./executableproduct.md)
  An executable product defined in a package.
- [struct LibraryProduct](./libraryproduct.md)
  A library product defined in a package.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/package)*