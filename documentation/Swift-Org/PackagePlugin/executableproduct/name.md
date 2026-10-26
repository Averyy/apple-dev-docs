---
url: "https://docs.swift.org/latest/documentation/packageplugin/executableproduct/name"
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

### Inspecting an Executable Target
- [let id: ID](./id.md)
  Unique identifier for the product.
- [let mainTarget: Target](./maintarget.md)
  The target that contains the main entry point of the executable.
- [let targets: [Target]](./targets.md)
  The targets that directly comprise the product, in the order in which they are declared in the package manifest.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/executableproduct/name)*