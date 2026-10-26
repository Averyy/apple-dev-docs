---
url: "https://docs.swift.org/latest/documentation/packageplugin/systemlibrarytarget/compilerflags"
framework: "Swift-Org/PackagePlugin"
---

# compilerFlags

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

Flags from `pkg-config` to pass to Clang and SwiftC.

## Declaration

```swift
let compilerFlags: [String]
```

#### Discussion

Flags are passed to using `-Xcc`.

## See Also

### Inspecting the System Library Target
- [let id: ID](./id.md)
  Unique identifier for the target.
- [var name: String](./name.md)
  The name of the target, as defined in the package manifest.
- [let pkgConfig: String?](./pkgconfig.md)
  The name of the `pkg-config` file, if any, describing the library.
- [var dependencies: [TargetDependency]](./dependencies.md)
  Any other targets on which this target depends, in the same order as specified in the package manifest.
- [let linkerFlags: [String]](./linkerflags.md)
  Flags from `pkg-config` to pass to the platform linker.
- [var directoryURL: URL](./directoryurl.md)
  The file URL of the target directory in the local file system.
- [var directory: Path](./directory.md)
  The absolute path of the target directory in the local file system.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/systemlibrarytarget/compilerflags)*