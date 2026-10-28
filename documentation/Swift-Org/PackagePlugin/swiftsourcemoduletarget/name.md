---
url: "https://docs.swift.org/latest/documentation/packageplugin/swiftsourcemoduletarget/name"
framework: "Swift-Org/PackagePlugin"
---

# name

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

The name of the target, as defined in the package manifest.

## Declaration

```swift
let name: String
```

## Discussion

This name is unique among the targets of the package in which it is defined.

## See Also

### Inspecting a Swift Source Module Target
- [let id: ID](./id.md)
  Unique identifier for the target.
- [let kind: ModuleKind](./kind.md)
  The kind of module, describing whether it contains unit tests, contains the main entry point of an executable, or neither.
- [let moduleName: String](./modulename.md)
  The name of the module produced by the target.
- [let directoryURL: URL](./directoryurl.md)
  The file URL of the target directory in the local file system.
- [let dependencies: [TargetDependency]](./dependencies.md)
  Any other targets on which this target depends, in the same order as specified in the package manifest.
- [let compilationConditions: [String]](./compilationconditions.md)
  Any custom compilation conditions specified for the Swift target in the package manifest.
- [let directory: Path](./directory.md)
  The absolute path of the target directory in the local file system.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/swiftsourcemoduletarget/name)*