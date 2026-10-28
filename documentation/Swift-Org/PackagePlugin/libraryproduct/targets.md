---
url: "https://docs.swift.org/latest/documentation/packageplugin/libraryproduct/targets"
framework: "Swift-Org/PackagePlugin"
---

# targets

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

The targets that directly comprise the product, in the order in which they are declared in the package manifest.

## Declaration

```swift
let targets: [Target]
```

## Discussion

The product contains the transitive closure of the these targets and their dependencies.

## See Also

### Inspecting a Library Product
- [let id: ID](./id.md)
  Unique identifier for the product.
- [let name: String](./name.md)
  The name of the product, as defined in the package manifest.
- [let kind: Kind](./kind-swift.property.md)
  A value that indicates whether the library is static, dynamic, or automatically determined.
- [LibraryProduct.Kind](./kind-swift.enum.md)
  The kind of library product.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/libraryproduct/targets)*