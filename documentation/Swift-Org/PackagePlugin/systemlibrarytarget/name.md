---
url: "https://docs.swift.org/latest/documentation/packageplugin/systemlibrarytarget/name"
framework: "Swift-Org/PackagePlugin"
---

# name

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

The name of the target, as defined in the package manifest.

## Declaration

```swift
var name: String
```

#### Discussion

This name is unique among the targets of the package in which it is defined.

## See Also

### Inspecting the System Library Target
- [let id: ID](./id.md)
  Unique identifier for the target.
- [let pkgConfig: String?](./pkgconfig.md)
  The name of the `pkg-config` file, if any, describing the library.
- [var dependencies: [TargetDependency]](./dependencies.md)
  Any other targets on which this target depends, in the same order as specified in the package manifest.
- [let compilerFlags: [String]](./compilerflags.md)
  Flags from `pkg-config` to pass to Clang and SwiftC.
- [let linkerFlags: [String]](./linkerflags.md)
  Flags from `pkg-config` to pass to the platform linker.
- [var directoryURL: URL](./directoryurl.md)
  The file URL of the target directory in the local file system.
- [var directory: Path](./directory.md)
  The absolute path of the target directory in the local file system.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/systemlibrarytarget/name)*