---
url: "https://docs.swift.org/latest/documentation/packageplugin/product/targets"
framework: "Swift-Org/PackagePlugin"
---

# targets

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The targets that directly comprise the product, in the order in which they are declared in the package manifest.

## Declaration

```swift
var targets: [Target] { get }
```

## Discussion

The product contains the transitive closure of the these targets and their dependencies. Some kinds of products have further restrictions on the set of targets (for example, an executable product must have one and only one target that defines the main entry point for an executable).

## See Also

### Inspecting a Package Product
- [var id: ID](./id-swift.property.md)
  Unique identifier for the product.
- [var name: String](./name.md)
  The name of the product, as defined in the package manifest.
- [var sourceModules: [SourceModuleTarget]](./sourcemodules.md)
- [typealias ID](./id-swift.typealias.md)
  The type that represents the identifier of a package product.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/product/targets)*