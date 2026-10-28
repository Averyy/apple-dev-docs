---
url: "https://docs.swift.org/latest/documentation/packageplugin/clangsourcemoduletarget/name"
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

### Inspecting a Clang Source Module Target
- [let id: ID](./id.md)
  Unique identifier for the target.
- [let kind: ModuleKind](./kind.md)
  The kind of module.
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/clangsourcemoduletarget/name)*