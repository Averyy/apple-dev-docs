---
url: "https://docs.swift.org/latest/documentation/packageplugin/binaryartifacttarget/directoryurl"
framework: "Swift-Org/PackagePlugin"
---

# directoryURL

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

The file URL of the target directory in the local file system.

**Availability**:
- SwiftPM 6.0+

## Declaration

```swift
let directoryURL: URL
```

## See Also

### Inspecting the Target
- [let id: ID](./id.md)
  Unique identifier for the target.
- [let name: String](./name.md)
  The name of the target, as defined in the package manifest.
- [let kind: Kind](./kind-swift.property.md)
  The kind of binary artifact.
- [let origin: Origin](./origin-swift.property.md)
  The original source of the binary artifact.
- [let artifactURL: URL](./artifacturl.md)
  The file URL of the location of the binary artifact in the local file system.
- [let dependencies: [TargetDependency]](./dependencies.md)
  Any other targets on which this target depends, in the same order as specified in the package manifest.
- [BinaryArtifactTarget.Kind](./kind-swift.enum.md)
  A kind of binary artifact.
- [BinaryArtifactTarget.Origin](./origin-swift.enum.md)
  The original location of a binary artifact.
- [let artifact: Path](./artifact.md)
  The path location of the binary artifact in the local file system.
- [let directory: Path](./directory.md)
  The absolute path of the target directory in the local file system.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/binaryartifacttarget/directoryurl)*