---
url: "https://docs.swift.org/latest/documentation/packageplugin/executableproduct"
framework: "Swift-Org/PackagePlugin"
---

# ExecutableProduct

**Framework**: Swift-Org/PackagePlugin  
**Kind**: struct  
**Role**: Structure

An executable product defined in a package.

## Declaration

```swift
struct ExecutableProduct
```

## Topics

### Inspecting an Executable Target
- [let id: ID](./executableproduct/id.md)
  Unique identifier for the product.
- [let name: String](./executableproduct/name.md)
  The name of the product, as defined in the package manifest.
- [let mainTarget: Target](./executableproduct/maintarget.md)
  The target that contains the main entry point of the executable.
- [let targets: [Target]](./executableproduct/targets.md)
  The targets that directly comprise the product, in the order in which they are declared in the package manifest.
### Default Implementations
- [Product Implementations](./executableproduct/product-implementations.md)

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
- [struct LibraryProduct](./libraryproduct.md)
  A library product defined in a package.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/executableproduct)*