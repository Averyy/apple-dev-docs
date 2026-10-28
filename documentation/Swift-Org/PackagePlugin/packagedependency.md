---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagedependency"
framework: "Swift-Org/PackagePlugin"
---

# PackageDependency

**Framework**: Swift-Org/PackagePlugin  
**Kind**: struct  
**Role**: Structure

A resolved dependency of a package.

## Declaration

```swift
struct PackageDependency
```

## Overview

This is a separate entity in order to make it easier for future versions of the API to add information about the dependency itself.

## Topics

### Inspecting a Package Dependency
- [let package: Package](./packagedependency/package.md)
  The package that is a dependency.

## See Also

### Inspecting the Package Representation
- [struct Package](./package.md)
  A single package in a graph of packages.
- [struct ToolsVersion](./toolsversion.md)
  A version of Swift package manager on whose semantics a package relies.
- [enum PackageOrigin](./packageorigin.md)
  The origin of a package.
- [protocol Product](./product.md)
  A single product defined in a package.
- [struct ExecutableProduct](./executableproduct.md)
  An executable product defined in a package.
- [struct LibraryProduct](./libraryproduct.md)
  A library product defined in a package.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagedependency)*