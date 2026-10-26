---
url: "https://docs.swift.org/latest/documentation/packageplugin/libraryproduct/name"
framework: "Swift-Org/PackagePlugin"
---

# name

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

The name of the product, as defined in the package manifest.

## Declaration

```swift
let name: String
```

#### Discussion

This name is unique among the products of the package in which it is defined.

## See Also

### Inspecting a Library Product
- [let id: ID](./id.md)
  Unique identifier for the product.
- [let kind: Kind](./kind-swift.property.md)
  A value that indicates whether the library is static, dynamic, or automatically determined.
- [let targets: [Target]](./targets.md)
  The targets that directly comprise the product, in the order in which they are declared in the package manifest.
- [LibraryProduct.Kind](./kind-swift.enum.md)
  The kind of library product.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/libraryproduct/name)*