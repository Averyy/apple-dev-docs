---
url: "https://docs.swift.org/latest/documentation/packageplugin/product/name"
framework: "Swift-Org/PackagePlugin"
---

# name

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The name of the product, as defined in the package manifest.

## Declaration

```swift
var name: String { get }
```

## Discussion

This name is unique among the products of the package in which it is defined.

## See Also

### Inspecting a Package Product
- [var id: ID](./id-swift.property.md)
  Unique identifier for the product.
- [var sourceModules: [SourceModuleTarget]](./sourcemodules.md)
- [var targets: [Target]](./targets.md)
  The targets that directly comprise the product, in the order in which they are declared in the package manifest.
- [typealias ID](./id-swift.typealias.md)
  The type that represents the identifier of a package product.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/product/name)*