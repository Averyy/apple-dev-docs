---
url: "https://docs.swift.org/latest/documentation/packageplugin/target/name"
framework: "Swift-Org/PackagePlugin"
---

# name

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The name of the target, as defined in the package manifest.

## Declaration

```swift
var name: String { get }
```

## Discussion

This name is unique among the targets of the package in which it is defined.

## See Also

### Inspecting a target
- [var id: ID](./id-swift.property.md)
  Unique identifier for the target.
- [var directoryURL: URL](./directoryurl.md)
  The file URL of the target directory in the local file system.
- [var sourceModule: SourceModuleTarget?](./sourcemodule.md)
  Convenience accessor which casts the receiver to`SourceModuleTarget`, if possible.
- [var dependencies: [TargetDependency]](./dependencies.md)
  Any other targets on which this target depends, in the same order as they are specified in the package manifest.
- [var recursiveTargetDependencies: [Target]](./recursivetargetdependencies.md)
  The transitive closure of all the targets on which the receiver depends.
- [typealias ID](./id-swift.typealias.md)
  The type that represents the ID of the target.
- [var directory: Path](./directory.md)
  The absolute path of the target directory in the local file system.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/target/name)*