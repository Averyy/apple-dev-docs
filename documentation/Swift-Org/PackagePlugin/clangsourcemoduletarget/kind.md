---
url: "https://docs.swift.org/latest/documentation/packageplugin/clangsourcemoduletarget/kind"
framework: "Swift-Org/PackagePlugin"
---

# kind

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

The kind of module.

## Declaration

```swift
let kind: ModuleKind
```

#### Discussion

The kind of module describes whether it contains unit tests, the main entry point of an executable, or neither.

## See Also

### Inspecting a Clang Source Module Target
- [let id: ID](./id.md)
  Unique identifier for the target.
- [let name: String](./name.md)
  The name of the target, as defined in the package manifest.
- [let moduleName: String](./modulename.md)
  The name of the module produced by the target.
- [let directoryURL: URL](./directoryurl.md)
  The file URL of the target directory in the local file system.
- [let dependencies: [TargetDependency]](./dependencies.md)
  Any other targets on which this target depends, in the same order as specified in the package manifest.
- [let headerSearchPaths: [String]](./headersearchpaths.md)
  Any custom header search paths specified for the Clang target.
- [let preprocessorDefinitions: [String]](./preprocessordefinitions.md)
  Any preprocessor definitions specified for the Clang target.
- [let directory: Path](./directory.md)
  The absolute path of the target directory in the local file system.
- [let publicHeadersDirectory: Path?](./publicheadersdirectory.md)
  The directory containing public C headers, if applicable.
- [let publicHeadersDirectoryURL: URL?](./publicheadersdirectoryurl.md)
  The directory containing public C headers, if applicable.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/clangsourcemoduletarget/kind)*