---
url: "https://docs.swift.org/latest/documentation/packageplugin/product"
framework: "Swift-Org/PackagePlugin"
---

# Product

**Framework**: Swift-Org/PackagePlugin  
**Kind**: protocol  
**Role**: Protocol

A single product defined in a package.

## Declaration

```swift
protocol Product
```

## Topics

### Inspecting a Package Product
- [var id: ID](./product/id-swift.property.md)
  Unique identifier for the product.
- [var name: String](./product/name.md)
  The name of the product, as defined in the package manifest.
- [var sourceModules: [SourceModuleTarget]](./product/sourcemodules.md)
- [var targets: [Target]](./product/targets.md)
  The targets that directly comprise the product, in the order in which they are declared in the package manifest.
- [typealias ID](./product/id-swift.typealias.md)
  The type that represents the identifier of a package product.

## Relationships

### Conforming Types
- [ExecutableProduct](./executableproduct.md)
- [LibraryProduct](./libraryproduct.md)

## See Also

### Inspecting the Package Representation
- [struct Package](./package.md)
  A single package in a graph of packages.
- [struct ToolsVersion](./toolsversion.md)
  A version of Swift package manager on whose semantics a package relies.
- [enum PackageOrigin](./packageorigin.md)
  The origin of a package.
- [struct PackageDependency](./packagedependency.md)
  A resolved dependency of a package.
- [struct ExecutableProduct](./executableproduct.md)
  An executable product defined in a package.
- [struct LibraryProduct](./libraryproduct.md)
  A library product defined in a package.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/product)*