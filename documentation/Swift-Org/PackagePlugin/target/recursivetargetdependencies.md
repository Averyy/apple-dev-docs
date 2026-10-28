---
url: "https://docs.swift.org/latest/documentation/packageplugin/target/recursivetargetdependencies"
framework: "Swift-Org/PackagePlugin"
---

# recursiveTargetDependencies

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

The transitive closure of all the targets on which the receiver depends.

## Declaration

```swift
var recursiveTargetDependencies: [Target] { get }
```

## Discussion

Package manager orders the results such that every dependency appears before any other target that depends on it.

The dependencies are sorted in topological sort order.

## See Also

### Inspecting a target
- [var id: ID](./id-swift.property.md)
  Unique identifier for the target.
- [var name: String](./name.md)
  The name of the target, as defined in the package manifest.
- [var directoryURL: URL](./directoryurl.md)
  The file URL of the target directory in the local file system.
- [var sourceModule: SourceModuleTarget?](./sourcemodule.md)
  Convenience accessor which casts the receiver to`SourceModuleTarget`, if possible.
- [var dependencies: [TargetDependency]](./dependencies.md)
  Any other targets on which this target depends, in the same order as they are specified in the package manifest.
- [typealias ID](./id-swift.typealias.md)
  The type that represents the ID of the target.
- [var directory: Path](./directory.md)
  The absolute path of the target directory in the local file system.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/target/recursivetargetdependencies)*