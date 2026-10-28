---
url: "https://docs.swift.org/latest/documentation/packageplugin/swiftsourcemoduletarget/modulename"
framework: "Swift-Org/PackagePlugin"
---

# moduleName

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

The name of the module produced by the target.

## Declaration

```swift
let moduleName: String
```

## Discussion

This is derived from the target name, though future Swift package manager versions may allow this to be customized.

## See Also

### Inspecting a Swift Source Module Target
- [let id: ID](./id.md)
  Unique identifier for the target.
- [let name: String](./name.md)
  The name of the target, as defined in the package manifest.
- [let kind: ModuleKind](./kind.md)
  The kind of module, describing whether it contains unit tests, contains the main entry point of an executable, or neither.
- [let directoryURL: URL](./directoryurl.md)
  The file URL of the target directory in the local file system.
- [let dependencies: [TargetDependency]](./dependencies.md)
  Any other targets on which this target depends, in the same order as specified in the package manifest.
- [let compilationConditions: [String]](./compilationconditions.md)
  Any custom compilation conditions specified for the Swift target in the package manifest.
- [let directory: Path](./directory.md)
  The absolute path of the target directory in the local file system.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/swiftsourcemoduletarget/modulename)*