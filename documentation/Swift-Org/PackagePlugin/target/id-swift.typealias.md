---
url: "https://docs.swift.org/latest/documentation/packageplugin/target/id-swift.typealias"
framework: "Swift-Org/PackagePlugin"
---

# Target.ID

**Framework**: Swift-Org/PackagePlugin  
**Kind**: typealias  
**Role**: Type Alias

The type that represents the ID of the target.

## Declaration

```swift
typealias ID = String
```

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
- [var recursiveTargetDependencies: [Target]](./recursivetargetdependencies.md)
  The transitive closure of all the targets on which the receiver depends.
- [var directory: Path](./directory.md)
  The absolute path of the target directory in the local file system.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/target/id-swift.typealias)*