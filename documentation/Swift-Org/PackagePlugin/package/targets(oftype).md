---
url: "https://docs.swift.org/latest/documentation/packageplugin/package/targets(oftype:)"
framework: "Swift-Org/PackagePlugin"
---

# targets(ofType:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: method  
**Role**: Instance Method

The targets in this package that conform to a specific type.

## Declaration

```swift
func targets<T>(ofType: T.Type) -> [T] where T : Target
```

## See Also

### Inspecting Package Targets
- [let targets: [Target]](./targets.md)
  Any regular targets defined in this packagewith the exception of plugin targets.
- [func targets(named: [String]) throws -> [Target]](./targets%28named%29.md)
  The list of targets matching the given names.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/package/targets(oftype:))*