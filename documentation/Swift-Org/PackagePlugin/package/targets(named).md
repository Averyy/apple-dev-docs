---
url: "https://docs.swift.org/latest/documentation/packageplugin/package/targets(named:)"
framework: "Swift-Org/PackagePlugin"
---

# targets(named:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: method  
**Role**: Instance Method

The list of targets matching the given names.

## Declaration

```swift
func targets(named targetNames: [String]) throws -> [Target]
```

## Discussion

Throws an error if any of the targets cannot be found.

## See Also

### Inspecting Package Targets
- [let targets: [Target]](./targets.md)
  Any regular targets defined in this packagewith the exception of plugin targets.
- [func targets<T>(ofType: T.Type) -> [T]](./targets%28oftype%29.md)
  The targets in this package that conform to a specific type.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/package/targets(named:))*