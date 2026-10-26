---
url: "https://docs.swift.org/latest/documentation/packageplugin/libraryproduct"
framework: "Swift-Org/PackagePlugin"
---

# LibraryProduct

**Framework**: Swift-Org/PackagePlugin  
**Kind**: struct  
**Role**: Structure

A library product defined in a package.

## Declaration

```swift
struct LibraryProduct
```

## Topics

### Inspecting a Library Product
- [let id: ID](./libraryproduct/id.md)
  Unique identifier for the product.
- [let name: String](./libraryproduct/name.md)
  The name of the product, as defined in the package manifest.
- [let kind: Kind](./libraryproduct/kind-swift.property.md)
  A value that indicates whether the library is static, dynamic, or automatically determined.
- [let targets: [Target]](./libraryproduct/targets.md)
  The targets that directly comprise the product, in the order in which they are declared in the package manifest.
- [LibraryProduct.Kind](./libraryproduct/kind-swift.enum.md)
  The kind of library product.
### Default Implementations
- [Product Implementations](./libraryproduct/product-implementations.md)

## Relationships

### Conforms To
- [Product](./product.md)

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
- [protocol Product](./product.md)
  A single product defined in a package.
- [struct ExecutableProduct](./executableproduct.md)
  An executable product defined in a package.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/libraryproduct)*