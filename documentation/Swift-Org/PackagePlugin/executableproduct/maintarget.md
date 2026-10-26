---
url: "https://docs.swift.org/latest/documentation/packageplugin/executableproduct/maintarget"
framework: "Swift-Org/PackagePlugin"
---

# mainTarget

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

The target that contains the main entry point of the executable.

## Declaration

```swift
let mainTarget: Target
```

#### Discussion

Every executable product has exactly one main executable target. This target will always be one of the targets in the product’s `targets` array.

## See Also

### Inspecting an Executable Target
- [let id: ID](./id.md)
  Unique identifier for the product.
- [let name: String](./name.md)
  The name of the product, as defined in the package manifest.
- [let targets: [Target]](./targets.md)
  The targets that directly comprise the product, in the order in which they are declared in the package manifest.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/executableproduct/maintarget)*