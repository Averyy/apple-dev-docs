---
url: "https://docs.swift.org/latest/documentation/packageplugin/executableproduct/targets"
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

The product contains the transitive closure of the these targets and their dependencies. For an `ExecutableProduct`, exactly one of the targets in this list must be an `ExecutableTarget`.

## See Also

### Inspecting an Executable Target
- [let id: ID](./id.md)
  Unique identifier for the product.
- [let name: String](./name.md)
  The name of the product, as defined in the package manifest.
- [let mainTarget: Target](./maintarget.md)
  The target that contains the main entry point of the executable.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/executableproduct/targets)*