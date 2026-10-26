---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/buildresult/builtartifact"
framework: "Swift-Org/PackagePlugin"
---

# PackageManager.BuildResult.BuiltArtifact

**Framework**: Swift-Org/PackagePlugin  
**Kind**: struct  
**Role**: Structure

The single artifact produced during a build.

## Declaration

```swift
struct BuiltArtifact
```

## Topics

### Inspecting a Build Artifact
- [var kind: Kind](./builtartifact/kind-swift.property.md)
  The kind of artifact built.
- [var url: URL](./builtartifact/url.md)
  The file URL of the built artifact in the local file system.
- [PackageManager.BuildResult.BuiltArtifact.Kind](./builtartifact/kind-swift.enum.md)
  The kind of artifact built.
- [var path: Path](./builtartifact/path.md)
  Full path of the built artifact in the local file system.

## See Also

### Inspecting a Build Result
- [var builtArtifacts: [BuiltArtifact]](./builtartifacts.md)
  The artifacts built from the products in the package.
- [var logText: String](./logtext.md)
  The log output.
- [var succeeded: Bool](./succeeded.md)
  A Boolean value that indicates whether the build succeeded or failed.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/buildresult/builtartifact)*