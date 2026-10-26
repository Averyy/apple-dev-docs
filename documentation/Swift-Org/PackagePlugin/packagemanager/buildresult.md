---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/buildresult"
framework: "Swift-Org/PackagePlugin"
---

# PackageManager.BuildResult

**Framework**: Swift-Org/PackagePlugin  
**Kind**: struct  
**Role**: Structure

The results of running a build.

## Declaration

```swift
struct BuildResult
```

## Topics

### Inspecting a Build Result
- [var builtArtifacts: [BuiltArtifact]](./buildresult/builtartifacts.md)
  The artifacts built from the products in the package.
- [var logText: String](./buildresult/logtext.md)
  The log output.
- [var succeeded: Bool](./buildresult/succeeded.md)
  A Boolean value that indicates whether the build succeeded or failed.
- [PackageManager.BuildResult.BuiltArtifact](./buildresult/builtartifact.md)
  The single artifact produced during a build.

## See Also

### Building a Package
- [func build(BuildSubset, parameters: BuildParameters) throws -> BuildResult](./build%28_,parameters%29.md)
  Performs a build of all, or a subset, of products and targets in a package.
- [PackageManager.BuildSubset](./buildsubset.md)
  Specifies a subset of package products and targets to build.
- [PackageManager.BuildParameters](./buildparameters.md)
  Parameters and options to apply during a build.
- [PackageManager.BuildConfiguration](./buildconfiguration.md)
  The configuration to use for the build.
- [PackageManager.BuildLogVerbosity](./buildlogverbosity.md)
  The amount of detail to include in a build log.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/buildresult)*