---
url: "https://docs.swift.org/latest/documentation/packageplugin/package/targets"
framework: "Swift-Org/PackagePlugin"
---

# targets

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

Any regular targets defined in this packagewith the exception of plugin targets.

## Declaration

```swift
let targets: [Target]
```

## Discussion

The targets are specified in the same order as the package manifest.

## See Also

### Inspecting Package Targets
- [func targets(named: [String]) throws -> [Target]](./targets%28named%29.md)
  The list of targets matching the given names.
- [func targets<T>(ofType: T.Type) -> [T]](./targets%28oftype%29.md)
  The targets in this package that conform to a specific type.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/package/targets)*