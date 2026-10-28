---
url: "https://docs.swift.org/latest/documentation/packageplugin/target/dependencies"
framework: "Swift-Org/PackagePlugin"
---

# dependencies

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Any other targets on which this target depends, in the same order as they are specified in the package manifest.

## Declaration

```swift
var dependencies: [TargetDependency] { get }
```

## Discussion

Conditional dependencies that do not apply are filtered out.

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
- [var recursiveTargetDependencies: [Target]](./recursivetargetdependencies.md)
  The transitive closure of all the targets on which the receiver depends.
- [typealias ID](./id-swift.typealias.md)
  The type that represents the ID of the target.
- [var directory: Path](./directory.md)
  The absolute path of the target directory in the local file system.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/target/dependencies)*